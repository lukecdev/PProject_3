# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words

USER_NAME = ""

def Welcome_game():
    """
    Start function with game instructions 
    """
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
    print("Game Title")
    print("Game Difficulty \n")
    print("Press" + "1" + "For topic 1")
    print(f"2 Game Instructions.")
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
            break
    
def play_game():
    print("Welcome to Guess the word")
    print("FFFF")

def end_game():
        Exception

def main():
    """
    Function to run the game from the beginning
    """
    Welcome_game()
    #play_game()

main()