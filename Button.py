from graphics import *

class Button():

    def __init__(self, win, color, text, center, size):

        p1 = Point(center.x - size, center.y - size/2)
        p2 = Point(center.x + size, center.y + size/2)
        self.r = Rectangle(p1, p2)
        self.r.draw(win)
        self.r.setFill(color)
        self.t = Text(center, text)
        self.t.setSize(18)
        self.t.draw(win)


    def changeColor(self, newColor):
        self.r.setFill(newColor)
        
