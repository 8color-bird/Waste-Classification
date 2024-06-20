from gtts import gTTS
import tempfile
import os

def tts(detected_objects):
    if not detected_objects:
        detected_text = "물체가 감지되지 않았습니다."
    else:
        detected_text = "전방에: " + ", ".join(detected_objects)+"수거함이 있습니다."

    tts = gTTS(text=detected_text, lang='ko')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(temp_file.name)
    
    with open(temp_file.name, 'rb') as f:
        tts_result = f.read()

    os.unlink(temp_file.name)  # 임시 파일 삭제
    return tts_result