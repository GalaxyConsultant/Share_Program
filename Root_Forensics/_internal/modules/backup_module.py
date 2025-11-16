# -*- coding: utf-8 -*-
import subprocess
import threading
import os
from tkinter import simpledialog, messagebox, END

ADB = "adb"


# -------------------------------
# 기본 실행 함수
# -------------------------------
def run(cmd):
    subprocess.Popen(cmd, shell=True).wait()


# ================================================================
#   1) 일반 백업 (컨텐츠 : DCIM / Pictures / Movies / Download 등)
#   비밀번호: back
# ================================================================
def run_general_backup(output):
    """사진/영상/문서/다운로드 자동 백업"""

    pwd = simpledialog.askstring("비밀번호", "비밀번호 입력:", show="*")
    if pwd != "back":
        messagebox.showerror("오류", "비밀번호가 틀렸습니다.")
        return

    def worker():

        output.delete(1.0, END)
        output.insert(END, "[일반 백업 시작]\n")

        backup_root = "backup_general"
        os.makedirs(backup_root, exist_ok=True)

        paths = {
            "DCIM": "/sdcard/DCIM",
            "Pictures": "/sdcard/Pictures",
            "Movies": "/sdcard/Movies",
            "Music": "/sdcard/Music",
            "Documents": "/sdcard/Documents",
            "Download": "/sdcard/Download",
        }

        for name, dpath in paths.items():
            output.insert(END, f"→ {name} 백업 중...\n")
            local_dir = os.path.join(backup_root, name)
            os.makedirs(local_dir, exist_ok=True)
            run(f'{ADB} pull "{dpath}" "{local_dir}"')

        output.insert(END, "\n[일반 백업 완료]\n저장폴더: backup_general/\n")

    threading.Thread(target=worker, daemon=True).start()



# ================================================================
#   2) 특정 백업 (DB 포함 가능)
#   비밀번호: backback
# ================================================================
def run_specific_backup(output):
    """사용자가 직접 입력한 경로 pull"""

    pwd = simpledialog.askstring("비밀번호", "비밀번호 입력:", show="*")
    if pwd != "backback":
        messagebox.showerror("오류", "비밀번호가 틀렸습니다.")
        return

    target = simpledialog.askstring(
        "백업할 경로 입력",
        "TWRP 기준 절대경로를 입력하세요.\n예: /data/user/0/com.android.providers.contacts/databases"
    )
    if not target:
        return

    def worker():
        output.delete(1.0, END)
        output.insert(END, "[특정 백업 시작]\n")

        backup_root = "backup_specific"
        os.makedirs(backup_root, exist_ok=True)

        save_path = os.path.join(backup_root, target.replace("/", "_"))
        os.makedirs(save_path, exist_ok=True)

        output.insert(END, f"→ {target} 백업 중...\n")
        run(f'{ADB} pull "{target}" "{save_path}"')

        output.insert(END, f"\n[특정 백업 완료]\n저장폴더: {save_path}\n")

    threading.Thread(target=worker, daemon=True).start()
