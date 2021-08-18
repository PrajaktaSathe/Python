import requests

from projects.sachinl0har.chatbots.helper import say, run


def cnt(_input: str):
    print(_input)
    url = f"http://api.brainshop.ai/get?bid=157984&key=3S0hhLXZ5GS2KYs4&uid=[uid]&msg=[{_input}]"
    r = requests.get(url)
    return r.json()['cnt']


def acro(_input, recognizer=None, microphone=None):
    response = cnt(_input)
    say(response)


if __name__ == "__main__":
    run("Acro", acro)
