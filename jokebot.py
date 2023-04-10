# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "jokebot.py" program of Assignment 2
# of CSI6208 in Semester 1, 2023.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.


# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
from typing import List
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import json

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
            return round((self._sumOfRatings / self._numOfRatings),1)

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


class ProgramGUI:
    data: List[Joke] = []
    currentJoke: int = 0
    window: tk.Tk = None
    users_rating:tk.StringVar
    main_frame:tk.Frame = None


    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data file and creating the user interface.
        # See Points 1 to 4 "Requirements of jokebot.py" section of the assignment brief. 
        # Create a new window
        self.window = tk.Tk()
        # Create a frame
        self.main_frame = tk.Frame(self.window, width=1200, height=800)
        # Set the window title
        self.window.title("Joke Bot")
        self.window.geometry("1200x800")
        # create a custom style for the window title
        style = ttk.Style()
        style.configure("Title.TLabel", foreground="black", font=("TkDefaultFont", 12, "bold"), anchor="w")
        self.data = self.loadData()
        self.showJoke()


    def showJoke(self):
        joke:Joke = self.data[self.currentJoke]
        if joke != None:
            # create a font for the top label
            font = ("Arial", 24, "bold")
            top_label = tk.Label(self.main_frame, text=joke.getSetup(), font=font)
            top_label.grid(row=0,column=1,columnspan=3)

            # create a font for the bottom label
            font = ("Arial", 18, "bold", "italic")
            bottom_label = tk.Label(self.main_frame, text=joke.getPunchline(), font=font)
            bottom_label.grid(row=1,column=1,columnspan=3)

            # create a font for the rating label
            font = ("Arial", 14)
            rating_label = tk.Label(self.main_frame, text= "Joke has not been rated!" if joke.getNumOfRatings() == 0 else "Rated: " + str(joke.getNumOfRatings()) + " time(s). Average rating is " + str(joke.getRating()) + "/5.", font=font)
            rating_label.grid(row=2,column=1,columnspan=3)

            # create a font for the buttons
            font = ("Arial", 14)
            self.users_rating = tk.StringVar()

            # Create the label and entry widgets
            users_rating_label = tk.Label(self.main_frame, text="Your Rating: ", font=font)
            users_rating_label.grid(row=3,column=0,sticky="ew")
            users_rating_entry = tk.Entry(self.main_frame, textvariable=self.users_rating, width=2)
            users_rating_entry.grid(row=3,column=1,sticky="ew")
            users_rating_entry.focus()

            # Create the submit button
            rate_button = tk.Button(self.main_frame, text="Submit", font=font, command=lambda: self.rateJoke())
            rate_button.grid(row=3,column=2,sticky="ew")


            self.main_frame.grid_columnconfigure((0, 4), weight=1)

            # Pack the main frame
            self.main_frame.pack(anchor="center", expand=True)


    
        # Display the window
        self.window.mainloop()

    def rateJoke(self):
        joke:Joke = self.data[self.currentJoke]
        if joke != None:
            try:
                rating = int(self.users_rating.get())
                if rating < 1 or rating > 5:
                    messagebox.showerror("Error", "Invalid rating. Enter an integer between 1 and 5.")
                    return

                joke.rate(rating)
                self.saveChanges(self.data)
                self.currentJoke += 1
                # check if we have reached the end of the list
                if self.currentJoke >= len(self.data):
                    messagebox.showinfo("Success", "That was the last joke. The program will now end.")
                    self.window.destroy()
                    return
                
                messagebox.showinfo("Success", "Thank you for rating. The next joke will now appear.")
                self.clearFrame()
                self.showJoke()
            except ValueError:
                messagebox.showerror("Error", "Invalid rating. Enter an integer between 1 and 5.")

    def clearFrame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def loadData(self):
        try:
            data = open("data.txt", "r")
            text = data.read()
            if text == "":
                return []
            jokes = []
            for joke in json.loads(text):
                jokes.append(Joke.fromJSON(json.loads(joke)))
            return jokes
        except FileNotFoundError:
            messagebox.showerror("Error", "Missing/Invalid file")
            self.window.destroy()
            return
        
    def saveChanges(self,dataList: List[Joke]):
        file = open("data.txt", "w")
        jsonList = []
        for joke in dataList:
            jsonList.append(joke.toJSON())
        file.write(json.dumps(jsonList))
        file.close()



# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
