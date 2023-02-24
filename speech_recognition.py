import speech_recognition as sr

def speech_to_text():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something: ")
        audio = r.listen(source)
        print("Done")

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
        except Exception as e:
            print(e)

speech_to_text()  
