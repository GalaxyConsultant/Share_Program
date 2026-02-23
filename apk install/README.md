# 🔧 APK 강제설치 프로그램

ADB를 내장하여 별도 설치 없이 APK를 강제 설치할 수 있는 Windows 전용 프로그램입니다.

---

## 📌 주요 기능

✔ 디버깅 연결 확인 (adb devices)  
✔ APK 강제설치 (파일명만 입력하면 자동으로 .apk 추가)  
✔ 개발자 옵션 및 USB 디버깅 종료  

---

## 📥 다운로드

### 🔽 EXE 직접 다운로드

아래 링크를 클릭하면 바로 다운로드됩니다.

👉 **[APK 강제설치 프로그램 다운로드](https://raw.githubusercontent.com/GalaxyConsultant/Share_Program/main/apk%20install/apk%20install.exe)**

> 다운로드가 바로 되지 않으면  
> 마우스 오른쪽 클릭 → 다른 이름으로 저장

---

## 🖥 실행 방법

1. 스마트폰 USB 연결
2. 휴대폰에서 USB 디버깅 허용
3. 프로그램 실행
4. 원하는 기능 버튼 선택

---

## 📦 사용 방법

### 1️⃣ 디버깅 연결
ADB로 현재 연결된 기기를 확인합니다.

---

### 2️⃣ APK 강제설치

- 설치할 APK 파일을 프로그램과 같은 폴더에 위치
- "APK 강제설치" 버튼 클릭
- 파일명만 입력 (확장자 제외)

예시 입력:1234


---

### 3️⃣ 개발자옵션 종료

ADB를 통해 아래 항목을 비활성화합니다.

- 개발자 옵션
- USB 디버깅

---

## ⚙️ 빌드 정보

- Python + Tkinter 기반
- PyInstaller --onefile 빌드
- ADB 3종 파일 내장
  - adb.exe
  - AdbWinApi.dll
  - AdbWinUsbApi.dll

별도 ADB 설치 필요 없음

---

## ⚠️ 주의사항

- 삼성 USB 드라이버 설치 필요
- Windows Defender 경고 시  
  → "추가 정보" → "실행"

---

## 🏷 제작

GalaxyConsultant  
CodeNote Project