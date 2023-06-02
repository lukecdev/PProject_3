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

    while True:
        select = input("\n")
        break
   
    
def play_game():
    print("Play game")

def main():
    """
    Function to run the game from the beginning
    """
    game_start()
    # play_game()

main()