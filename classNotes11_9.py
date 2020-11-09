# class notes from 11/9 where we start graphics!

from graphics import *

def main():

    print("Starting graphics")

    win = GraphWin("My graphics", 800, 600)
    win.setBackground("red")

    p1 = Point(100,100)
    p2 = Point(300,400)

    r = Rectangle(p1,p2)
    r.setFill("cyan")
    r.draw(win)



if __name__ == "__main__":
    main()
