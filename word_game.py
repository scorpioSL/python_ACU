# Name:
# Student Number:

# This file is provided to you as a starting point for the "word_game.py" program of Assignment
# of CSI6208 in Semester 1, 2023.  It mainly provides you with a suitable list of words.
# Please use this file as the basis for your assignment work.  You are not required to reference it.


# This function receives two words as parameters should return the number of matching letters between them.
# See the assignment brief for details of this function's requirements.
import random


def compareWords(word1, word2):
    return sum(1 for a, b in zip(word1, word2) if a == b)


# Import the random module to allow us to select the word list and password at random.


# Create a list of 100 words that are similar enough to work well for this game.
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER',
                  'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']


# The rest is up to you...
# See the assignment brief for details of the program requirements.
# Select 8 random words from the candidate list
tempWordList = random.sample(candidateWords, 8)
wordList = []

for(i, word) in enumerate(tempWordList):
    item = {"word": word, "matchCount": 0}
    wordList.append(item)

# Select a random word from the list to be the password
password = random.choice(wordList).get("word")

# Initialize the game variables
won = False
guessesRemaining = 4

# Welcome the user to the game
print("Welcome to the Guess-The-Word Game.")
print("Password is one of these words:\n")

# Start the game loop
while guessesRemaining > 0 and not won:
    # Print the word list and the number of guesses remaining
    for i, word in enumerate(wordList):
        if word.get("matchCount") > 0:
            print(f"{i+1}: {word.get('word')} [{word.get('matchCount')}/{len(word.get('word'))} correct]")
        else:
            print(f"{i+1}: {word.get('word')}")
    print(f"\nGuesses Remaining: {guessesRemaining}\n")

    # Prompt the user to choose a word by entering its index number
    guessNum = int(input("Guess (enter 1-7): "))
    guessesRemaining -= 1

    # Check if the guess is correct
    guess = wordList[(guessNum-1)]
    print(f"{guess.get('word')}")
    if guess.get("word") == password:
        print("\nPassword correct.")
        print("\nCongratulations, You win!")
        won = True
    else:
        print("\nPassword incorrect.")
        print(
                f"{compareWords(guess.get('word'), password)}/{len(word.get('word'))} correct.\n")
        # Compare the guess and the password to determine the number of matching letters
        guess["matchCount"] = compareWords(guess.get('word'), password)
