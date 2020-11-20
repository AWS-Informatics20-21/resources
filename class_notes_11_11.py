# class notes from 11/11 where we start graphics!

from graphics import *
from Button import *

def main():

    print("Starting graphics")

    # window is set with a width and a height in terms of pixels.
    # (x , y)

    win = GraphWin("My graphics", 800, 600)

    '''p1 = Point(100, 0)
    p2 = Point(100, 600)
    l = Line(p1, p2)
    l.draw(win)'''

    #create a grid in a for loop   
    #create x coordinates
    for i in range(7):
    
        p1 = Point(100 + i*100, 0)
        p2 = Point(100 + i*100, 600)
        l = Line(p1, p2)
        l.draw(win)

    #create y coordinate
    for i in range(5):
        
        p1 = Point(0, 100 + i*100)
        p2 = Point(800, 100 + i*100)
        l = Line(p1, p2)
        l.draw(win)

    c = Circle(Point(600, 400), 100)
    c.draw(win)
    c.setFill("yellow")
    c.setWidth(10)


    b = Button(win, 'red', "Hi", Point(200, 200), 80)
    quitButton = Button(win, 'red', "Quit", Point(200, 400), 60)

    b.changeColor('green')
    
    b.t.setSize(36)


    while True:
        m1 = win.getMouse()

        #test the quit button
        isFinished = quitButton.isClicked(m1)
        if isFinished:
            break
        
        #testing the clicking of button

        isItClicked = b.isClicked(m1)
        if isItClicked:
            print("it was clicked!")
        else:
            print("we didn't click it")

        

    
    print("Done program")
    win.close()


    



if __name__ == "__main__":
    main()





    




