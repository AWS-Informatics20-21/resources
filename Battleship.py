# BattleShip Template

from graphics import *

def main():

    print("Opening the Battleship game")

    

    win = GraphWin("Battleship", 600, 800)

    #create a grid in a for loop   
    #create x coordinates
    for i in range(8):
        p1 = Point(200 + i*50, 0)
        p2 = Point(200 + i*50, 800)
        l = Line(p1, p2)
        l.draw(win)

    #create y coordinate
    for i in range(16):
        p1 = Point(200, i*50)
        p2 = Point(600, i*50)
        l = Line(p1, p2)
        l.draw(win)

    middle = Line(Point(200, 400), Point(600, 400))
    middle.setWidth(5)
    middle.draw(win)

    '''sampleC = Circle(Point(375,475), 24)
    sampleC.draw(win)
    sampleC.setFill('cyan')'''

    #small
    sampleC = Circle(Point(140,480), 24)
    sampleC.draw(win)
    sampleC.setFill('cyan')

    smallT = Text(Point(100,480),"2 x ")
    smallT.setSize(14)
    smallT.draw(win)

    #medium
    medC = Circle(Point(110,540), 24)
    medC2 = Circle(Point(160,540), 24)
    medC.draw(win)
    medC.setFill('cyan')
    medC2.draw(win)
    medC2.setFill('cyan')

    medT = Text(Point(75,540),"3 x ")
    medT.setSize(14)
    medT.draw(win)

    #large
    largeC = Circle(Point(65,600), 24)
    largeC2 = Circle(Point(115,600), 24)
    largeC3 = Circle(Point(165,600), 24)
    largeC.draw(win)
    largeC2.draw(win)
    largeC3.draw(win)
    largeC.setFill('cyan')
    largeC2.setFill('cyan')
    largeC3.setFill('cyan')

    largeT = Text(Point(30,600),"1 x ")
    largeT.setSize(14)
    largeT.draw(win)

    #hit
    h = Circle(Point(100,330), 22)
    h.setOutline('red')
    h.setWidth(3)
    h.draw(win)
    hText = Text(Point(60, 330), "hit:")
    hText.draw(win)

    #miss
    l1 = Line(Point(76,380), Point(124,428))
    l2 = Line(Point(76, 428), Point(124, 380))
    l1.setOutline('blue')
    l2.setOutline('blue')
    l1.draw(win)
    l2.draw(win)
    lText = Text(Point(50, 402), "miss:")
    lText.draw(win)

    #intstructions
    inst = Text(Point(100,60), "Welcome to Battleship!")
    inst1 = Text(Point(100,120), "To play, you will need a partner.")
    inst2 = Text(Point(100,160), "1. Edit the python file to draw ships!")
    inst3 = Text(Point(100,200), "2. Locate your opponents ships!")
    inst4 = Text(Point(100,240), "3. Edit the python file to draw hits!")

    inst.setSize(18)
    inst.draw(win)
    inst1.draw(win)
    inst2.draw(win)
    inst3.draw(win)
    inst4.draw(win)
    
 









    



if __name__ == "__main__":
    main()





    




