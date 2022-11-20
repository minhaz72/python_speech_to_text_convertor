# python speech to text convertor : 
import speech_recognition as sr 

a=sr.Recognizer()
 
with sr.Microphone() as src: 
    print(' Ask Anything : ')
    audio=a.lisent(src)
    try : 
        text= a.recognize_google(audio)
        print('text : ' ,text )
    except : 
        print('  sooory your audio is not clear : ')


 