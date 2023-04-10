# Name:
# Student Number:

# This file is provided to you as a starting point for the "admin.py" program of Project
# of CSI6208 in Semester 1, 2023.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json
import os.path
from typing import List


class Joke:
    _setup = ""
    _punchline = ""
    _sumOfRatings = 0
    _numOfRatings = 0

    def __init__(self, setup, punchline):
        self._setup = setup
        self._punchline = punchline

    def getSetup(self):
        return self._setup

    def getPunchline(self):
        return self._punchline

    def getRating(self):
        if self._numOfRatings == 0:
            return 0
        else:
            return self._sumOfRatings / self._numOfRatings

    def getNumOfRatings(self):
        return self._numOfRatings

    def rate(self, rating):
        self._sumOfRatings += rating
        self._numOfRatings += 1

    def toJSON(self):
        return json.dumps({
            "setup": self._setup,
            "punchline": self._punchline,
            "sumOfRatings": self._sumOfRatings,
            "numOfRatings": self._numOfRatings
        }, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    @staticmethod
    def fromJSON(json):
        joke = Joke(json["setup"], json["punchline"])
        joke._sumOfRatings = json["sumOfRatings"]
        joke._numOfRatings = json["numOfRatings"]
        return joke


# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
# CSI6208 Requirement: Also enforce a minimum value of 1.  See assignment brief.
def inputInt(prompt):
    valid = False
    while not valid:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Invalid number. Must be greater than 0.")
                continue
            valid = True
        except ValueError:
            print("Invalid number.")
    return value


# This function repeatedly prompts for input until something (not whitespace) is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def inputSomething(prompt):
    valid = False
    while not valid:
        value = input(prompt)
        if value.strip() != "":
            valid = True
    return value


# This function opens "data.txt" in write mode and writes dataList to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def saveChanges(dataList):
    file = open("data.txt", "w")
    jsonList = []
    for joke in dataList:
        jsonList.append(joke.toJSON())
    file.write(json.dumps(jsonList))
    file.close()

# initial check to see if file exists, if not create it and write an empty list to it


def checkFile():
    exists = os.path.isfile("data.txt")
    if not exists:
        data = open("data.txt", "w")
        data.write("[]")
        data.close()


def loadFile():
    data = open("data.txt", "r")
    text = data.read()
    if text == "":
        return []
    jokes = []
    for joke in json.loads(text):
        jokes.append(Joke.fromJSON(json.loads(joke)))

    return jokes


# Here is where you attempt to open data.txt and read the data / create an empty list if the file does not exist.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Joke Bot Admin Program.')

checkFile()
data: List[Joke] = loadFile()

while True:
    print('Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete, [t]op or [q]uit.')
    # Prompt for input and convert it to lowercase.
    choice = input('> ').lower()
    optionalSelection = None

    if (len(choice) > 1):
        choices = choice.split(" ")
        choice = choices[0]
        if (choice != 'v' and choice != 'd' and choice != 's'):
            print("Invalid input.")
            continue
        try:
            optionalSelection = choices[1]
        except ValueError:
            print("Invalid input.")
            continue

    if choice == 'a':
        # Add a new joke.
        joke = Joke(inputSomething("Enter the joke setup: "),
                    inputSomething("Enter the joke punchline: "))
        data.append(joke)
        saveChanges(data)
    elif choice == 'l':
        # List the current jokes.
        print("List of jokes:")
        if len(data) == 0:
            print("No jokes saved.")
            continue

        for index, joke in enumerate(data):
            li = str(index+1)+") "+joke.getSetup()
            print(li)
    elif choice == 's':
        # Search the current jokes.
        if len(data) == 0:
            print("No jokes saved.")
            continue

        search = optionalSelection if optionalSelection != None else inputSomething(
            "Enter search term: ")
        print("Search results:")

        for index, joke in enumerate(data):
            if search in joke.getSetup() or search in joke.getPunchline():
                li = str(index+1)+") "+joke.getSetup()
                print(li)
    elif choice == 'v':
        # View a joke.
        if len(data) == 0:
            print("No jokes saved.")
            continue

        viewSuccess = False
        while not viewSuccess:
            index = int(optionalSelection) if optionalSelection != None else inputInt(
                "Joke number to view: ")
            try:
                index -= 1
                joke = data[index]
                print(joke.getSetup())
                print(joke.getPunchline())

                if (joke.getNumOfRatings() != 0):
                    print("Rated " + str(joke.getNumOfRatings()) +
                          " time(s). Average rating is " + str(joke.getRating()) + "/5.")
                else:
                    print("This joke has not been rated.")

                viewSuccess = True
            except IndexError:
                optionalSelection = None
                print("Invalid index number.")
    elif choice == 'd':
        # Delete a joke.
        if len(data) == 0:
            print("No jokes saved.")
            continue

        deleteSuccess = False
        while not deleteSuccess:
            index = int(optionalSelection) if optionalSelection != None else inputInt(
                "Joke number to delete: ")
            try:
                index -= 1
                del data[index]
                saveChanges(data)
                deleteSuccess = True
                print("Joke deleted.")
            except IndexError:
                optionalSelection = None
                print("Invalid index number.")
    elif choice == 't':
        # return list of jokes that have more than 4 ratings
        if len(data) == 0:
            print("No jokes saved.")
            continue

        for index, joke in enumerate(data):
            if joke.getRating() > 4:
                li = str(index+1)+") "+joke.getSetup()
                print(li)

    elif choice == 'q':
        # Quit the program.
        print('Goodbye!')
        break
    else:
        # Print "invalid choice" message.
        print("Invalid choice.")
