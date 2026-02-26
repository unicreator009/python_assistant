import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import pywhatkit
import wikipedia


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            command = command.lower()
            print(f"you said: {command}")
            return command
        except:
            speak("sorry, i did not understand that")
            return ""


def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("opening youtube.")

def search_google(query):
      pywhatkit.search(query)
      speak(f"searching for {query} on google.")

def open_calculator():
    subprocess.Popen("calc.exe")
    speak("opening calculator.")

def open_notepad():
    subprocess.Popen("notepad.exe")
    speak("opening notepad.")


def open_google():
    webbrowser.open("https://www.google.com")
    speak("opening google.")

def answer_question(question):
    try:
        result = wikipedia.summary(question, sentences=2)  
        print(result)
        speak(result)
    except:
        speak("sorry, i could not find an answer to that question. Opening google.")

        webbrowser.open(f"https://www.google.com/search?q={question}")

def main():
    speak("hello i am your digital assistant. how can i help you?")
    while True:
        command = listen()

        if "open youtube" in command:
            open_youtube()
        elif "open google" in command:
            open_google()
        elif "open calculator" in command:
            open_calculator()
        elif "open notepad" in command:
            open_notepad()
        elif "search" in command:
            query = command.replace("search" , " ")
            search_google(query)
        elif "who is" in command or "what is" in command:
            answer_question(command)
        elif "open copilot" in command:
            open_copilot()

        elif "exit" in command or "quit" in command:
            speak("goodbye!")
            break

        elif command != "":
            speak("searching for you.")
          
            search_google(command)

       
        
if __name__ == "__main__":
    main()
