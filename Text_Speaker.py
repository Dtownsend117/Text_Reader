import speech_recognition as sr
import pyttsx3
import pyautogui
import pyperclip
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",180)

def read_highlighted_text():
    
    pyautogui.hotkey('ctrl', 'c') # Simulates the keyboard to compy the highlighted text
    time.sleep(0.5)  # Time window to save text to clipboard
    try:
        # This will retrieve the text from the clipboard
        highlighted_text = pyperclip.paste()
        print("Highlighted text: " + highlighted_text) # This will dispaly the highlighted text
        engine.say(highlighted_text) # This speaks the text
        engine.runAndWait()
    except Exception as e:
        print("Error reading highlighted text:", e)

def voice_commands():
    recognizer = sr.Recognizer()
    
    while True:
        with sr.Microphone() as source:
            print("Listening for commands...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio).lower()
                print("You said: " + command)
                
                # Trigger phrases to read the text, add/change to your liking
                read_phrases = ['read that', 'read this', 'speak that', 'say that']
                
                if any(phrase in command for phrase in read_phrases):
                    read_highlighted_text()
                elif 'exit' in command:
                    print("Exiting...")
                    break
                else:
                    print("Command not recognized. Please say 'read that' or 'exit'.")
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    voice_commands()
