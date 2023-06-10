![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,



Guess Word is a Python terminal game, which runs on the Code Institute mock terminal on Heroku. Users can try guess the word by inputting letters until they get the correct word or run out of lives. The user can view the game instructions and choose the game difficulty.

Git Repository can be found here: 
live Deployed site: https://word-guess.herokuapp.com/


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

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

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

During the planning process a flow chart was created to show the basic steps needed to play the game.


## Features

1. Welcome Screen 
    - This is the first screen when the program runs. It asks for the user to enter a name to continue.

2. Main Menu
    - After a name is entered, the options of playing the game or read game rules are displayed.

3. Select Level    
    - 

### Future Features

- Word topics. Adding a section to select what topic of words to guess.
- Graphics would help improve the appeal of the game.

## Technologies Used
1. Python - All code was written in Python language
2. Github - For code repository and code version control.
3. Heroku - To deploy the live application.
4. Gitpod - Cload based code editor used.
5. LucidCharts - Used for flow chart creation.

## Deployment & Local Development

👩🏻‍💻 View an example of a completed Deployment & Local Development section [here](https://github.com/kera-cudmore/TheQuizArms#Deployment)

### Deployment

Include instructions here on how to deploy your project. For your first project you will most likely be using GitHub Pages.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

Place instructions on how to fork your project here.

#### How to Clone

Place instructions on how to clone your project here.

## Testing

Start as you mean to go on - and get used to writing a TESTING.md file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a TESTING.md file from your first project you will thank yourself later when completing your later projects, which will contain much more information.
  
Use this part of the README to link to your TESTING.md file - you can view the example TESTING.md file [here](milestone1-testing.md)

## Credits

👩🏻‍💻 View an example of a completed Credits section [here](https://github.com/kera-cudmore/BookWorm#Credits)

The Credits section is where you can credit all the people and sources you used throughout your project.

### Code Used

If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

### Content

Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

###  Media

If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.
  
###  Acknowledgments

If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
