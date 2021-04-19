from graphics import *
from random import *

# DICE ROLL GAME
# A probability game using two dice where,
# -- You win if both dice 1 and dice 2 have the same faces.
# -- You lose if both dice 1 and dice 2 have different faces.

def main():
    win = GraphWin('Dice Rolling Game', 300, 100)    # set window
    win.setCoords(0, 0, 16, 5)

    # draw square for first dice
    first = Rectangle(Point(4, 2), Point(6, 4))  # sets body for dice 1
    first.setFill('black')
    first.draw(win)

    # draw square for second dice
    second = Rectangle(Point(10, 2), Point(12, 4))  # sets body for dice 2
    second.setFill('pink')
    second.draw(win)

    starting = Text(Point(8, 1), "Please click each die twice to roll.")    # text output for start
    starting.draw(win)

    # setting dots for first dice
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


    # setting dots for second dice
    dot6 = Circle(Point(10.5, 3.5), 0.2)  # sets upper left dot
    dot6.setFill('white')
    dot7 = Circle(Point(10.5, 2.5), 0.2)  # sets lower left dot
    dot7.setFill('white')
    dot8 = Circle(Point(11.5, 3.5), 0.2)  # sets upper right dot
    dot8.setFill('white')
    dot9 = Circle(Point(11.5, 2.5), 0.2)  # sets lower right dot
    dot9.setFill('white')
    centersecond = Point(11, 3)  # center of second dice
    dot10 = Circle(centersecond, 0.2)  # sets center dot
    dot10.setFill('white')

    win.getMouse()
    rand = randint(1, 5)    # using randint to randomize the dots on the first dice
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

    win.getMouse()
    rand1 = randint(1, 5)   # using randint to randomize the dots on the second dice
    if rand1 == 1:      # first case: dice with 1 dot
        win.getMouse()
        dot10.draw(win)
    elif rand1 == 2:    # second case: dice with 2 dots
        win.getMouse()
        dot6.draw(win)
        dot9.draw(win)
    elif rand1 == 3:    # third case: dice with 3 dots
        win.getMouse()
        dot7.draw(win)
        dot8.draw(win)
        dot10.draw(win)
    elif rand1 == 4:    # fourth case: dice with 4 dots
        win.getMouse()
        dot6.draw(win)
        dot7.draw(win)
        dot8.draw(win)
        dot9.draw(win)
    elif rand1 == 5:    # fifth case: dice with 5 dots
        win.getMouse()
        dot6.draw(win)
        dot7.draw(win)
        dot8.draw(win)
        dot9.draw(win)
        dot10.draw(win)

    win.getMouse()
    win.close()     # close window

main()
