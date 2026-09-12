# -*- coding: utf-8 -*-
import subprocess
import threading
import os
import sys
from tkinter import END, simpledialog, messagebox

PASSWORD = "locklock"

# 🔹 여기 3개의 명령어에 네가 직접 TWRP용 명령어 넣어라
cmd1 = "mount -o rw,remount /data"
cmd2 = "rm /data/system/locksettings.db"
cmd3 = "rm /data/system/gatekeeper.pattern.key"


# ================================
#  🔥 PyInstaller exe 환경에서도 adb.exe 정확히 찾도록 수정
# ================================
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

ADB = os.path.join(BASE_DIR, "adb.exe")   # exe와 같은 폴더에 있는 adb.exe 사용


def exec_adb(cmd):
    """
    adb shell 명령 실행 (TWRP 전용)
    su 없이 root shell 바로 실행됨
    """
    full_cmd = f'"{ADB}" shell "{cmd}"'
    subprocess.Popen(
        full_cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ).wait()


def run_custom_commands(output_box):

    # =====================
    # 🔒 비밀번호 입력 처리
    # =====================
    pwd = simpledialog.askstring("비밀번호", "비밀번호 입력:", show="*")

    # (1) 닫기, 취소 → None 반환 → 에러 방지
    if pwd is None:
        return

    # (2) 틀리면 오류
    if pwd != PASSWORD:
        messagebox.showerror("오류", "비밀번호가 틀렸습니다.")
        return

    # =====================
    #  비동기 실행
    # =====================
    def worker():

        output_box.insert(END, "[작업 시작]\n")

        if cmd1 and cmd1.strip():
            output_box.insert(END, "[잠금DB 찾는중...]\n")
            exec_adb(cmd1)
            output_box.insert(END, "[완료]\n")

        if cmd2 and cmd2.strip():
            output_box.insert(END, "[잠금DB 분석중...]\n")
            exec_adb(cmd2)
            output_box.insert(END, "[완료]\n")

        if cmd3 and cmd3.strip():
            output_box.insert(END, "[잠금 해제...]\n")
            exec_adb(cmd3)
            output_box.insert(END, "[완료]\n")

        output_box.insert(END, "\n[잠금해제 작업 완료]\n")

    threading.Thread(target=worker, daemon=True).start()
