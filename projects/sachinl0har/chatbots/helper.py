from datetime import datetime

import pyttsx3

import speech_recognition as sr

engine = pyttsx3.init()


def say(sentence: str):
    print(sentence)

    engine.say(sentence)
    engine.runAndWait()


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


def run(name: str, func):
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    wish_me()
    say(f"{name} here, how may I help you?")

    while True:
        _input = recognize_speech_from_mic(recognizer, microphone)

        if not _input["error"]:
            print(_input["transcription"])
            func(_input["transcription"], recognizer, microphone)
        else:
            say(_input["error"])


def wish_me():
    now = datetime.now()
    hour = now.hour

    times = [("morning", (0 <= hour < 12)), ("afternoon", (12 <= hour < 18)), ("evening", (18 <= hour < 24))]

    for time in times:
        if time[1]:
            say(f"Good {time[0]}!")
