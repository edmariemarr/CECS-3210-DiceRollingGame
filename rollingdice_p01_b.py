from graphics import *
from random import *

# DICE ROLL GAME
# A probability game using two dice where,
# -- You win if both dice 1 and dice 2 have the same faces.
# -- You lose if both dice 1 and dice 2 have different faces.

# Resources:
# dice exercise on HW 4
# graphics.pdf
# https://stackoverflow.com/questions/15651521/dice-roll-in-python-gui

# Some changes:
# - Uses functions in order to organize the game's various steps
# - Global variables to access within other functions (ex. msg is the variable for all text now)

def main():
    win = GraphWin('Dice Rolling Game', 300, 100)    # set window
    win.setCoords(0, 0, 16, 5)

    firstdice(win)
    seconddice(win)

    startingtext(win)

    win.autoflush = False
    win.getMouse()

    randfirst(win)
    win.getMouse()
    randsecond(win)

    msg.undraw()
    results(win, rand1, rand)

    endingtext(win)

def firstdice(win):
    # draw square for first dice
    first = Rectangle(Point(4, 2), Point(6, 4))  # sets body for dice 1
    first.setFill('black')
    first.draw(win)

def seconddice(win):
    # draw square for second dice
    second = Rectangle(Point(10, 2), Point(12, 4))  # sets body for dice 2
    second.setFill('pink')
    second.draw(win)

def startingtext(win):
    global msg
    msg = Text(Point(8, 1), "Please click each die twice to roll.")    # text output for start
    msg.draw(win)

def firstdots():
    # setting dots for first dice
    global dot1, dot2, dot3, dot4, dot5, dot6, dot7
    dot1 = Circle(Point(4.5, 3.5), 0.2)  # sets upper left dot
    dot1.setFill('white')
    dot2 = Circle(Point(4.5, 2.5), 0.2)  # sets lower left dot
    dot2.setFill('white')
    dot3 = Circle(Point(5.5, 3.5), 0.2)  # sets upper right dot
    dot3.setFill('white')
    dot4 = Circle(Point(5.5, 2.5), 0.2)  # sets lower right dot
    dot4.setFill('white')
    centerfirst = Point(5, 3)  # center of first dice
    dot5 = Circle(centerfirst, 0.2)  # sets center dot
    dot5.setFill('white')
    dot6 = Circle(Point(4.5, 3), 0.2)   # sets middle left dot
    dot6.setFill('white')
    dot7 = Circle(Point(5.5, 3), 0.2)   # sets middle right dot
    dot7.setFill('white')

def seconddots():
    # setting dots for second dice
    global dot8, dot9, dot10, dot11, dot12, dot13, dot14
    dot8 = Circle(Point(10.5, 3.5), 0.2)  # sets upper left dot
    dot8.setFill('white')
    dot9 = Circle(Point(10.5, 2.5), 0.2)  # sets lower left dot
    dot9.setFill('white')
    dot10 = Circle(Point(11.5, 3.5), 0.2)  # sets upper right dot
    dot10.setFill('white')
    dot11 = Circle(Point(11.5, 2.5), 0.2)  # sets lower right dot
    dot11.setFill('white')
    centersecond = Point(11, 3)  # center of second dice
    dot12 = Circle(centersecond, 0.2)  # sets center dot
    dot12.setFill('white')
    dot13 = Circle(Point(10.5, 3), 0.2)  # sets middle left dot
    dot13.setFill('white')
    dot14 = Circle(Point(11.5, 3), 0.2)  # sets middle right dot
    dot14.setFill('white')

def randfirst(win):
    firstdots()
    global rand
    rand = randint(1, 6)    # using randint to randomize the dots on the first dice
    if rand == 1:   # first case: dice with 1 dot
        win.getMouse()
        dot5.draw(win)
    elif rand == 2:     # second case: dice with 2 dots
        win.getMouse()
        dot1.draw(win)
        dot4.draw(win)
    elif rand == 3:     # third case: dice with 3 dots
        win.getMouse()
        dot2.draw(win)
        dot3.draw(win)
        dot5.draw(win)
    elif rand == 4:     # fourth case: dice with 4 dots
        win.getMouse()
        dot1.draw(win)
        dot2.draw(win)
        dot3.draw(win)
        dot4.draw(win)
    elif rand == 5:     # fifth case: dice with 5 dots
        win.getMouse()
        dot1.draw(win)
        dot2.draw(win)
        dot3.draw(win)
        dot4.draw(win)
        dot5.draw(win)
    elif rand == 6:     # sixth case: dice with 6 dots
        win.getMouse()
        dot1.draw(win)
        dot2.draw(win)
        dot3.draw(win)
        dot4.draw(win)
        dot6.draw(win)
        dot7.draw(win)

def randsecond(win):
    seconddots()
    global rand1
    rand1 = randint(1, 6)   # using randint to randomize the dots on the second dice
    if rand1 == 1:      # first case: dice with 1 dot
        win.getMouse()
        dot12.draw(win)
    elif rand1 == 2:    # second case: dice with 2 dots
        win.getMouse()
        dot8.draw(win)
        dot11.draw(win)
    elif rand1 == 3:    # third case: dice with 3 dots
        win.getMouse()
        dot9.draw(win)
        dot10.draw(win)
        dot12.draw(win)
    elif rand1 == 4:    # fourth case: dice with 4 dots
        win.getMouse()
        dot8.draw(win)
        dot9.draw(win)
        dot10.draw(win)
        dot11.draw(win)
    elif rand1 == 5:    # fifth case: dice with 5 dots
        win.getMouse()
        dot8.draw(win)
        dot9.draw(win)
        dot10.draw(win)
        dot11.draw(win)
        dot12.draw(win)
    elif rand1 == 6:    # sixth case: dice with 6 dots
        win.getMouse()
        dot8.draw(win)
        dot9.draw(win)
        dot10.draw(win)
        dot11.draw(win)
        dot13.draw(win)
        dot14.draw(win)

def results(win, rand1, rand):
    # loop to check whether the dots on both die are the same amount
    # -- if they are, the user won.
    # -- if not, the user lost.
    if rand1 == rand:
        msg = Text(Point(8, 1), "YOU WON!")
        msg.draw(win)
    else:
        msg = Text(Point(8, 1), "YOU LOST!")
        msg.draw(win)
    update()
    time.sleep(3)   # wait a few seconds before next text
    win.autoflush = True
    msg.undraw()

def endingtext(win):
    msg = Text(Point(8, 1), "Click again to close game.")    # text output for end
    msg.draw(win)
    win.getMouse()
    win.close()     # close window

main()
