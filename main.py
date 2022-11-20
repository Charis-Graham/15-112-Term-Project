#6:40 - 7:32pm, 52 min
#7:45 - 8:46pm, 1 hr, 1 min
#9:05 - 10:00pm, 55 min
#1:30 - 1:48am
#1:50 - 2:50am 1 hr 18 min
#11:15 - 5:45 5hr 30 min

'''Goals for tomorrow:
- work on interaction of elephant with surroundings
 ---> the water becomes more muddy color
 ---> tree becomes duller and disappears
'''

from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *
from classes import *

def appStarted(app):
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

def keyPressed(app, event):
    #controls the player moving
    playerMove(app, event)

def keyReleased(app, event):
    playerStill(app, event)

def timerFired(app):
    #this runs through the sprite to have the elephant walk at a constant pace
    #this line is copied from timerFired in
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    app.player.spriteCounter = (1 + app.player.spriteCounter) % app.player.numFrames

def redrawAll(app, canvas):
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

runApp(width = 400, height = 400)