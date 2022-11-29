from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *

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
    

def gameMode_keyReleased(app, event):
    #controls what happens when the elephant is still
    playerStill(app, event)

def gameMode_timerFired(app):
    #this runs through the sprite to have the elephant walk at a constant pace
    #this line is copied from timerFired in
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    app.player.spriteCounter = (1 + app.player.spriteCounter) % app.player.numFrames

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