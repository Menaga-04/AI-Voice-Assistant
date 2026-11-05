
import pyttsx3
import speech_recognition as sr
from free_brain import ask_assistant

# Voice output function
def speak(text):
    print("Assistant:", text)

    engine = None

    try:
        engine = pyttsx3.init('sapi5')
        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        engine.say(str(text))
        engine.runAndWait()

    except Exception as e:
        print("Voice error:", e)

    finally:
        if engine is not None:
            engine.stop()
            del engine


# Microphone setup
recognizer = sr.Recognizer()


def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now!")

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.WaitTimeoutError:
        print("No speech detected. Please try again.")
        return ""

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service error.")
        return ""

    except Exception as e:
        print("Microphone error:", e)
        return ""


# Welcome message
speak("Hello! I am your voice assistant. How can I help you?")


# Main assistant loop
while True:

    command = listen()

    if not command:
        continue

    if "exit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        break

    response = ask_assistant(command)

    # Speak every answer
    speak(response)
