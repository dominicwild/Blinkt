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
    WHITE = [255,255,255]
    PURPLE = [145,30,180]
    MAROON = [128,0,0]
    ORANGE = [245,130,48]

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
            "yellow": Color.YELLOW,
            "w": Color.WHITE, 
            "white": Color.WHITE,
            "p": Color.PURPLE,
            "purple": Color.PURPLE,
            "m": Color.MAROON,
            "maroon": Color.MAROON,
            "o": Color.ORANGE,
            "orange": Color.ORANGE
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
    numSeq = []
    difficulty = -1
    speed = -1
    name = ""
    scoreFile = "scores.csv"

    def __init__(self):
        self.addButton(Color.RED, [0, 1])
        self.addButton(Color.GREEN, [2, 3])
        self.addButton(Color.YELLOW, [4, 5])
        self.addButton(Color.BLUE, [6, 7])
        self.reset()
        open(self.scoreFile, "a+").close()

    def addButton(self, color, leds):
        self.buttons.append(Button(color, leds))

    def lightButton(self, buttonNum, sleepTime=1):
        button = self.buttons[buttonNum]
        for led in button.leds:
            set_pixel(led, button.color)
        # set_pixel(button.leds[0], button.color)
        # set_pixel(button.leds[1], button.color)
        show()
        time.sleep(sleepTime)
        self.reset()
        print("")

    def display(self):
        show()

    def reset(self):
        clear()

    def getNumberOfButtons(self):
        return len(self.buttons)

    def getButtonColour(self,index):
        return self.buttons[index].color

    def deleteButtons(self):
        self.buttons = []

    def getButtonColours(self):
        colors = []
        for button in self.buttons:
            colors.append(button.color)
        return colors

    def getSpeed(self,options):
        while self.speed < 0:
            self.renderMenu(options)
            print("In this mode you select a speed and the LEDs will stay lit for that duration.")
            try:
                self.speed = int(input("Select a speed\n> "))
                if(self.speed < 0 and self.speed > 5):
                    print("That is not a valid speed, try again. It must be one of the options above.")
            except Exception:
                print("The speed must be a number from the above.")
                self.speed = -1

    def getDifficulty(self):
        while self.difficulty < 0:
            print("In this mode you can create your own custom difficulty.")
            try:
                self.difficulty = int(input("Input a number to create your difficulty. The higher the number, the more lights you will have to remember in each round of the game, however the more points you'll get!\n> "))
                if(self.difficulty < 0):
                    print("That is not a valid difficulty, try again. It must be greater than zero.")
            except Exception:
                print("The difficulty must be a number.")
                self.difficulty = -1

    #Since modes are only simplistic (only modifying points generated per round) no need to separate into classes. Although could be done in future if logic gets more complicated.
    def classicMode(self):
        rand = randint(0, self.getNumberOfButtons() - 1)
        self.sequence.append(self.getButtonColour(rand))
        self.numSeq.append(rand)

        self.displaySequence(self.numSeq)
        return 1
    
    def difficultyMode(self):

        self.getDifficulty()
            
        for i in range(self.difficulty):
            rand = randint(0, self.getNumberOfButtons() - 1)
            self.sequence.append(self.getButtonColour(rand))
            self.numSeq.append(rand)

        self.displaySequence(self.numSeq)
        return self.difficulty*self.difficulty

    def speedRunMode(self):

        options = ["Slowest", "Slow", "Normal", "Fast", "Fastest"]
        speeds = [2,1.5,1,0.5,0.25]
        modifiers = [0.25,0.5,1,2,4]

        self.getSpeed(options)

        modifier =modifiers[self.speed-1]
        duration = speeds[self.speed-1] #Assign actual speed value

        rand = randint(0, self.getNumberOfButtons() - 1)
        self.sequence.append(self.getButtonColour(rand))
        self.numSeq.append(rand)

        self.displaySequence(self.numSeq, duration)

        return modifier

    def multiMode(self):

        if(self.getNumberOfButtons() == 4):
            print("In this mode instead of 4 buttons, there are 8 you must memorise.")
            self.deleteButtons()
            buttons = [[Color.RED, [0]],[Color.GREEN, [1]],[Color.YELLOW, [2]],[Color.BLUE, [3]],[Color.WHITE, [4]],[Color.ORANGE, [5]],[Color.MAROON, [6]],[Color.PURPLE, [7]]]
            for button in buttons:
                self.addButton(button[0], button[1])
        
        colorString = ""
        for color in self.getButtonColours():
            colorString += color.name + " "

        rand = randint(0, self.getNumberOfButtons() - 1)
        self.sequence.append(self.getButtonColour(rand))
        self.numSeq.append(rand)

        self.displaySequence(self.numSeq)
        print("The available colours are: " + colorString) #Print colours in case user forgets or doesn't know what a particular colour may be
        return 1 + 0.5*len(self.numSeq)

    def textMode(self):
        mode = "Invalid option"
        while mode == "Invalid option":
            self.renderMenu(["Classic Mode", "Difficulty Mode", "Speed Run Mode", "Multi Mode"])
            option = input("Which mode do you want to play? (input the number):\n> ")
            modes = {"1" : self.classicMode, "2": self.difficultyMode, "3": self.speedRunMode, "4" : self.multiMode}
            mode = modes.get(option, "Invalid option")
        print("Playing the text version of Simon.")
        print("Write your guesses with spaces separating the colours i.e., 'y b r g' for guessing yellow, blue, red and then green, in that order")
        playing = True
        points = 0
        numSeq = []
        while playing:
            modifier = mode()
            self.reset()
            correct = self.parseGuess(input("What was the sequence of lights?\n> ").strip(" ")) #Trim so that extra spaces don't invalidate user input
            if (correct):
                points += 1*modifier
                cls()
                print("That was correct. You have " + str(points) + " points")
            else:
                print("That was incorrect. You finished with " +
                      str(points) + " points")
                print("The correct sequence was " + self.getStringSequence())
                self.storeScore(points)
                self.resetGameState()
                playing = False
    
    def resetGameState(self):
        self.sequence = []
        self.numSeq = []
        self.difficulty = -1
        self.speed = -1
        if(not self.getNumberOfButtons() == 4):
            self.deleteButtons()
            self.addButton(Color.RED, [0, 1])
            self.addButton(Color.GREEN, [2, 3])
            self.addButton(Color.YELLOW, [4, 5])
            self.addButton(Color.BLUE, [6, 7])

    def parseGuess(self, guess):
        guessedSequence = guess.split(" ")
        
        if(not len(self.sequence) == len(guessedSequence)):
            return False

        for i in range(len(self.sequence)):
            if(Color.toColor(guessedSequence[i]) == self.sequence[i]):
                continue
            else:
                return False
        return True

    def displaySequence(self, numSeq, duration=1):
        for i in numSeq:
            cls()
            self.lightButton(i, duration)
        cls()  # To erase the final light

    def getStringSequence(self):
        stringSeq = ""
        for i in range(len(self.sequence)):
            stringSeq += self.sequence[i].name + " "
        return stringSeq

    def start(self):
        while True:
            self.renderMenu(["Text Based", "View Leaderboard"])
            option = input("Select an option: ")
            mode = {"1": self.textMode, "2": self.printLeaderBoard}
            toPlay = mode.get(option, False)
            if (toPlay):
                toPlay()
            else:
                print("That was not a valid option. Please choose again.")

    def renderMenu(self, menu):
        length = 40
        i = 0
        print("#"*length)
        for option in menu:
            i += 1
            print("# " + str(i) + ". " + option +" "*(length - 5 - len(str(i)) - len(option)) + "#")
        print("#"*length)


    def getName(self):
        while len(self.name) == 0 or len(self.name) > 12:
            if(len(self.name) == 0):
                print("You must enter a name.")
            if (len(self.name) > 12):
                print("That name is too long.")
            self.name = input("What is your name? (for the leaderboard)\n> ")

    def storeScore(self, points):
        if(self.name == ""):
            # Only ask for name when necessary
            self.getName()
        try:
            with open(self.scoreFile, "r+") as scores, open("temp.csv", "w+", newline='') as temp:
                writer = csv.writer(temp)
                reader = sorted(csv.reader(scores), key=lambda row: row[1], reverse=True)
                saved = False
                for row in reader:
                    if(row[0] == self.name):
                        if(round(float(row[1])) < points):
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
        leaders = []
        with open(self.scoreFile, "r") as scores:
            reader = csv.reader(scores)
            i= 0
            negativePadding = 0
            for row in reader:
                i += 1
                if(len(str(i)) ==2 ):
                    negativePadding = -1
                leaders.append(row[0] + " "*(12 - len(row[0]) + negativePadding) + row[1])
                if(i == 10):
                    break
        self.renderMenu(leaders)

simon = SimonSays()

simon.start()
