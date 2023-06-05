# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words, cats 
import os

USER_NAME = ""

def clear():
    """
    Function to clear terminal for a better user experience.
    """
    os.system("cls" if os.name == "nt" else "clear")

def Welcome_game():
    """
    Start function with game instructions 
    """
    print("welcome")
    global USER_NAME
    while True:
        
        USER_NAME = input("Please  enter your name:\n")
        if USER_NAME == "y": 
            print("Username is: " + USER_NAME)
            game_start()
        else:
            print("please try again")  
            end_game()
        
        #except ValueError:
           # clear()
            #print("Name must be longer than 2 characters")

        #if (len(USER_NAME) >= 2 and len(USER_NAME) <= 8 and USER_NAME.count("") <= 0):
            
        #else:
           # clear()
           # print(Welcome)        
def game_start():
    print("Please select 1, 2, 3 or 4 from the Main Menu below.\n")
    print("""
1 - topic words
2 - game rules
3 - topic cats
4 - quit
    \n""")

    print("What is your choice?")
    #print("Game Difficulty \n")
    #print("Press" "1" "For topic 1")
    #print(f"2 Game Instructions.")
    #print("Press" + "2" + "For topic 2")
    #print("Press" + "3" + "For topic 3")
    topic = False
    while not topic:
        select = input("\n")
        if select == "1":
            topic = True
            play_game()
            
        elif select == "2":
            topic = True
            print("topic2")
            play_game()
                

        elif select == "3":
            topic = True
            play_cats()  

        else:
            print(" Please select 1, 2 or 3 only to continue")
            end_game()

def get_random_word():
    """
    Get random words for game from list
    """   
    global word
    word = random.choice(words) 

    return word.lower()

def get_cat_word():
    """
    gets random word from cats word list
    """   
    global word
    word = random.choice(cats)

    return word.lower()

def play_again():
    """
    A loop to repeat the game if the user wants to
    """
    global play_loop
    play_loop = input("Do you want to play again? y or n?")
    while play_loop not in ("y", "n"):
        play_loop = input("Do you want to play again? y or n?")
    if play_loop == "y":
        print("you entered Y")
        clear()
        Welcome_game()
    if play_loop == "n":
        print("you entered N")
        exit()
    else:
        print("try again")        

def play_cats():
    """
    Running game with cats words list
    """
    word = get_cat_word()
    num_lives = 5
    guesses = []
    finish = False

    while not finish:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")   
        print("")

        guess = input(f"lives left{num_lives}, Next letter: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            num_lives -= 1
            if num_lives == 0:
                break
        
        finish = True
        for letter in word:
            if letter.lower() not in guesses:
                finish = False  
        if finish:
            print(f"congrats you guessed {word} correct!")  
        else:
            print(f"You ran out of lives, the correct word was {word}")    
                             
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
    finish = False
    
    while not finish:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")   
        print("")

        guess = input(f"lives left{num_lives}, Next letter: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            num_lives -= 1
            if num_lives == 0:
                break
        
        finish = True
        for letter in word:
            if letter.lower() not in guesses:
                finish = False  
        if finish:
            print(f"congrats you guessed {word} correct!")  
        else:
            print(f"You ran out of lives, the correct word was {word}")    
                             
    return play_again()   

def end_game():
        print("Thank you")
        play_again()

def main():
    """
    Function to run the game from the beginning
    """
    Welcome_game()
    play_game()
 
print("Welcome to Guess the word")
main()