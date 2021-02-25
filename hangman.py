#! /usr/bin/python3
# hangman.py - My version of the Hangman game with English words
# in the command line
import random, time, sys

# Game's main function with a loop
def game(word):
    '''Game function with a while loop that repeats
    until score hits 0 or word is found'''
    userWordGuess = len(word)*'_'
    userCharGuess = ''
    score = 10

    while userWordGuess != word and score > 0:
        print("This is your current score:", score)
        print("Your current guess:", userWordGuess)
        userCharGuess = input("Guess a letter: ")

        if userCharGuess == '':
            print("You haven't entered a letter!\n")

        elif len(userCharGuess) > 1:
            print("Please write only one letter.\n")

        elif userCharGuess.upper() not in word:
            print("This letter isn't in the word to guess, too bad! You just lost a point!\n")
            score -= 1

        else:
            print("Good guess!\n")
            indices = [i for i, e in enumerate(word) if e == userCharGuess.upper()]
            t = list(userWordGuess)
            for n in range(len(indices)):
                index = indices[n]
                t[index] = userCharGuess.upper()
            userWordGuess = ''.join(t)

    if (userWordGuess == word):
        print("Awesome! You found the word:", word)
        print("You have a score of:", score)
    else:
        print("Too bad! The word to guess was:", word)
        print("Better luck next time!")

# Game initialization that chooses a random word from a list in a file
def initGame():
    # Open the file that contains the words and shuffle the word array
    f = open('list.txt')
    words = f.readlines()
    f.close()

    # Shuffle the word array 10 times
    for i in range(10):
        random.shuffle(words)

    # Select a random word
    n = random.randint(0, len(words))
    word = words[n][0:-1].upper()

    return word


c1 = "Welcome to the Hangman game"
print(c1)
print('-' * len(c1))
rn = 0
while rn == 0:
    c2 = """\nWhat do you want to do?
    1. Play
    2. Add words to the dictionary
    3. Quit game"""
    print(c2)
    choice = input("Enter your choice [1/2/3]: ")

    if choice.isnumeric():
        if int(choice) == 1:
            print(40*'-'+"\nLet's start the game! Please wait.")
            time.sleep(0.5)
            for i in range(5):
                s1 = "Choosing a word" + i * "."
                sys.stdout.write("\r" + (s1))
                sys.stdout.flush()
                time.sleep(0.25)
            word = initGame()
            print("\nOkay let's start! There are %d letters in the word to guess.\n" % len(word))
            game(word)

        elif int(choice) == 2:
            pass

        elif int(choice) == 3:
            print("\nSee you next time!!")
            rn = 1
    else:
        print("\nI didn't understand your choice.")
