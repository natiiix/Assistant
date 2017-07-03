# Try to import speech recognition module
try:
    import speech_recognition as sr
# If the module is not present in the system
except ImportError as e:
    print("Unable to import speech recognition module! Make sure it is installed on your system!")
    print(e)

# ======== FOR DEBUGGING PURPOSES ========
import synthesizer

def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        synthesizer.speak("Listening")
        audio = r.listen(source)
        
    synthesizer.speak("Processing")
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None
