
from typing import List
import json

jsonData = [
    {
      "numOfRatings": 10,
      "punchline": "Why did the tomato turn red? Because it saw the salad dressing!",
      "setup": "What did one tomato say to the other?",
      "sumOfRatings": 45
    },
    {
      "numOfRatings": 5,
      "punchline": "What do you call a fake noodle? An impasta!",
      "setup": "Did you hear about the Italian chef that died?",
      "sumOfRatings": 20
    },
    {
      "numOfRatings": 12,
      "punchline": "Why was the math book sad? Because it had too many problems.",
      "setup": "Did you hear about the kidnapping at the playground?",
      "sumOfRatings": 65
    },
    {
      "numOfRatings": 3,
      "punchline": "What do you call a bear with no teeth? A gummy bear!",
      "setup": "Why did the cookie go to the doctor?",
      "sumOfRatings": 15
    },
    {
      "numOfRatings": 8,
      "punchline": "Why don’t skeletons fight each other? They don’t have the guts!",
      "setup": "Why did the scarecrow win an award?",
      "sumOfRatings": 30
    },
    {
      "numOfRatings": 7,
      "punchline": "I'm reading a book on the history of glue - I just can't seem to put it down.",
      "setup": "Did you hear about the guy who invented Lifesavers?",
      "sumOfRatings": 25
    },
    {
      "numOfRatings": 2,
      "punchline": "Why was the belt sent to jail? For holding up pants.",
      "setup": "What do you call a belt made of watches?",
      "sumOfRatings": 10
    },
    {
      "numOfRatings": 11,
      "punchline": "Why don’t scientists trust atoms? Because they make up everything!",
      "setup": "What did the grape say when it got stepped on?",
      "sumOfRatings": 50
    },
    {
      "numOfRatings": 6,
      "punchline": "Why did the coffee file a police report? It got mugged.",
      "setup": "How does a rabbi make coffee?",
      "sumOfRatings": 22
    },
    {
      "numOfRatings": 13,
      "punchline": "Why did the chicken cross the playground? To get to the other slide!",
      "setup": "Why did the tomato turn red?",
      "sumOfRatings": 68
    },
    {
      "numOfRatings": 9,
      "punchline": "I told my wife she was drawing her eyebrows too high. She looked surprised.",
      "setup": "I’m on a whiskey diet. I’ve lost three days already.",
      "sumOfRatings": 40
    },
    
    ]
    


def saveChanges():
    file = open("data_test.txt", "w")
    dump_data = []
    for joke in jsonData:
        dump_data.append(json.dumps({
            "setup": joke["setup"],
            "punchline": joke["punchline"],
            "sumOfRatings": joke["sumOfRatings"],
            "numOfRatings": joke["numOfRatings"]
        }, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
    file.write(json.dumps(dump_data))
    file.close()


saveChanges()