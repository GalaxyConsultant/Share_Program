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
import sys


# 🔐 비밀번호 그대로 유지
PASSWORD = "change"


# ================================
#  🔥 exe 환경에서도 ADB 절대경로 보장
# ================================
if getattr(sys, 'frozen', False):
    APP_DIR = os.path.dirname(sys.executable)
else:
    APP_DIR = os.path.dirname(os.path.abspath(__file__))

ADB = os.path.join(APP_DIR, "adb.exe")


# ================================
#  실행 함수
# ================================
def run(cmd: str):
    """subprocess 실행 + strip 오류 방지"""
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    out = p.stdout.strip() if p.stdout else ""
    err = p.stderr.strip() if p.stderr else ""
    return out, err, p.returncode


def check_adb():
    out, err, code = run(f'"{ADB}" devices')
    if code != 0:
        messagebox.showerror("오류", f"adb 실행 실패\n\n{err}")
        return False

    lines = [l for l in out.splitlines() if l.strip()]
    if len(lines) <= 1:
        messagebox.showerror("오류", "ADB 연결 없음")
        return False

    return True


def check_su():
    _, _, code = run(f'"{ADB}" shell su -c "id"')
    return code == 0


# ================================
#  값 자동 생성
# ================================
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
        name = device = product = code

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


# ================================
#  스크립트 생성
# ================================
def build_script(vals):
    m  = vals["model"]
    nm = vals["name"]
    dv = vals["device"]
    pd = vals["product"]
    br = vals["brand"]
    mf = vals["manufacturer"]
    ch = vals["characteristics"]
    fp = vals["fingerprint"]

    lines = [
        "#!/system/bin/sh",
        f"resetprop ro.product.model {m}",
        f"resetprop ro.product.name {nm}",
        f"resetprop ro.product.device {dv}",
        f"resetprop ro.product.brand {br}",
        f"resetprop ro.product.manufacturer {mf}",
        f"resetprop ro.product.product {pd}",

        f"resetprop ro.product.system.model {m}",
        f"resetprop ro.product.system.name {nm}",
        f"resetprop ro.product.system.device {dv}",

        f"resetprop ro.product.vendor.model {m}",
        f"resetprop ro.product.vendor.name {nm}",
        f"resetprop ro.product.vendor.device {dv}",

        f"resetprop ro.product.odm.model {m}",
        f"resetprop ro.product.odm.name {nm}",
        f"resetprop ro.product.odm.device {dv}",

        f"resetprop ro.product.system_ext.model {m}",
        f"resetprop ro.product.system_ext.name {nm}",
        f"resetprop ro.product.system_ext.device {dv}",

        f"resetprop ro.build.product {dv}",
        f"resetprop ro.build.characteristics {ch}",
        "resetprop ro.build.type user",
        "resetprop ro.build.tags release-keys",

        f"resetprop ro.build.fingerprint \"{fp}\"",
        f"resetprop ro.product.build.fingerprint \"{fp}\"",
        f"resetprop ro.system.build.fingerprint \"{fp}\"",
        f"resetprop ro.vendor.build.fingerprint \"{fp}\"",
        f"resetprop ro.odm.build.fingerprint \"{fp}\"",
        f"resetprop ro.system_ext.build.fingerprint \"{fp}\"",
    ]

    return "\n".join(lines)


# ================================
#  post-fs-data 스크립트 생성
# ================================
def create_postfs_script():
    try:
        if not check_adb():
            return
        if not check_su():
            messagebox.showerror("오류", "su 권한 필요")
            return

        model = simpledialog.askstring("모델명 입력", "변경할 모델명을 입력하세요.")
        if model is None:
            return
        if model.strip() == "":
            messagebox.showerror("오류", "모델명이 비어있습니다.")
            return

        vals = auto_generate_values(model)
        script_text = build_script(vals)

        # temp 파일 생성
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".sh")
        tmp.write(script_text.encode("utf-8"))
        tmp.close()

        local = tmp.name
        remote_tmp = "/data/local/tmp/prop_spoof.sh"
        final = "/data/adb/post-fs-data.d/99-prop-spoof.sh"

        # push
        run(f'"{ADB}" push "{local}" "{remote_tmp}"')

        # 이동 + 권한
        run(f'"{ADB}" shell su -c "mkdir -p /data/adb/post-fs-data.d"')
        run(f'"{ADB}" shell su -c "mv {remote_tmp} {final}"')
        run(f'"{ADB}" shell su -c "chmod 755 {final}"')

        # 즉시 실행
        run(f'"{ADB}" shell su -c "sh {final}"')

        # 결과 확인
        keys = [
            "ro.product.model",
            "ro.build.product",
            "ro.build.characteristics"
        ]

        result = []
        for k in keys:
            out, _, _ = run(f'"{ADB}" shell getprop {k}')
            result.append(f"{k}: {out}")

        messagebox.showinfo("완료", "\n".join(result) + "\n\n재부팅하면 항상 적용됩니다.")

        if messagebox.askyesno("재부팅", "지금 재부팅할까요?"):
            run(f'"{ADB}" shell su -c "reboot"')

        os.unlink(local)

    except Exception as e:
        messagebox.showerror("예상치 못한 오류", f"{e}")


# ================================
#  UI
# ================================
def start_ui():

    # 비밀번호 입력
    pwd = simpledialog.askstring("비밀번호", "비밀번호 입력:", show="*")
    if pwd is None:
        return
    if pwd != PASSWORD:
        messagebox.showerror("오류", "비밀번호가 틀렸습니다.")
        return

    ui = tk.Tk()
    ui.title("Post-fs Prop Spoofer Creator")
    ui.geometry("520x230")

    msg = tk.Label(
        ui,
        text="※ Magisk 루팅 기기에서만 작동합니다.",
        pady=15
    )
    msg.pack()

    btn = tk.Button(
        ui,
        text="모델명 변경하기",
        height=2,
        command=create_postfs_script
    )
    btn.pack(fill="x", padx=40, pady=15)

    ui.mainloop()


def main():
    start_ui()


if __name__ == "__main__":
    main()
