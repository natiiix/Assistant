"""
This module is used for speech-to-text conversion.

It uses the speech_recognition module to perform
the audio recording as well as the conversion itself.
"""

# Try to import speech recognition module
try:
    import speech_recognition as sr
# If the module is not present in the system
except ImportError as ex:
    print("Unable to import speech recognition module! Make sure it is installed on your system!")
    print(ex)

# ======== FOR DEBUGGING PURPOSES ========
import synthesizer

def listen():
    """
    This function records an audio sequence using microphone,
    processes it using Google's Speech API and returns the
    resolved string if the conversion was successful.
    If the conversion has failed, None is returned instead.
    """
    # obtain audio from the microphone
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        synthesizer.speak("Listening")
        audio = rec.listen(source)

    synthesizer.speak("Processing")
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use
        # `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return rec.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
