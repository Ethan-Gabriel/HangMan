from os import system
import random

def hangman_game():
    
    name = (input("\nWelcome to Hangman! What is your first name? ")).capitalize()
    print()
    print("Hello " + name + ", It is time to play HangMan!")
    print("Each time you select an incorrect letter, your # of turns decreases.")
   
    while True:
        print("Choose a Cateogry: Movies (1), Company Names (2), School Suplies (3), Artist Names (4)")
        category = int(input("Choice (1, 2, 3 or 4): "))

        if category == 1:
            words = [
                "Forrest Gump",
                "Hangman Project",
                "The Godfather",
                "The Green Mile",
                "Hotel Rwanda",
                "Goodfellas",
                "Scarface",
                "The Terminal",
                "Million Dollar Baby",
                "Driving Miss Daisy",
                "Catch Me If You Can",
                "Chinatown",
                "The Departed",
                "Dances with Wolves",
                "Ford v Ferrari",
                "Little Women",
                "A Star Is Born",
                "Dear Basketball"
            ] 
            print("You chose the movies cateogry! Start Guessing...\n")
            break
        elif category == 2:
            words = [
                "Apple Inc",
                "Samsung Technologies",
                "Texas Instruments",
                "Louis Vuitton",
                "British Airways",
                "American Express",
                "The North Face",
                "Tommy Hilfiger",
                "Polo Ralph Lauren",
                "American Eagle Outfitters",
            ] 
            print("You chose the company names cateogry! Start Guessing...\n")
            break
        elif category == 3:
            words = [
                "Penicl",
                "Eraser",
                "Sharpener",
                "Calculator",
                "Binder",
                "Duotang",
                "Phone Charger",
                "Laptop",
                "Graph Paper",
                "Lined Paper",
            ] 
            print("You chose the school supplies cateogry! Start Guessing...\n")
            break
        elif category == 4:
            words = [
                "Ariana Grande",
                "Michael Jackson",
                "Freddie Mercury",
                "Taylor Swift",
                "Lady Gaga",
                "Selena Gomez",
                "Justin Bieber",
                "Elvis Presley",
                "Jennifer Lopez",
                "Ed Sheeran",
            ] 
            print("You chose the artist names cateogry! Start Guessing...\n")
            break
        else:
            print("Invalid choice! Try again...")
            continue
    
    guessed_word = []
    guesses = ""
    turns = 10

    word = (random.choice(words)).upper()

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=" ")
            elif char == " ":
                print(' / ', end=" ") 
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\n" + name + ", you WON! :)")
            break

        guess = (input("\nGuess a Character: ")).upper()

        if len(guess) > 1:
            break

        guesses += guess
        if (guess not in word) and (guess not in guessed_word):
            turns -= 1
            guessed_word.append(guess)
            print("\nWrong Guess!")

        print("\nYou have ", turns, "more guesses")
        print("\nWrong Character's Entered : ", guessed_word)

        if turns == 0:
            print("\nGame is OVER, you LOST :o")

    check = (input("\nDo you want to play again Y/N? ")).upper()
    print()

    if check == "Y":
        hangman_game()
    else:
        print("Thank you for playing HangMan!")

hangman_game()