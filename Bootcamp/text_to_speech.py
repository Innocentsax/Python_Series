import pyttsx3

text = input("Enter a text which you want to convert to speech: ")

engine = pyttsx3.init()
engine.save_to_file(text, 'audio_record.mp3')
#engine.say(text)

engine.runAndWait()
