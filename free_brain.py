
from datetime import datetime
import webbrowser
import random
import subprocess
from urllib.parse import quote_plus


def ask_assistant(question):
    question = question.lower().strip()

    # 1. Greetings
    if question in ["hello", "hi", "hey"] or question.startswith(
        ("hello ", "hi ", "hey ")
    ):
        return "Hello! Nice to hear from you."

    # 2. Time
    elif "time" in question or "clock" in question:
        return "The current time is " + datetime.now().strftime("%I:%M %p")

    # 3. Date
    elif "date" in question or "today" in question:
        return "Today is " + datetime.now().strftime("%A, %d %B %Y")

    # 4. Assistant identity
    elif "your name" in question or "who are you" in question:
        return "I am your personal Python voice assistant."

    # 5. Conversation
    elif "how are you" in question:
        return "I am doing great! How can I help you?"

    elif "hear me" in question or "can you hear" in question:
        return "Yes! I can hear you clearly."

    elif "what can you do" in question:
        return (
            "I can tell the time and date, answer basic questions, "
            "search Google, open websites and desktop applications."
        )

    # 6. Basic educational information
    elif "what is python" in question or "meaning of python" in question:
        return (
            "Python is a popular high-level programming language. "
            "It is used in artificial intelligence, data science, "
            "web development and automation."
        )

    elif "what is artificial intelligence" in question or "what is ai" in question:
        return (
            "Artificial Intelligence enables machines to perform "
            "tasks that normally require human intelligence."
        )

    elif "what is machine learning" in question or "what is ml" in question:
        return (
            "Machine Learning is a branch of artificial intelligence "
            "that allows computers to learn from data."
        )

    # 7. Jokes
    elif "joke" in question:
        jokes = [
            "Why did the computer go to the doctor? It had a virus!",
            "Why was the computer cold? It left its Windows open!"
        ]
        return random.choice(jokes)

    # 8. Open websites
    elif "youtube" in question:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "wikipedia" in question:
        webbrowser.open("https://www.wikipedia.org")
        return "Opening Wikipedia."

    elif "open google" in question:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    # 9. Open Windows applications
    elif "open notepad" in question:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."

    elif "open calculator" in question or "open calc" in question:
        subprocess.Popen(["calc.exe"])
        return "Opening Calculator."

    # 10. Search Google
    elif "search" in question or question.startswith("google"):
        search_text = question

        for phrase in ["search for", "search", "google"]:
            search_text = search_text.replace(phrase, "", 1).strip()

        if not search_text:
            return "Please tell me what you want to search for."

        webbrowser.open(
            "https://www.google.com/search?q=" + quote_plus(search_text)
        )
        return "Searching Google for " + search_text

    # 11. Thank you
    elif "thank" in question:
        return "You're welcome!"

    # 12. Search when the assistant does not recognize a question
    else:
        webbrowser.open(
            "https://www.google.com/search?q=" + quote_plus(question)
        )
        return (
            "I don't have a ready answer for that. "
            "I am searching Google for " + question
        )
