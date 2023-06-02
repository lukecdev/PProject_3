# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words

def game_start():
    """
    Start function with game instructions 
    """
    print("Game Title")
    print("Game Difficulty \n")
    print("Press" + "1" + "For topic 1")
    print("Press" + "2" + "For topic 2")
    print("Press" + "3" + "For topic 3")
    topic = False
    while not topic:
        select = input("\n")
        if select == "1":
            topic = True
            
            return play_game()
        
        elif select == "2":
            topic = True
            print("topic2")
            

        elif select == "3":
            topic = True
            break    

        else:
            print(" Please select 1, 2 or 3 only to continue")
    
def play_game():
    print("Welcome to Guess the word")
    print("FFFF")

def main():
    """
    Function to run the game from the beginning
    """
    game_start()
    #play_game()

main()