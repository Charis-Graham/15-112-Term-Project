from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *

def gameMode_initiate(app):
    #draw grass
    grass(app)

    #draws a tree
    app.tree = Tree(100)
    app.tree.treeImage(app)

    #creates an element of class water
    app.water = WateringHole(app, 100)
    app.water.waterImage(app)

    #creates a player of class elephant
    app.player = Elephant(app, "baby", 100, 100, 100)
    #initializes the animations for walking and standing still
    app.player.elephantWalking(app)
    app.player.elephantStandStill(app)

#Copied from game object class developed in Lecture 1
#Tuesday, November 22, 2022 by Pat Virtue
#which was based on side scroller #3 on 
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
def gameMode_getBounds(self):
    # returns absolute bounds, not taking scrollX into account
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

def gameMode_keyPressed(app, event):
    #controls the player moving
    playerMove(app, event)

    #to be removed later, these are controls to test certain unfinished 
    #elements of water and tree classes
    if event.key == "t":
        app.tree.randomTreeSpawn(app)
    elif event.key == "w":
        app.water.randomWaterSpawn(app)
    elif event.key == "r":
        app.water.goMuddy(app)
    elif event.key == "l":
        app.tree.goLeaves(app)
    elif event.key == "h":
        app.mode = "helpScreenMode"
    
def gameMode_keyReleased(app, event):
    #controls what happens when the elephant is still
    playerStill(app, event)

def gameMode_timerFired(app):
    #this runs through the sprite to have the elephant walk at a constant pace
    #this line is copied from timerFired in
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    app.player.spriteCounter = (1 + app.player.spriteCounter) % app.player.numFrames

    #keeps the game mode from being resized
    #will probably be removed later
    if (app.width != app.helpScreen.size[0] 
        or app.height != app.helpScreen.size[1]):
        app.setSize(app.helpScreen.size[0], app.helpScreen.size[1])

def gameMode_redrawAll(app, canvas):
    #draws the ground
    drawGround(app, canvas)
    #draws a tree
    app.tree.drawTree(app, canvas)
    #draw water
    app.water.drawWater(app, canvas)
    #draws the player elephant
    if (app.player.elephantMoveLeft == False and 
        app.player.elephantMoveDown == False and
        app.player.elephantMoveRight == False and 
        app.player.elephantMoveUp == False):
        app.player.drawElephantStill(app, canvas)
    else:
        app.player.drawElephantWalk(app, canvas)
        app.player.elephantWeaken()

