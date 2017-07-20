"""
Simple cross-platform TTS (text-to-speech) module for Python 3
Uses pywin32 on Windows and eSpeak on Linux

Installation of dependencies:
Windows: pip install pywin32
Linux: sudo apt-get install espeak python3-espeak
"""

# Get name string of the host operating system
import platform
OSNAME = platform.uname().system

# Host OS is Windows
if OSNAME == "Windows":
    # Import the Windows TTS module
    try:
        import win32com.client
    # TTS module is not present on the system
    except ImportError as ex:
        print("Unable to import Win32 module! Make sure pywin32 is installed on your system!")
        print(ex)

# Host OS is Linux
elif OSNAME == "Linux":
    # Import the Linux TTS module
    try:
        from espeak import espeak
    # TTS module is not present on the system
    except ImportError as ex:
        print("Unable to import eSpeak module! Make sure it is installed on your system!")
        print(ex)

# Unknown host OS
else:
    raise Exception("Unknown host operating system! Unable to import proper text-to-speech module!")

def speak(text, *args):
    """
    Reads the specified text string using the OS-specific TTS module
    text: Text string to read
    *args: Optional voice index argument (used by Windows TTS)
    """
    # Windows - pywin32 - SAPI
    if OSNAME == "Windows":
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        # If the optional argument is specified
        if args:
            # Get the voice index from the argument list
            voiceid = int(args[0])
            # Counter of available voices
            voicecounter = 0

            # Iterate through the avaiable voices
            for voice in speaker.GetVoices():
                # The requested voice index reached
                if voicecounter == voiceid:
                    # Select the voice and break the voice selection loop
                    speaker.Voice = voice
                    break
                # Current voice's index is lower than the requested one
                else:
                    voicecounter += 1

        # Read the text string
        speaker.Speak(text)

    # Linux - eSpeak
    elif OSNAME == "Linux":
        # Read the text string
        espeak.synth(text)
