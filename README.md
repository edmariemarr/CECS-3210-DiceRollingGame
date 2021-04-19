# Rodriguez_132704_project01_DiceRollingGame
Adv. Programming Project

**Game Description:**
This simple rolling dice game is known as a game of probability. The user wins if both dice have the same faces, and loses if they have different faces.

1. **Set the window and the coordinates for the window. The header of the window will read "Dice Rolling Game" and the window will be 300 x 100.**
2. **Draw the squares that serve as the body for the dice using Rectangle.**
    - The first square is at the left of the window and will be colored black.
    - The second square is at the right of the window and will be colored pink.
3. **A text will appear below the dice that will tell the user that, to successfully roll the die, they must click twice for each dice.**
4. **Set the dots for the first and second dice, separately.**
    - We will use Circle to draw the dots that will be on the face of the dice.
    - These dots are: 1.) upper left dot, 2.) lower left dot, 3.) upper right dot, 4.) lower right dot, 5.) center dot, 6.) middle left dot, 7.) middle right dot.
    - This consists of 14 dots overall.
    - The dots will be colored white.
5. **Use random library's randint in order to randomize the dots on the dice.**
    - The random cases start from 1 to 6 which represent the 6 different dice faces.
    - We create if/else if loops for each of the dice, separately.
    - First case contains the face of the dice with only one dot.
    - Second case contains the face of the dice with two dots.
    - Third case contains the face of the dice with three dots.
    - Fourth case contains the face of the dice with four dots.
    - Fifth case contains the face of the dice with five dots.
    - Sixth case contains the face of the dice with six dots.
6. **Remove the starting text regarding instructions.**
7. **If/else loop where, if the random loop for the first die has the same value of the random loop for the second die, then the user wins.**
    - The user loses if the values do not match.
    - A text saying "YOU WON!" or "YOU LOST!" appears under the dice.
    - Ex. If random loop of first die and random loop of second die are both 6 then "YOU WIN!"
8. **Remove winning/losing text.**
9. **Display final text saying that, to close the game, you must click the window again.**
10. **Close the game with win.close()**

**References**
- HW 4 dice exercise (my own)
- graphics pdf document
- https://stackoverflow.com/questions/15651521/dice-roll-in-python-gui

*Justification for using StackOverflow website:*
I had thought of the idea of making a probability game using the dice exercise in HW 4
because of someone's comment asking me "do the dice roll?" when I showed them my homework output, but I
had trouble figuring out how to change the dice faces using getMouse().
I had already tried using loops for this but nothing worked.
Then, I found this website and saw the question poster had a similar project as me.
I decided to use the random library and the if/else if statement similarly to the question poster,
but I accomodated the dots with my knowledge of the positioning. So, if you see our projects they are different.
Since my project is a game, I made an if statement so that the user will get a text output for when they win or lose the game.
