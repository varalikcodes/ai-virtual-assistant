import requests
import speech_recognition as sr
import pyttsx3

# Initialize recognizers
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Your API Key for OpenWeatherMap
API_KEY = "eb506b232ede4df9ecbb11ec9bc0720a"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return None
        except sr.RequestError:
            print("Error connecting to the recognition service.")
            return None

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        return f"The weather in {city} is currently {temp} degrees Celsius with {weather_desc}."
    else:
        return "I couldn't find the weather information for that location."

def main():
    speak("Hello! I am your virtual assistant.")
    while True:
        command = listen()
        if command is not None:
            if "exit" in command.lower():
                speak("Goodbye!")
                break
            elif "hello" in command.lower():
                speak("Hello! How can I assist you today?")
            elif "weather" in command.lower():
                speak("Please tell me the city name.")
                city = listen()
                if city:
                    weather_info = get_weather(city)
                    speak(weather_info)
                else:
                    speak("I didn't catch that.")
            else:
                speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    main()
