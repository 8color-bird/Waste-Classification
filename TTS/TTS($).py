import os
import cv2
import numpy as np
from roboflow import Roboflow
from gtts import gTTS
from playsound import playsound
import tempfile
from collections import Counter
import time

# Roboflow API를 통해 데이터셋 다운로드
rf = Roboflow(api_key="GU4mhuwv8vHYi5IzBfep")
project = rf.workspace("waste-detection-oss-prj").project("8-color-bird-waste-detection")
dataset = project.version(1).download("yolov8")

# YOLOv8 모델 로드 (이미 제공된 yolov8.py를 활용)
model = YOLO("yolov8.weights")

# 이미지 경로 설정 (다운로드된 데이터셋에서 이미지 파일 선택)
image_path = os.path.join(dataset.location, "train", "your_image_file.jpg")

# 이미지 로드
image = cv2.imread(image_path)
(H, W) = image.shape[:2]

# 객체 탐지 수행
results = model.predict(image)


# 탐지된 객체 처리 및 설명 생성
def generate_description(results, model):
    class_counts = Counter()
    for result in results:
        for detection in result:
            classID = detection[5]
            class_counts[model.names[classID]] += 1

    if not class_counts:
        return "탐지된 객체가 없습니다."

    most_common = class_counts.most_common(2)

    if len(most_common) == 1 or most_common[0][1] > most_common[1][1]:
        description = most_common[0][0]
    else:
        description = "분간이 어렵습니다."

    return description


description = generate_description(results, model)


# 텍스트 설명을 TTS로 변환하여 실시간으로 재생
def speak_text(text, lang='ko'):
    tts = gTTS(text=text, lang=lang, slow=False)
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts.save(fp.name + ".mp3")
        playsound(fp.name + ".mp3")


# 탐지 결과를 1초 후에 음성으로 출력
time.sleep(1)
speak_text(description)