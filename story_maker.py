import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow  
import random as rn
import pyttsx3

# text to speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# story elements
characters = [
    "knight", "thief", "scientist", "traveler", "king", "queen", 
    "wizard", "farmer", "teacher", "doctor", "soldier", "merchant", 
    "pirate", "detective", "chef", "student", "musician", "dancer", 
    "artist", "explorer"
]

personalities = [
    "brave", "shy", "curious", "scary", "kind", "happy", 
    "sad", "funny", "angry", "calm", "quiet", "nice", 
    "mean", "smart", "lazy", "strong", "weak", "friendly", 
    "serious"
]

places = [
    "a forest", "a haunted house", "a castle", "a mountain", 
    "a beach", "a village", "a big city", "an island", "a cave", 
    "a desert", "a spaceship", "a farm", "a jungle", "a small town", 
    "a boat", "a library", "a magical world", "a palace", "a school", "a zoo"
]

goals = [
    "find a hidden treasure", "escape a deadly trap", "save the world", 
    "win a big race", "solve a mystery", "build a home", "find a lost pet", 
    "make new friends", "climb a tall mountain", "learn a magic spell", 
    "catch a thief", "find a safe place", "fix a broken machine", "discover a secret"
]

class StoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Story_maker.clicked.connect(self.generate_story)

    def generate_story(self):
        character = rn.choice(characters)
        personality = rn.choice(personalities)
        place = rn.choice(places)
        goal = rn.choice(goals)

    
        if place in ["a forest", "a desert", "a mountain", "a jungle"]:
            story = f"A {personality} {character} journeyed through {place} to {goal}."
        elif place in ["a castle", "a haunted house", "a palace", "a magical world"]:
            story = f"In {place}, a {personality} {character} set out to {goal}."
        elif place in ["a city", "a village", "a small town", "a school"]:
            story = f"A {personality} {character} in {place} sought to {goal}."
        elif place == "a spaceship":
            story = f"A {personality} {character} aboard a spaceship was determined to {goal}."
        else:
            story = f"A {personality} {character} in {place} embarked on a quest to {goal}."
        self.ui.story_box.setPlainText(story)
        engine.say(story)
        engine.runAndWait()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StoryApp()
    window.show()
    sys.exit(app.exec_())
