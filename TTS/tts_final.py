from gtts import gTTS
import pygame
import io

def tts(detected_objects):
    if not detected_objects:
        detected_text = "물체가 감지되지 않았습니다."
    else:
        detected_text = "전방에: " + ", ".join(detected_objects) + " 수거함이 있습니다."

    tts = gTTS(text=detected_text, lang='ko')
    
    # 음성 데이터를 메모리 버퍼에 저장
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # pygame 초기화 및 음성 재생
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue