from gtts import gTTS


def create_mp3(text):
    mytext = text
    language = 'pl'
    
    sound = gTTS(text=mytext, lang=language, slow=False)
    sound.save("static/sound.mp3")
    sound.save("assets/sound.mp3")


