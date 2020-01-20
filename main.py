from blinkt import set_pixel as set, get_pixel, clear, set_all, set_brightness, set_clear_on_exit, show
from enum import Enum
from random import randint
import time
import os
import csv


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_pixel(pixel, color):
    value = color.value
    set(pixel, value[0], value[1], value[2])

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
    name = False
    scoreFile = "scores.csv"

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
        numSeq = []
        while playing:
            # Show colour
            rand = randint(0, len(self.buttons)-1)
            self.sequence.append(self.buttons[rand].color)
            numSeq.append(rand)
            self.displaySequence(numSeq)
            correct = self.parseGuess(
                input("What was the sequence of lights?\n> "))
            if(correct):
                points += 1
                cls()
                print("That was correct. You have " + str(points) + " points")
            else:
                print("That was incorrect. You finished with " +
                      str(points) + " points")
                print("The correct sequence was " + self.getStringSequence())
                self.storeScore(points)
                self.sequence = []
                playing = False

    def parseGuess(self, guess):
        guessedSequence = guess.split(" ")
        for i in range(len(self.sequence)):
            if(Color.toColor(guessedSequence[i]) == self.sequence[i]):
                continue
            else:
                return False
        # Amount of colours guessed must be equal also
        return len(self.sequence) == len(guessedSequence)

    def displaySequence(self, numSeq):
        for i in numSeq:
            cls()
            self.lightButton(i, 1)
        cls()  # To erase the final light

    def getStringSequence(self):
        stringSeq = ""
        for i in range(len(self.sequence)):
            stringSeq += self.sequence[i].name + " "
        return stringSeq

    def start(self):
        while True:
            self.renderMenu(["Text Based", "View Leaderboard"])
            option = input("Select which an option: ")
            mode = {"1": self.textMode}
            toPlay = mode.get(option, False)
            if(toPlay):
                toPlay()
            else:
                print("That was not a valid option. Please choose again.")

    def renderMenu(self, menu):
        length = 40
        i = 0
        print("#"*length)
        for option in menu:
            i += 1
            print("# " + str(i) + ". " + option +
                  " "*(length - 6 - len(option)) + "#")
        print("#"*length)

    def storeScore(self, points):
        if(self.name == False):
            # Only ask for name when necessary
            self.name = input("What is your name? (for the leaderboard)\n> ")
        try:
            with open(self.scoreFile, "r+") as scores, open("temp.csv", "w+", newline='') as temp:
                writer = csv.writer(temp)
                reader = sorted(csv.reader(scores), key=lambda row: row[1], reverse=True)
                saved = False
                for row in reader:
                    if(row[0] == self.name):
                        if(int(row[1]) < points):
                            row[1] = points
                            print("Your score has been updated in the leaderboard.")
                        else:
                            print("You already have a higher score in the leaderboard.")
                        saved = True
                    
                if(saved == False):
                    reader.append([self.name,points])
                reader.sort(key=lambda row: int(row[1]),reverse=True) #Sort at saving, rather than leaderboard as this could be put on a background thread if it becomes cumbersome and users would get more frustrating if the leaderboard took a long time to load, than they would saving.
                writer.writerows(reader)

        except Exception as e:
            print(e)


        os.replace("temp.csv", self.scoreFile)


    def printLeaderBoard(self):
        with open(self.scoreFile, "r") as scores:
            reader = csv.reader(scores)
            for row in reader:
                print("")





simon = SimonSays()
simon.addButton(Color.RED, [0, 1])
simon.addButton(Color.GREEN, [2, 3])
simon.addButton(Color.YELLOW, [4, 5])
simon.addButton(Color.BLUE, [6, 7])

simon.start()
