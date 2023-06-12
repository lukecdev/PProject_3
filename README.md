
Guess Word is a Python terminal game, which runs on the Code Institute mock terminal on Heroku. Users can try guess the word by inputting letters until they get the correct word or run out of lives. The user can view the game instructions and choose the game difficulty.

Git Repository can be found here: https://github.com/lukecdev/word-guess
live Deployed site: https://word-guess.herokuapp.com/

![Mockup](/views/images/mockup-python.jpg)


---
## CONTENTS

* [UX](#ux)
  * [Strategy](#strategy)
    * [Scope](#scope)
    * [User Stories](#user-stories)

* [Design](#design)
  * [Colour](#colour)
  * [FlowChart](#flow-chart)

* [Features](#features)
  * [Future Implementations](#future-features)

* [Technologies Used](#technologies-used)

* [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)

---

## UX
### Strategy
The objective of the site is for users to test their word guessing ablity. 
#### Scope
- Ask the user for their user name.
- Ask the user to chose to enter game or read game instructions.
- Offer the user 2 levels of game difficulty - Easy or Expert.
- Allow the user to guess the word in the given lives.

#### User Stories
I want a game that is simple to play from the start.
I want the game to provide a challenge for differnt users.
I want instructions for the game to be simple to understand.


## Design

- As this game is devloped in a Python terminal. There is not many design options. Readability and usablity are most important. 
### Colour

- To add some colour to the text in the terminal by intalling Colorama in Python. This allows for the Green and Yellow colurs to the text.

### Flow Chart

During the planning process a flow chart was created to show the basic steps needed to play the game. This was used to develop the logic steps of the game.

![FlowChart](/views/images/flowchart.jpg)


## Features

1. Welcome Screen 
    - This is the first screen when the program runs. It asks for the user to enter a name to continue.

    ![Welcome Screen](/views/images/welcome-screen.jpg)
2. Main Menu
    - After a name is entered, the options of playing the game or read game rules are displayed.

    ![Main Menu](/views/images/main-menu.jpg)

3. Select Level     
    - The game displays the user with two difficulty levels for the game. Selecting a level affects how many lives the user gets to guess the secret word.
    - Easy level gives the user 10 lives.
    - Expert level gives the user 5 lives.

    ![Level](/views/images/level.jpg)

4. Game Mode
    - This section displays the blank spaces of the word to guess. The user is asked to guess a letter. If correct it will show in the space. If incorrect you user will lose a life.

    ![Game Mode](/views/images/rules.jpg)

5. Game Rules     
    - This section displays the instructions of how the game to the user.

    ![Rules](/views/images/welcome-screen.jpg)

### Future Features

- Word topics. Adding a section to select what topic of words to guess.
- Graphics would help improve the appeal of the game.
- The ability for the user to enter the full word if they know it. 

## Technologies Used
1. Python - All code was written in Python language
2. Github - For code repository and code version control.
3. Heroku - To deploy the live application.
4. Gitpod - Cload based code editor used.
5. LucidCharts - Used for flow chart creation.
6. Colored - Was used to add color to terminal text.

## Deployment

The project was deployed using Code Institutes mock terminal for Heroku.
The steps taken were:

In [heroku](https://dashboard.heroku.com/apps): 
    
  1. Open the "new" menu and click on "Create new app".
  2. Fill form fields with app name and region (Europe). Click on "Create app".
  3. In the "Settings" section, click on "Add buildpack" and add Python and NodeJS, *in that order*.
  4. In "Deployment method", select the GitHub option and provide the repository details. Click on "Connect".
  5. Click on "Enable Automatic Deploys" and finally, click on "Deploy Branch".

#### Forking the repository
1. Log into the Github repository.
2. Underneath your avatar is a button labelled **Fork**, click this.
3. You should have your own copy now..

#### Cloning the repository
1. Log into Github and locate the repository.
2. Under the repository name click the button labelled - code.
3. You will see an option to clone or download.
4. Copy the url for cloning by clicking the clipboard icon.
5. Launch Codeanywhere or your own choice of directory.
6. Change the current working directory to the location you want the cloned directory to be.
7. Type git clone and paste the Url from step 4. 
8. Press enter to create the cloned directory.

## Testing

### Code Validating
- Code was validated using [CI Python Linter](https://pep8ci.herokuapp.com/#)

- ![Code Validator](/views/images/code-test-new.jpg)

### Bugs
- Bugs where encountered while coding the project. Most where solved during the process through continuious testing of the code. Using print statments on the code editor terminal, I was able to quickly test sections and find bugs. When a function was finalilzed it was run though the code validator. 

  - One of the ongoing bugs that I was unable to fix in time was the syntax error in line 25 and 224, the code validator was suggesting to add a "if" and "is" to the true satatment, but this caused the final program not run. So the decision wass made to leave these bugs in place as the game currenlty runs to my desired result with them.

## Credits

- I used watched this ![Youtube Video](https://www.youtube.com/watch?v=5x6iAKdJB6U) which helped me build the random word selector and  
  word guessing structure of the game. I got inspiration from this video on how to structure the functions.

###  Acknowledgments

- A huge thanks to [Chris Quinn](https://github.com/10xOXR) for his help, suggestions and patiece while I put together this project. 

- A huge thanks to [Jubril Akolade](https://github.com/Jubrillionaire) for his help in last minute issues I had with my prject. 
