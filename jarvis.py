import speech_recognition as sr
import pyttsx3
import os

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Define the function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Sorry, there was an error processing your request: {e}")

# Get user input
comment = recognize_speech()

# Save comment to a file
with open("comments.txt", "a") as f:
    f.write(comment + "\n")

# Read comments from the file
with open("comments.txt", "r") as f:
    comments = f.readlines()

# Print the comments
print("Comments:")
for comment in comments:
    print(comment)
    
# Change the voice of the program
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speak the comments using the new voice
for comment in comments:
    engine.say(comment)
    engine.runAndWait()
