import speech_recognition as sr
import pyttsx3
import os
import subprocess
import webbrowser
import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for user input and converts it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble with the speech recognition service.")
            return ""

def perform_task(command):
    """Performs tasks based on user command."""
    if 'open' in command:
        if 'notepad' in command:
            speak("Opening Notepad")
            subprocess.Popen('notepad.exe')
        elif 'browser' in command:
            speak("Opening web browser")
            webbrowser.open('https://www.google.com')
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'exit' or 'thankyou' in command or 'quit' in command:
        speak("Its ok , Goodbye!")
        exit()

def main():
    """Main function to run the voice assistant."""
    speak("Hello, I am your voice assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            perform_task(command)

if __name__ == "__main__":
    main()
