# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words 
import os
import colorama # Adds color to text
from colorama import Fore, Style

USER_NAME = ""

def clear():
    """
    Function to clear terminal for a better user experience.
    """
    os.system("cls" if os.name == "nt" else "clear")

def welcome_game():
    """
    Start function with game instructions 
    """
    print(f"\n{Fore.GREEN}WELCOME TO GUESS THE WORD!\n")
    global USER_NAME
    while True:
        USER_NAME = input(f"{Fore.WHITE}Please enter your name:\n")
        if (USER_NAME.isalpha() == True and len(USER_NAME) >=2):
            print("Hello " + USER_NAME + "!\n")
            game_start()
        else:
            print("User name must be greater than 2 and only letters.")  
            welcome_game()
    
def game_start():
    print("Please select 1, 2 or 3 from the Main Menu below.\n")
    print("""
1 - Enter Game
2 - Game Instructions
3 - Exit Game
    \n""")

    topic = False
    while not topic:
        select = input("What is your choice?")
        if select == "1":
            topic = True
            select_level()
            
        elif select == "2":
            topic = True
            instructions()
        
        elif select == "3":
            topic = True
            clear()
            exit()  

        else:
            print("Please select 1, 2 or 3 only to continue")
            game_start()

def instructions():
    """
    Shows the instructions of the game.
    """
    print(f"{Fore.YELLOW}Game Instructions:"
         f"{Fore.WHITE}") 
    print("""
Enter the game and choose ypur difficulty.
Easy difficulty gives the user 10 lives.
Expert difficulty gives the user 5 lives.  
Enter a letter from A to Z only.
The game will display how many charaters are in the word to be guessed.
If the letter is correct it will show in the above word.
If the letter is not correct, you will loose a live. 
If you reach 0 lives, the game is over.
    """)
    print(f"{Fore.YELLOW}Best of Luck!"
         f"{Fore.WHITE}")
    input("Press Enter to return to main menu!")
    game_start()

def get_random_word():
    """
    Get random words for game from list
    """   
    global word
    word = random.choice(words) 

    return word.lower()

def select_level():
    """
    Lets the player chose the game difficulty 
    which affects the amount of lives they get.
    """
    print("Select Level Below:")
    print("""
1 - Normal
2 - Expert
3 - Main Menu
    \n""")

    level = False
    while not level:
        select = input("Your choice:")
        if select == "1":
            level = True
            play_easy()
            
        elif select == "2":
            level = True
            play_game()

        elif select == "3":
            level = True
            game_start()

        else:
            print("Please select 1, 2 or 3 only to continue")
            select_level()

def play_again():
    """
    A loop to repeat the game if the user wants to
    """
    global play_loop
    play_loop = input("Do you want to play again? (Y/N)")
    while play_loop not in ("y", "n"):
        play_loop = input("Do you want to play again? (Y/N)")
    if play_loop == "y":
        clear()
        game_start()
    if play_loop == "n":
        clear()
        print(f"Thank you for playing {USER_NAME}!\n")
        welcome_game()
    else:
        print("Please press Y or N only!")        

def play_easy():
    """
    Runs the game 
    Game is based around the Hang-Man game from the youtube video
    https://www.youtube.com/watch?v=5x6iAKdJB6U 
    """

    word = get_random_word()
    num_lives = 10
    guesses = []
    wrong_letters = []

    finish = False
    print(f"The {len(word)} word is:")

    while not finish:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print(" _ ", end= "")   
        print(" ")

        guess = input(f"{USER_NAME}'s lives left {num_lives}, Next letter: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            num_lives -= 1
            print(f"letters guessed: {guesses}")
             
        finish = True
        for letter in word:
            if letter.lower() not in guesses:
                finish = False  
        if finish == True:
            print(f"congrats {USER_NAME} you guessed {word} correct!")  
        elif num_lives == 0:
            print(f"You ran out of lives {USER_NAME}, the correct word was {word}")
            break    
                             
    return play_again()   

def play_game():
    """
    Runs the game 
    Game is based around the Hang-Man game from the youtube video
    https://www.youtube.com/watch?v=5x6iAKdJB6U 
    """

    word = get_random_word()
    num_lives = 5
    guesses = []
    wrong_letters = []

    finish = False
    print(f"The {len(word)} word is:")

    while not finish:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print(" _ ", end= "")   
        print(" ")

        guess = input(f"{USER_NAME}'s lives left {num_lives}, Next letter: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            num_lives -= 1
            print(f"letters guessed: {guesses}")
             
        finish = True
        for letter in word:
            if letter.lower() not in guesses:
                finish = False  
        if finish == True:
            print(f"Congrats {USER_NAME} you guessed {Fore.GREEN}{word.upper()} correct!"
                 f"{Fore.WHITE}")  
        elif num_lives == 0:
            print(f"You ran out of lives {USER_NAME}, the correct word was {Fore.GREEN}{word.upper()}!"
                 f"{Fore.WHITE}")
            break    
                             
    return play_again()   

def main():
    """
    Function to run the game from the beginning
    """
    welcome_game()
    play_game()

main()