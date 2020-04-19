import speech_recognition as sr


def takeCommand():
    print("Press any key to start.")
    e = input()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio)
        print(f"User Said: {query}\n")
        # speak(query)

    except Exception as e:
        print(e)

        print("Sorry sir please!! say that again..")

        return "None"

    return query


if __name__ == "__main__":
    takeCommand()
