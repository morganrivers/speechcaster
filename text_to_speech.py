from gtts import gTTS
with open('out.txt') as f:
    text = f.read()
    print(text)
    # quit()
    # for l in lines:
        # text = l.replace('\n','')
        # if(text == ''):
            # continue
    tts = gTTS(text=text, lang='en')
    tts.save("test.wav")