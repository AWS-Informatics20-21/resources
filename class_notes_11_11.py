# class notes from 11/11 where we start graphics!

from graphics import *

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

    



if __name__ == "__main__":
    main()





    




