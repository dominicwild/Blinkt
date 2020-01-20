from blinkt import set_pixel as set, get_pixel, clear, set_all, set_brightness, set_clear_on_exit, show
from enum import Enum
from random import randint
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Color(Enum):
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    YELLOW = [255, 225, 25]

    @staticmethod
    def toColor(text):
        switch = {
            "b": Color.BLUE,
            "blue": Color.BLUE,
            "r": Color.RED,
            "red": Color.RED,
            "g": Color.GREEN,
            "green": Color.GREEN,
            "y": Color.YELLOW,
            "yellow": Color.YELLOW
        }
        return switch.get(text.lower(), False)


class Button():
    def __init__(self, color, leds):
        self.color = color
        self.leds = leds

    def toString(self):
        "Color: " + self.color.name + "\n" + self.leds.toString()


class SimonSays():
    buttons = []
    sequence = []

    def addButton(self, color, leds):
        self.buttons.append(Button(color, leds))

    def lightButton(self, buttonNum, sleepTime=1):
        button = self.buttons[buttonNum]
        set_pixel(button.leds[0], button.color)
        set_pixel(button.leds[1], button.color)
        show()
        time.sleep(sleepTime)
        self.reset()
        print("")

    def display(self):
        show()

    def reset(self):
        clear()

    def textMode(self):
        print("Playing the text version of Simon.")
        print("Write your guesses with spaces separating the colours i.e., 'y b r g' for guessing yellow, blue, red and then green, in that order")
        playing = True
        points = 0
        while playing:
            # Show colour
            rand = randint(0, len(self.buttons)-1)
            self.sequence.append(self.buttons[rand].color)
            self.lightButton(rand, 1)
            correct = self.parseGuess(
                input("What was the sequence of lights?\n> "))
            if(correct):
                points += 1
                cls()
                print("That was correct. You have " + str(points) + " points")
            else:
                print("That was incorrect. You finished with " + str(points) + " points")
                print("The correct sequence was " + self.getStringSequence())
                playing = False

    def parseGuess(self, guess):
        guessedSequence = guess.split(" ")
        for i in range(len(self.sequence)):
            if(Color.toColor(guessedSequence[i]) == self.sequence[i]):
                continue
            else:
                return False
        return True

    def getStringSequence(self):
        stringSeq = ""
        for i in range(len(self.sequence)):
            stringSeq += self.sequence[i].name + " "
        return stringSeq

    def start(self):
        while True: 
            option = input("Select which Simon you'd like to play: ")
            mode = {"1": self.textMode}
            toPlay = mode.get(option, False)
            if(toPlay):
                toPlay()


def set_pixel(pixel, color):
    value = color.value
    set(pixel, value[0], value[1], value[2])


simon = SimonSays()
simon.addButton(Color.RED, [0, 1])
simon.addButton(Color.GREEN, [2, 3])
simon.addButton(Color.YELLOW, [4, 5])
simon.addButton(Color.BLUE, [6, 7])

simon.start()
