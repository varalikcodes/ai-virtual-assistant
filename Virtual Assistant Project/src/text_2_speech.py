import pyttsx3

def test_text_to_speech():
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    print("About to speak...")  # Print before speaking
    engine.say("Hello! I am your virtual assistant. How can I help you today?")
    engine.runAndWait()  # Wait for the speech to finish
    print("Finished speaking.")  # Print after speaking

# Test the function
test_text_to_speech()