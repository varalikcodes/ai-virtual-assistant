import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def test_voice_recognition():
    with sr.Microphone() as source:
        print("Listening... Say something!")
        # Listen for input
        audio = recognizer.listen(source)
        try:
            # Recognize speech
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Error connecting to the recognition service.")

# Test the function
test_voice_recognition()
