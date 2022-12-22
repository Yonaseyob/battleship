# Battleship Game
Battleship Game is a python game,which runs in the code inistitute mock terminal on Heroku.
The user can play by guessing the row and column of the hidden battleship on the playboard.

![Capture](https://user-images.githubusercontent.com/112119971/209225076-db1893ea-c768-4482-bf2e-04444dd3ca45.JPG)

## How to play
The game is played by the user entering a column and row number (coordinates) of the location they suspect a battleship is laid. If that location is on a battleship, it is a hit and marked as "x", If the location is not on a battleship, it is a miss and marked as "-".
## Features
### Existing Features
* Random board generation
  - Ships are placed randomly on the board.
  - The player can not see the location of the ship.
 
 ![Capture3](https://user-images.githubusercontent.com/112119971/209230465-3317cb92-2f37-410b-b50b-9c1d49f16142.JPG)

* Accepts user input
* Input validation and error-cheking

![Capture2](https://user-images.githubusercontent.com/112119971/209229597-805d6c6d-fa93-4b9a-8ac4-656e7a8b3d61.JPG)

### Testing
I have manually tested by giving invalid input: strings while expecting a number input, out-of-bounds input, same input twice
### Bugs
No bugs found.
### Validation Testing
* PEP8
I could not validate on PEP8, because I can't find it online instead I tried to validate on other online python code checkers, and I got different feedback.
## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

The steps for deployment are as follows:

* Fork or clone this repository
* Create a new Heroku app
* Set the buildpacks to Python and NodeJS in that order
* Link the Heroku app to the repository
* Click on Deploy
## Credits
* The idea of using battleships is a suggested by the Code Institute with "Ultimate Battleships" as inspiration.
* To solve the problems that I encountered in building this game I used several youtube and google search results.
