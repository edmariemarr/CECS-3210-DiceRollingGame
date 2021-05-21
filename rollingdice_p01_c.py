from graphics import *
from random import *

class Dice:
    def __init__(self, x1, y1, x2, y2, color, win):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.win = win
        self.first = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))  # sets body for dice 1
        self.first.setFill(self.color)
        self.first.draw(self.win)

class Dots:
    def __init__(self, x, y, radius, win):
        self.x = x
        self.y = y
        self.radius = radius
        self.win = win
        self.dot = Circle(Point(self.x, self.y), self.radius)  # sets dot
        self.dot.setFill('white')
        self.dot.draw(win)

def main():
    win = GraphWin('Dice Rolling Game', 300, 100)
    win.setCoords(0, 0, 16, 5)

    Dice(4, 2, 6, 4, 'black', win)
    Dice(10, 2, 12, 4, 'pink', win)

    msg = Text(Point(8, 1), "Please click each die twice to roll.")  # text output for start
    msg.draw(win)

    win.autoflush = True
    win.getMouse()

    rand = randint(1, 6)  # using randint to randomize the dots on the first dice
    if rand == 1:  # first case: dice with 1 dot
        win.getMouse()
        dot_5 = Dots(5, 3, 0.2, win)
    elif rand == 2:  # second case: dice with 2 dots
        win.getMouse()
        dot_1 = Dots(4.5, 3.5, 0.2, win)
        dot_4 = Dots(5.5, 2.5, 0.2, win)
    elif rand == 3:  # third case: dice with 3 dots
        win.getMouse()
        dot_2 = Dots(4.5, 2.5, 0.2, win)
        dot_3 = Dots(5.5, 3.5, 0.2, win)
        dot_5 = Dots(5, 3, 0.2, win)
    elif rand == 4:  # fourth case: dice with 4 dots
        win.getMouse()
        dot_1 = Dots(4.5, 3.5, 0.2, win)
        dot_2 = Dots(4.5, 2.5, 0.2, win)
        dot_3 = Dots(5.5, 3.5, 0.2, win)
        dot_4 = Dots(5.5, 2.5, 0.2, win)
    elif rand == 5:  # fifth case: dice with 5 dots
        win.getMouse()
        dot_1 = Dots(4.5, 3.5, 0.2, win)
        dot_2 = Dots(4.5, 2.5, 0.2, win)
        dot_3 = Dots(5.5, 3.5, 0.2, win)
        dot_4 = Dots(5.5, 2.5, 0.2, win)
        dot_5 = Dots(5, 3, 0.2, win)
    elif rand == 6:  # sixth case: dice with 6 dots
        win.getMouse()
        dot_1 = Dots(4.5, 3.5, 0.2, win)
        dot_2 = Dots(4.5, 2.5, 0.2, win)
        dot_3 = Dots(5.5, 3.5, 0.2, win)
        dot_4 = Dots(5.5, 2.5, 0.2, win)
        dot_6 = Dots(4.5, 3, 0.2, win)
        dot_7 = Dots(5.5, 3, 0.2, win)

    rand1 = randint(1, 6)  # using randint to randomize the dots on the second dice
    if rand1 == 1:  # first case: dice with 1 dot
        win.getMouse()
        dot_12 = Dots(11, 3, 0.2, win)
    elif rand1 == 2:  # second case: dice with 2 dots
        win.getMouse()
        dot_8 = Dots(10.5, 3.5, 0.2, win)
        dot_11 = Dots(11.5, 2.5, 0.2, win)
    elif rand1 == 3:  # third case: dice with 3 dots
        win.getMouse()
        dot_9 = Dots(10.5, 2.5, 0.2, win)
        dot_10 = Dots(11.5, 3.5, 0.2, win)
        dot_12 = Dots(11, 3, 0.2, win)
    elif rand1 == 4:  # fourth case: dice with 4 dots
        win.getMouse()
        dot_8 = Dots(10.5, 3.5, 0.2, win)
        dot_9 = Dots(10.5, 2.5, 0.2, win)
        dot_10 = Dots(11.5, 3.5, 0.2, win)
        dot_11 = Dots(11.5, 2.5, 0.2, win)
    elif rand1 == 5:  # fifth case: dice with 5 dots
        win.getMouse()
        dot_8 = Dots(10.5, 3.5, 0.2, win)
        dot_9 = Dots(10.5, 2.5, 0.2, win)
        dot_10 = Dots(11.5, 3.5, 0.2, win)
        dot_11 = Dots(11.5, 2.5, 0.2, win)
        dot_12 = Dots(11, 3, 0.2, win)
    elif rand1 == 6:  # sixth case: dice with 6 dots
        win.getMouse()
        dot_8 = Dots(10.5, 3.5, 0.2, win)
        dot_9 = Dots(10.5, 2.5, 0.2, win)
        dot_10 = Dots(11.5, 3.5, 0.2, win)
        dot_11 = Dots(11.5, 2.5, 0.2, win)
        dot_13 = Dots(10.5, 3, 0.2, win)
        dot_14 = Dots(11.5, 3, 0.2, win)

    msg.undraw()

    if rand == rand1:
        msg = Text(Point(8, 1), "YOU WON!")
        msg.draw(win)
    else:
        msg = Text(Point(8, 1), "YOU LOST!")
        msg.draw(win)

    update()
    time.sleep(3)
    win.autoflush = True
    msg.undraw()

    msg = Text(Point(8, 1), "Click again to close game.")  # text output for end
    msg.draw(win)
    win.getMouse()
    win.close()

main()
