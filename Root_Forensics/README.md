🛡️ Root_Forensics

Android TWRP 백업 · 루팅 단말기 모델명 변경 · 잠금해제 자동화 툴

[📦 Root_Forensics 다운로드](https://download-directory.github.io/?url=https://github.com/GalaxyConsultant/Share_Program/tree/main/Root_Forensics)


📌 개요

Root_Forensics는 Android 단말기 분석 및 포렌식 작업을 간편하게 수행하기 위한 도구입니다.
루팅(Magisk) 또는 TWRP Recovery 환경에서 사용하는 기능들을 PC에서 GUI 기반으로 한 번에 처리할 수 있도록 제작되었습니다.

이 프로그램은 다음 3가지 핵심 기능을 제공합니다:

ADB 백업 (TWRP 전용)

모델명 변경 (Magisk 루팅 단말기 전용)

잠금화면 강제 제거 (TWRP 전용)

심플한 Dark UI 기반으로, 여러 PC 환경에서도 안정적으로 작동하도록 설계되었습니다.

🚀 기능 설명
1) 🔄 ADB 백업

TWRP Recovery 환경에서 실행하는 백업 기능입니다.
두 가지 모드가 제공됩니다:

✔ 일반 백업

기본 사용자 데이터(사진·동영상·문서 등)를 자동으로 PC로 백업합니다.

TWRP에서는 앱 영역 접근이 가능하므로
일반 사용자 컨텐츠는 자동 백업이 가능합니다.

✔ 특정 백업

앱 DB 또는 특정 파일 경로를 입력하여 선택적으로 백업하는 기능입니다.

앱 데이터(DB, shared_prefs, files 등)가 그대로 PC에 추출됩니다.

2) 🛠️ 모델명 변경 (Magisk 루팅 단말기 전용)

Magisk가 설치된 루팅 기기에서 model 값들을 자동으로 변경하여
카카오톡, 인스타그램, 특정 게임 등의 기기 제한을 우회하거나
모델명을 변경하고자 할 때 사용됩니다.


변경 스크립트는 /data/adb/post-fs-data.d에 저장되며
재부팅 후에도 자동 적용됩니다.

3) 🔓 잠금해제 (TWRP 전용)

TWRP Recovery에서 다음 파일을 삭제하여
핀/패턴/비밀번호 잠금 화면을 초기화합니다:


🖥️ 프로그램 화면 구성

상단: 3개의 핵심 기능 버튼

[ ADB 백업 ]   [ 모델명 변경 ]   [ 잠금해제 ]


중앙: 진행 상태 출력창 (실제 명령어는 숨기고 상태만 표시)

하단: 기능 설명 안내 문구

📂 폴더 구조

빌드된 프로그램 배포 시 다음 구조를 유지해야 합니다:

Root_Forensics/
 ├── Root_Forensics.exe
 ├── modules/
 │    ├── backup_module.py
 │    ├── custom_cmd_module.py
 │    └── prop_spoofer_postfs.py
 ├── adb.exe
 ├── AdbWinApi.dll
 ├── AdbWinUsbApi.dll
 ├── _internal/     ← 파이썬 런타임 포함 (필수)
 └── Root.ico


_internal 폴더는 반드시 포함되어야 하며
삭제하면 프로그램이 실행되지 않습니다.


⚠️ 유의사항

백업/잠금해제 기능은 TWRP Recovery 모드에서만 정상 작동

모델명 변경은 Magisk 루팅 단말기에서만 사용 가능

프로그램 사용으로 인한 오류는 사용자 책임

반드시 본인 소유 기기에서만 사용해야 함

📝 License

This project is provided for personal research & forensic usage.
