# -*- coding: utf-8 -*-
"""
Post-fs-data Prop Spoofer Creator (push 방식 안정화 버전)
- MagiskHide Props Config 불필요
- EOF 오류 없는 방식 (adb push → mv)
"""

import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog
import tempfile
import os

PASSWORD = "change"
ADB = "adb"


# -------------------------------
def run(cmd: str):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return p.stdout.strip(), p.stderr.strip(), p.returncode


def check_adb():
    out, err, code = run(f"{ADB} devices")
    if code != 0:
        messagebox.showerror("오류", f"adb 실행 실패\n\n{err}")
        return False

    lines = [l for l in out.splitlines() if l.strip()]
    if len(lines) <= 1:
        messagebox.showerror("오류", "ADB 연결 없음")
        return False
    return True


def check_su():
    _, _, code = run(f'{ADB} shell su -c "id"')
    return code == 0


# -------------------------------
def auto_generate_values(model):
    brand = "Samsung"
    manu = "Samsung"

    code = model.replace("SM-", "").replace("SM", "").lower()

    presets = {
        "p615n": ("gta4lwifi", "gta4lwifi", "gta4lwifi"),
        "p610": ("gta4lwifi", "gta4lwifi", "gta4lwifi"),

        "n981n": ("o1s", "o1s", "o1s"),
        "g998n": ("p4s", "p4s", "p4s"),
        "s908n": ("b0q", "b0q", "b0q"),

        "a505n": ("a50", "a50", "a50"),
        "a528n": ("a52s", "a52s", "a52s"),
    }

    if code in presets:
        name, device, product = presets[code]
    else:
        name = code
        device = code
        product = code

    ch = "tablet" if model.upper().startswith("SM-P") else "phone"

    fp = f"{brand}/{product}/{device}:14/QP1A.190711.020/{product}:user/release-keys"

    return {
        "model": model,
        "name": name,
        "device": device,
        "product": product,
        "brand": brand,
        "manufacturer": manu,
        "characteristics": ch,
        "fingerprint": fp
    }


# -------------------------------
def build_script(vals):
    m = vals["model"]
    name = vals["name"]
    dev = vals["device"]
    prod = vals["product"]
    brand = vals["brand"]
    manu = vals["manufacturer"]
    ch = vals["characteristics"]
    fp = vals["fingerprint"]

    lines = [
        "#!/system/bin/sh",
        f"resetprop ro.product.model {m}",
        f"resetprop ro.product.name {name}",
        f"resetprop ro.product.device {dev}",
        f"resetprop ro.product.brand {brand}",
        f"resetprop ro.product.manufacturer {manu}",
        f"resetprop ro.product.product {prod}",
        "",
        f"resetprop ro.product.system.model {m}",
        f"resetprop ro.product.system.name {name}",
        f"resetprop ro.product.system.device {dev}",
        "",
        f"resetprop ro.product.vendor.model {m}",
        f"resetprop ro.product.vendor.name {name}",
        f"resetprop ro.product.vendor.device {dev}",
        "",
        f"resetprop ro.product.odm.model {m}",
        f"resetprop ro.product.odm.name {name}",
        f"resetprop ro.product.odm.device {dev}",
        "",
        f"resetprop ro.product.system_ext.model {m}",
        f"resetprop ro.product.system_ext.name {name}",
        f"resetprop ro.product.system_ext.device {dev}",
        "",
        f"resetprop ro.build.product {dev}",
        f"resetprop ro.build.characteristics {ch}",
        "resetprop ro.build.type user",
        "resetprop ro.build.tags release-keys",
        "",
        f"resetprop ro.build.fingerprint \"{fp}\"",
        f"resetprop ro.product.build.fingerprint \"{fp}\"",
        f"resetprop ro.system.build.fingerprint \"{fp}\"",
        f"resetprop ro.vendor.build.fingerprint \"{fp}\"",
        f"resetprop ro.odm.build.fingerprint \"{fp}\"",
        f"resetprop ro.system_ext.build.fingerprint \"{fp}\"",
        "",
    ]

    return "\n".join(lines)


# -------------------------------
def create_postfs_script():
    if not check_adb():
        return
    if not check_su():
        messagebox.showerror("오류", "su 권한 필요")
        return

    model = simpledialog.askstring("모델명 입력", "적용할 모델명을 입력하세요.")
    if not model:
        return

    vals = auto_generate_values(model)
    script_text = build_script(vals)

    # 임시파일 생성
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".sh")
    temp_file.write(script_text.encode("utf-8"))
    temp_file.close()

    local_path = temp_file.name
    remote_tmp = "/data/local/tmp/prop_spoof.sh"
    final_path = "/data/adb/post-fs-data.d/99-prop-spoof.sh"

    # push
    run(f"{ADB} push {local_path} {remote_tmp}")

    # 이동 + 권한 설정
    run(f'{ADB} shell su -c "mkdir -p /data/adb/post-fs-data.d"')
    run(f'{ADB} shell su -c "mv {remote_tmp} {final_path}"')
    run(f'{ADB} shell su -c "chmod 755 {final_path}"')

    # 즉시 실행
    run(f'{ADB} shell su -c "sh {final_path}"')

    # 확인
    check_keys = [
        "ro.product.model",
        "ro.build.product",
        "ro.build.characteristics"
    ]
    results = []
    for k in check_keys:
        out, _, _ = run(f'{ADB} shell getprop {k}')
        results.append(f"{k}: {out}")

    messagebox.showinfo("완료", "\n".join(results) + "\n\n재부팅하면 항상 자동 적용됩니다.")

    if messagebox.askyesno("재부팅", "지금 재부팅할까요?"):
        run(f'{ADB} shell su -c "reboot"')

    os.unlink(local_path)


# -------------------------------
def start_ui():
    ui = tk.Tk()
    ui.title("Post-fs Prop Spoofer Creator")
    ui.geometry("520x230")

    label = tk.Label(
        ui,
        text=(
            "※ 모델명 변경 전 Magisk가 설치된 루팅 단말기인지 확인하세요"
        ),
        justify="left",
        padx=10,
        pady=10
    )
    label.pack(fill="x")

    btn = tk.Button(ui, text="모델명 변경하기", height=2, command=create_postfs_script)
    btn.pack(fill="x", padx=40, pady=15)

    ui.mainloop()


def main():
    root = tk.Tk()
    root.withdraw()

    pwd = simpledialog.askstring("비밀번호", "비밀번호 입력:", show="*")
    if pwd != PASSWORD:
        messagebox.showerror("오류", "비밀번호가 틀렸습니다.")
        return

    start_ui()


if __name__ == "__main__":
    main()
