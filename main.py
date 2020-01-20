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

class ClassicMode():

    sequence = []
    numSeq = []
    simon = None

    def __init__(self, simon):
        self.simon = simon

    def gameLogic(self):
        rand = randint(0, self.simon.getNumberOfButtons() - 1)
        self.sequence.append(self.simon.getButtonColour(rand))
        self.numSeq.append(rand)

        self.simon.displaySequence(self.numSeq)

    #The amount of score to add on each round
    def calculateScore(self):
        return 1

class DifficultyMode():

    difficulty = -1
    sequence = []
    numSeq = []

    def __init__(self, simon):
        self.simon = simon

    def gameLogic(self):

        while self.difficulty < 0:
            print("In this mode you can create your own custom difficulty.")
            try:
                difficulty = int(input("Input a number to create your difficulty. The higher the number, the more lights you will have to remember in each round of the game, however the more points you'll get!\n> "))
                if(difficulty < 0):
                    print("That is not a valid difficulty, try again. It must be greater than zero.")
            except Exception:
                print("The difficulty must be a number.")
                difficulty = -1

        for i in range(difficulty):
            rand = randint(0, self.simon.getNumberOfButtons() - 1)
            self.sequence.append(self.simon.getButtonColour(rand))
            self.numSeq.append(rand)

        self.simon.displaySequence(self.numSeq)

    #The amount of score to add on each round
    def calculateScore(self):
        return self.difficulty*self.difficulty

class SimonSays():
    buttons = []
    name = ""
    scoreFile = "scores.csv"

    def getNumberOfButtons(self):
        return len(self.buttons)

    def getButtonColour(self, index):
        return self.buttons[index].color

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
        mode = "Invalid option"
        while mode == "Invalid option":
            self.renderMenu(["Classic Mode", "Difficulty Mode"])
            option = input("Which mode do you want to play? (input the number):\n> ")
            modes = {"1" : ClassicMode(self), "2": DifficultyMode(self)}
            mode = modes.get(option, "Invalid option")
        print("Playing the text version of Simon.")
        print("Write your guesses with spaces separating the colours i.e., 'y b r g' for guessing yellow, blue, red and then green, in that order")
        playing = True
        points = 0
        
        while playing:
            mode.gameLogic()
            correct = self.parseGuess(input("What was the sequence of lights?\n> "))
            if (correct):
                points += mode.calculateScore()
                cls()
                print("That was correct. You have " + str(points) + " points")
            else:
                print("That was incorrect. You finished with " + str(points) + " points")
                print("The correct sequence was " + self.getStringSequence())
                self.storeScore(points)
                playing = False
    
    def resetGameState(self):
        self.sequence = []
        self.numSeq = []

    def parseGuess(self, guess):
        guessedSequence = guess.split(" ")
        for i in range(len(self.sequence)):
            if (Color.toColor(guessedSequence[i]) == self.sequence[i]):
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
            mode = {"1": self.textMode, "2": self.printLeaderBoard}
            toPlay = mode.get(option, False)
            if (toPlay):
                toPlay()
            else:
                print("That was not a valid option. Please choose again.")

    def renderMenu(self, menu):
        length = 40
        i = 0
        print("#" * length)
        for option in menu:
            i += 1
            print("# " + str(i) + ". " + option +
                  " " * (length - 6 - len(option)) + "#")
        print("#" * length)

    def getName(self):
        while len(self.name) == 0 or len(self.name) > 12:
            if(len(self.name) == 0):
                print("You must enter a name.")
            if (len(self.name) > 12):
                print("That name is too long.")
            self.name = input("What is your name? (for the leaderboard)\n> ")

    def storeScore(self, points):
        if (self.name == ""):
            # Only ask for name when necessary
            self.getName()
        try:
            with open(self.scoreFile, "r+") as scores, open("temp.csv", "w+", newline='') as temp:
                writer = csv.writer(temp)
                reader = sorted(csv.reader(scores),key=lambda row: row[1], reverse=True)
                saved = False
                for row in reader:
                    if (row[0] == self.name):
                        if (int(row[1]) < points):
                            row[1] = points
                            print("Your score has been updated in the leaderboard.")
                        else:
                            print(
                                "You already have a higher score in the leaderboard.")
                        saved = True

                if (saved == False):
                    reader.append([self.name, points])
                reader.sort(key=lambda row: int(row[1]),
                            reverse=True)  # Sort at saving, rather than leaderboard as this could be put on a background thread if it becomes cumbersome and users would get more frustrating if the leaderboard took a long time to load, than they would saving.
                writer.writerows(reader)

        except Exception as e:
            print(e)

        os.replace("temp.csv", self.scoreFile)

    def printLeaderBoard(self):
        leaders = []
        with open(self.scoreFile, "r") as scores:
            reader = csv.reader(scores)
            for row in reader:
                leaders.append(row[0] + " "*(12 - len(row[0])) + row[1])
        self.renderMenu(leaders)


simon = SimonSays()
simon.addButton(Color.RED, [0, 1])
simon.addButton(Color.GREEN, [2, 3])
simon.addButton(Color.YELLOW, [4, 5])
simon.addButton(Color.BLUE, [6, 7])

simon.start()
