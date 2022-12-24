import datetime
import operator
import os
import webbrowser
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()


# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey smart code' in command:
                command = command.replace('smart code', '')
                print(command)
    except:
        pass
    return command


def run_smartcode():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('the time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'Who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

        def get_operator(self, op):
            return {
                '+': operator.add,
                '-': operator.sub,
                'x': operator.mul,
                'divided': operator.__truediv__,
                'Mod': operator.mod,
                'mod': operator.mod,
                '^': operator.xor,
            }[op]

        def open_things(self, command):
            if command == "open youtube":
                talk("Opening YouTube.")
                webbrowser.open("https://www.youtube.com/channel/UCW34Ghe9-_TCA5Vy3-Agfnw")
                pass

            elif command == "open facebook":
                talk("Opening Facebook.")
                webbrowser.open("https://www.facebook.com")
                pass

            elif command == "open netflix":
                talk("Opening netflix.")
                os.startfile("https://www.netflix.com/tz/")
                pass

            elif command == "open spotify":
                talk("open spotify")
                os.startfile("https://open.spotify.com/playlist/2DLjklBlwaERsjOBeYFYyU")
                pass

            else:
                talk("I don't know how to open that yet.")
                pass

    elif 'thank you' in command:
        talk('happy to help')
    elif 'helo' in command:
        talk('im fine too')
    elif 'who made you' in command:
        talk('I was designed by smart codes in Dar-es-Salaam')
    elif 'who are you' in command:
        talk('Im. smart code your. Assistant. How can I help you?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_smartcode()
