# 시각장애인을 위한 분리수거함 네비게이터 개발
– Yolov8을 활용한 실시간 객체 탐지 기능 및 TTS 기능 중심으로 개발함.

## 목차
1. 프로젝트 설명
2. 개발 기간
3. 팀원 정보
4. 개발환경
5. 설치
6. 사용법

## 1. 프로젝트 설명
본 프로젝트에서는 시각장애인이 폐기물을 정확하게 분리할 수 있도록 지원하는 AI 기반 모바일 웹 서비스를 개발하는 것을 목표로 하였다.
이를 위해 가장 안정적인 모델인 YOLOv8를 활용한 높은 속도 및 정확도를 가진 "쓰레기 분리수거함 실시간 객체 탐지 모듈"과, 쓰레기 분류수거함의 종류를 시각장애인에게 알려주는 "한국어 TTS 음성 안내 모듈"을 연결하여 적용하였다.

본 프로젝트의 사용환경은 1> 폐기물을 배출하고자 하는 분리수거함에 내용물이 있는 상태, 2> 사용자(시각장애인)이 배출하고자 하는 폐기물은 촉각을 통해 미리 분류를 해둔 상태를 가정하고 있다.

특히 분리수거를 할 때 분리수거함의 이름표를 인식하는 방법도 있지만 분리수거함의 이름표와 폐기물의 내용물이 불일치하는 경우가 간혹 있다. 때로는 이름표가 없거나, 오염 및 훼손되는 등 이름표를 식별하기 어려운 경우도 있으므로, 분리수거 함 내의 내용물을 토대로 안내하는 상황을 가정하고 있다.

**(1) Real-time Object Detection(실시간 객체 인식) 모듈**<br/>
본 프로젝트에서는 객체 탐지 모델 중 가장 정확도와 안정도가 높은 YOLOv8 오픈소스를 활용하여 종이, 플라스틱, 캔, 유리, 스티로폼, 비닐, 페트 총 7개의 재활용 가능한 물체에 대한 객체 탐지를 가능하게 하는 모듈을 개발하였다. 또한 이 과정에서 AI-hub의 "재활용품 선별 이미지 데이터" 와 roboflow labeling api를 활용하였다.<br/>

![image](https://github.com/8color-bird/Waste-Classification/assets/102949053/1518c5db-8442-46fc-966d-ba73ab446547)
<br/>(Roboflow를 활용한 annotation 과정)

**(2) Text-To-Speech(이하 TTS, 음성 인식) 모듈**<br/>
gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API 를 기반으로한 TTS 모델을 사용하였다.
(https://github.com/pndurette/gTTS) 또한 해당 모듈을 커스터마이징하여 YOLOv8 재활용품 객체 탐지 모델의 결과 데이터를 인식하여 음성으로 출력하도록 하였다.

**(3) UI**<br/>
UI의 경우, 재활용 이미지를 상징하는 초록색과 녹색 및 해당 색깔과 함께할때 시인성이 좋은 흰색으로 MAIN COLOR를 선택하였다.
또한 색각이상자를 위한 컬러 유니버셜 디자인 가이드에 맞추어 색상 분포 및 UI 디자인을 진행하였다. 특히 초록색 중에서도 적록생맹을 위한 Bluish Green으로 메인 색상을 채택하였다. (#009E73)

## 2. 개발 기간
2024/05/12(일) ~ 2024/06/20(목)
- 제안서 작성
- 데이터 수집 및 가공
- 객체 탐지 모델 학습 및 생성
- TTS 모델 개발
- 앱 개발

## 3. 팀원 정보
- **고예린** : 팀장, 프로젝트 총괄 매니징, 실시간 객체 탐지 모델 개발 및 UI 개발
- **김시영** : 팀원1, 실시간 객체 탐지 모델 개발, 데이터 가공
- **손예림** : 팀원2, 실시간 객체 탐지 모델 개발, 데이터 가공
- **임소정** : 팀원3, TTS 모델 개발, 보고서 주필 작성

## 4. 개발 환경
- Python 3.10.12
- Colab 및 JupyterNotebook
- Gradio 라이브러리

## 5. 개발과정
(1) Waste_Classification_using_YOLOv8_V4_final.ipynb를 작성<br/>
(2) 해당 ipynb 코드를 실행하여 best.pt 라는 가중치 모델을 추출하였다<br/>
(3) 오픈소스를 바탕으로 tts_final.py 를 작성(TTS폴더 내부에 있음)<br/>
(4) ui를 위해 styles.css 파일 작성<br/>
(5) best.pt, tts_final.py, styles.css 활용하여 main.ipynb 작성<br/>
(6) main.ipynb 를 실행할 시 gradio 기반의 웹앱 서비스가 실행되도록 구현하였다.<br/>

## 6. 사용법
main.ipynb 실행 시 시각장애인이 폐기물을 정확하게 분리할 수 있도록 지원하는 AI 기반 모바일 웹 서비스를 실행할 수 있다.

아래 코드에 본인이 사용할 Roboflow API key, Workspace ID, Project ID 를 입력하여 사용할 수 있다.
```Python
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="your_api_key")
project = rf.workspace("your_workspace_ID").project("your_project_ID")
version = project.version(4)
dataset = version.download("yolov8")
```

<br/>이외 세부적인 모듈별 사용방법은 "5. 개발과정" 항목을 참고.

## 7. 라이센스
LICENSE 파일 참조.

## FAQ
기타 문의사항은 https://github.com/8color-bird/Waste-Classification/ 깃헙의 issues 항목에 작성요함.
