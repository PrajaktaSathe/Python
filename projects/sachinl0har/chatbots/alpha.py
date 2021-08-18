import random
import webbrowser
from datetime import datetime

from requests import get
import pyjokes

from projects.sachinl0har.chatbots.helper import say, recognize_speech_from_mic, run


def alpha(query, recognizer, microphone):
    # Search something on google
    if "search" in query:
        say("What would you like to search?")
        _input = recognize_speech_from_mic(recognizer, microphone)

        if not _input["error"]:
            search = _input["transcription"]
            webbrowser.open(search)
        else:
            say(_input["error"])

    # Whats the time
    elif "time" in query:
        now = datetime.now().strftime("%H:%M:%S")
        say(f"The Time is {now}")

    # Simple talks
    elif any(_input in query for _input in ["how are you", "what's up"]):
        replies = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                   'i am okay! How are you?']

        reply = random.choice(replies)
        say(reply)

        _input = recognize_speech_from_mic(recognizer, microphone)

        if not _input["error"]:
            user_response = _input["transcription"]

            if 'fine' in user_response or 'happy' in user_response or 'okay' in user_response:
                say('okay..')
            elif 'not' in user_response or 'sad' in user_response or 'upset' in user_response:
                say('oh sorry..')
        else:
            say(_input["error"])

    elif any(_input in query for _input in ['who made you', 'who created you', 'who developed you']):
        say("For your information Sachin Lohar AKA ALPHA Created me! I give Lot of Thanks to Him")

    elif "who are you" in query or "about yourself" in query or "your details" in query:
        about = "I am ALPHA an AI based computer program but i can help you lot like a your close friend! i " \
                "promise you! Simple try me to give simple command! like playing music or video from your " \
                "directory i also play video and song from web or online! i can also entertain you i so think you " \
                "Understand me! ok Lets Start"
        say(about)

    elif "hello" in query or "hello ALPHA" in query:
        say("Hello Sir! How May i Help you..")

    elif "name" in query:
        say("Thanks for Asking my name! It is ALPHA")

    elif "you feeling" in query:
        say("feeling Very sweet after meeting with you")

    # IP address
    elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        say(f"Your IP address is {ip}")

    # Joke
    elif "tell me a joke" in query:
        joke = pyjokes.get_joke()
        say(joke)

    # FIXME: This section looks unsafe.
    # elif "shut down the system" in query:
    #     os.system("shutdown /s /t 5")
    # elif "restart the system" in query:
    #     os.system("shutdown /r /t 5")
    # elif "sleep the system" in query:
    #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


if __name__ == "__main__":
    run("Alpha", alpha)
