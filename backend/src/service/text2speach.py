from gtts import gTTS
import requests
import tempfile


mytext = "Салам алейкум"
language = "ru"

myobj = gTTS(text=mytext, lang=language, slow=False)


with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_file:
    myobj.save(temp_file.name)

    with open(temp_file.name, "rb") as file:
        audio_bytes = file.read()

    # отправка файла

    file.close()
