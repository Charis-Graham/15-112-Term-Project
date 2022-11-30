from cmu_112_graphics import *

#GRASS BACKGROUND
def gameMode_grass(app):
    #draws the ground
    #Grass PNGs come from https://opengameart.org/content/grass-texture-pack
    #Under CC0
    #Created by Proxy Games
    app.grassImage = app.loadImage("images/grass/grass3.jpg")
    app.grassImage = app.scaleImage(app.grassImage, 12)
    sizeIm = app.grassImage.size
    app.grassImageHeight = sizeIm[1]
    app.grassImageWidth = sizeIm[0]

#draws the background of the game
def gameMode_drawGround(app, canvas):
    imageGrass = ImageTk.PhotoImage(app.grassImage)
    for dw in range(0, app.width, 384):
        for dh in range(0, app.height, 384):
            canvas.create_image(dw, dh,
                                image = imageGrass)

#OBJECT OVERLAP GRAPHICS
#Copied from game object class developed in Lecture 1
#Tuesday, November 22, 2022 by Pat Virtue
#which was based on side scroller #3 on 
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
def gameMode_getBounds(self):
    # returns absolute bounds, not taking xScroll into account
    (x0, y1) = (self.x, self.height/2 - self.y)
    (x1, y0) = (x0 + self.width, y1 - self.height)
    return x0, y0, x1, y1
    
def gameMode_intersectsObject(self, other):
    # return l2<=r1 and t2<=b1 and l1<=r2 and t1<=b2
    (ax0, ay0, ax1, ay1) = self.getBounds
    (bx0, by0, bx1, by1) = other.getBounds
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0))
#------