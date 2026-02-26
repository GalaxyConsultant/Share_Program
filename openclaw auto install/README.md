## 다운로드

[![다운로드](https://img.shields.io/badge/다운로드-OpenClawManager.exe-brightgreen?style=for-the-badge)](https://raw.githubusercontent.com/GalaxyConsultant/Share_Program/main/openclaw%20auto%20install/OpenClawManager.exe)

OpenClaw Manager (Windows + WSL)

Windows에서 WSL(Ubuntu) 환경에 OpenClaw + Gemini CLI를 설치하고 실행을 도와주는 간단한 매니저입니다.
버튼을 눌러 PowerShell/메모장을 열고, 안내된 명령어를 복사/붙여넣기만 하면 됩니다.

준비물

Windows 10/11

인터넷 연결

관리자 권한(WSL 설치 시 필요)

설치 순서 (처음 1회)
1) 프로그램 실행

manager.exe 실행

2) [Ubuntu 설치] 버튼

PowerShell이 열리면서 WSL Ubuntu 설치가 진행됩니다.

설치가 끝나면 안내대로 재부팅하세요.

3) Ubuntu 최초 실행(중요)

재부팅 후 PowerShell에서 아래 명령으로 Ubuntu를 한 번 실행하세요.

wsl -d Ubuntu-24.04

처음 실행 시 Ubuntu에서 계정 생성/비밀번호 설정을 요구합니다.
설정이 끝나면 Ubuntu를 종료해도 됩니다.

OpenClaw + Gemini 설치
4) [OpenClaw 설치] 버튼

Ubuntu 안에서 필요한 패키지 설치와 함께 아래 구성 요소가 설치됩니다.

Node.js

Gemini CLI (@google/gemini-cli)

OpenClaw

설치 중 비밀번호 입력(sudo) 을 요구할 수 있습니다.
Ubuntu에서 비밀번호를 입력하면 계속 진행됩니다.

OpenClaw 실행
5) [OpenClaw 실행] 버튼

PowerShell 창과 메모장이 함께 열립니다.

메모장에 나오는 명령어를 순서대로 복사 → 붙여넣기 하세요.

메모장 안내 예시:

Ubuntu 실행

wsl -d Ubuntu-24.04

OpenClaw 실행

openclaw onboard --install-daemon

마지막 줄의 안내대로:
“위 명령어를 복사 붙여넣기해주세요”

자주 발생하는 문제
Ubuntu가 이미 설치되어 있다는 오류가 나와요

이미 Ubuntu 배포판이 존재하는 경우 정상입니다.
그대로 다음 단계로 진행하면 됩니다.

설치/실행 중 비밀번호를 물어봐요

Ubuntu 최초 설정에서 만든 비밀번호를 입력하면 됩니다.
(입력해도 화면에 표시되지 않는 것이 정상입니다.)

OpenClaw 실행이 안 돼요 (command not found 등)

대부분 Ubuntu 최초 실행(계정/비번 설정) 을 안 했거나, 설치가 완료되지 않은 경우입니다.

먼저 Ubuntu 실행이 되는지 확인:

wsl -d Ubuntu-24.04

그 다음 OpenClaw 설치 버튼을 다시 실행해 주세요.

권장 사용 순서 요약

Ubuntu 설치

재부팅

Ubuntu 최초 실행(계정/비번 설정)

OpenClaw 설치

OpenClaw 실행(메모장 명령어 복붙)

안내

본 프로그램은 설치/실행을 돕는 도구입니다.
WSL/Ubuntu 환경이나 네트워크 상태에 따라 설치 시간이 달라질 수 있습니다.