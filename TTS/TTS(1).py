#Roboflow API를 통해 데이터를 받아와 객체 탐지 결과에 따라 TTS 기능을 구현하는 코드.
#'requests'라이브러리를 사용해 Roboflow API에 GET 요청을 보내고, 반환된 데이터를 처리하여 TTS 처리
#pip install requests pyttsx3


import requests
import pyttsx3
import json
import time

# Roboflow API endpoint 및 API key 설정
API_ENDPOINT = 'https://api.roboflow.com/dataset/{dataset_id}/annotations'
API_KEY = 'your_api_key_here'  # Roboflow API 키

# TTS 엔진 초기화
engine = pyttsx3.init()


# 객체 탐지 및 TTS 연결 함수 정의
def detect_and_speak_objects(image_url, classes):
    # 이미지 URL을 이용하여 객체 탐지 및 TTS 실행
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content

            # 여기서부터 객체 탐지 코드 추가
            # 예시로 클래스를 하드코딩하여 구현
            detected_classes = ['cat', 'dog', 'chair']  # 예시 클래스

            # TTS를 사용하여 탐지된 클래스 음성 출력
            for obj_class in detected_classes:
                text_to_speak = f"Detected {obj_class}"
                engine.say(text_to_speak)
                engine.runAndWait()
                time.sleep(0.1)  # 0.1초 대기

        else:
            print(f"Failed to fetch image data: Status code {response.status_code}")
    except Exception as e:
        print(f"Error occurred during request: {e}")


# Roboflow API를 통해 데이터 받아오기
def fetch_data_from_roboflow(dataset_id):
    try:
        headers = {
            'Authorization': f'Bearer {API_KEY}'
        }
        url = API_ENDPOINT.format(dataset_id=dataset_id)
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # 데이터 처리 로직 추가 (예: 이미지 URL 추출 및 객체 탐지 함수 호출)
            for entry in data:
                image_url = entry['image_url']
                detect_and_speak_objects(image_url, classes=['cat', 'dog', 'chair'])  # 예시 클래스
        else:
            print(f"Failed to fetch data from Roboflow API: Status code {response.status_code}")
    except Exception as e:
        print(f"Error occurred during API request: {e}")


# 메인 함수
def main():
    # Roboflow 데이터셋 ID 설정 (실제 사용할 데이터셋 ID로 대체 필요)
    dataset_id = 'your_dataset_id_here'  # Roboflow 데이터셋 ID

    # Roboflow API를 통해 데이터 받아오기
    fetch_data_from_roboflow(dataset_id)


if __name__ == "__main__":
    main()