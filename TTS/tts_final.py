from gtts import gTTS
import tempfile

def tts(detected_objects):
    if not detected_objects:
        detected_text = "물체가 감지되지 않았습니다."
    else:
        detected_text = "전방에: " + ", ".join(detected_objects) + " 수거함이 있습니다."

    tts = gTTS(text=detected_text, lang='ko')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(temp_file.name)

    return temp_file.name
