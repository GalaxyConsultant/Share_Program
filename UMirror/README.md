\### 📥 UMirror 다운로드

\[!\[Download Folder](https://img.shields.io/badge/Download-UMirror-blue?style=for-the-badge\&logo=github)](https://download-directory.github.io/?url=https://github.com/GalaxyConsultant/Share\_Program/tree/main/UMirror)







📱 UMirror v17



무선 디버깅 + TextBridge 입력기 + 패키지 설치 + 멀티 디바이스 미러링 통합 툴



UMirror v17은 안드로이드 기기를 PC에서 쉽고 빠르게 미러링하고,



PC 키보드로 한글까지 안정적으로 입력할 수 있는 TextBridge,



무선 디버깅 연결, 패키지 설치 도우미 기능을 포함한 올인원 ADB 기반 유틸리티입니다.



scrcpy 기반 미러링을 더 강력하고 편하게 사용할 수 있도록 구성되었습니다.



🚀 주요 기능



🔹 1. 화면 미러링 (scrcpy 기반)



버튼 한 번으로 선택한 기기 화면을 PC로 미러링



창 제목 자동 구분(UMirror-시리얼)



텍스트 입력 최적화를 위한 --prefer-text 옵션 적용



여러 기기 동시 연결 가능



🔹 2. TextBridge (PC → 스마트폰 입력 연동)



PC 키보드로 입력한 내용을 스마트폰에 자동 전송



한글 포함 모든 문자 안전하게 변환



스마트폰이 영어/한글이 섞여도 안정적으로 입력 가능



개별 디바이스마다 별도 TextBridge 입력창 활성화



🔹 3. 무선 디버깅(Wi-Fi) 지원



전용 다이얼로그에서 IP, 포트, PIN 입력만으로



ADB Pair



ADB Connect



둘 다 쉽게 처리 가능



유선 연결 없이도 미러링 가능



🔹 4. 패키지 자동 설치 도우미



UMirror 실행에 필요한 패키지를



버튼 클릭 한 번



자동 설치 로그 출력



설치 실패 시 즉시 확인 가능



별도 CMD창 없이 UMirror 내부에서 처리됩니다.



🔹 5. 멀티 디바이스 자동 감지



PC에 연결된 모든 기기 목록을 자동 표시



새로고침 버튼으로 즉시 목록 업데이트



기기 선택 후 미러링/입력 기능 사용 가능



🔹 6. 실시간 로그 출력



모든 연결, 입력, 실행 결과를 GUI에서 확인



가독성 높은 다크 테마 적용



자동 스크롤로 최신 로그 유지



🔹 7. 연결 초기화 \& 전체 종료



ADB disconnect 전체 초기화



실행 중인 scrcpy 프로세스 일괄 종료



미러링 재연결 시 오류 방지



🖥️ UI 구성



상단 기능 버튼: 패키지 설치 / 무선 디버깅 / 화면연결 / 새로고침 / 초기화 / 종료



중단: 연결된 기기 리스트



하단: 로그창 + TextBridge 입력창



밝기 낮은 다크 테마 구성



Consolas 기반의 텍스트 가독성 강화



📌 사용 방법



1\) USB 디버깅 활성화



스마트폰 → 개발자 옵션 → USB 디버깅 ON



2\) 프로그램 실행



UMirror.exe 실행



3\) 기기 목록 확인



“새로고침”으로 연결된 디바이스 확인



4\) 화면 연결



기기 선택 → "화면연결"



→ scrcpy 미러링 자동 실행



5\) TextBridge 입력



미러링이 시작되면 하단에 입력창 생성



→ 입력 후 Enter → 스마트폰으로 전송



6\) 무선 디버깅 (선택)



Wi-Fi 사용 시 “무선 디버깅” 메뉴에서



IP / 포트 / PIN 입력 후 Pair \& Connect



7\) 종료



scrcpy 전체 종료



ADB 연결 초기화



둘 다 버튼 제공



⚠️ 주의사항



scrcpy는 환경변수에 등록되어 있어야 실행됩니다.



무선 디버깅은 동일한 네트워크 환경에서만 연결됩니다.



TextBridge 입력은 일부 앱에서 변환 규칙에 따라 동작 방식이 다를 수 있습니다.

