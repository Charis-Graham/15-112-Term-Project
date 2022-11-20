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
    if event.key == "t":
        app.tree.randomTreeSpawn(app)
    elif event.key == "w":
        app.water.randomWaterSpawn(app)
    elif event.key == "r":
        app.water.goMuddy(app)
    elif event.key == "l":
        app.tree.goLeaves(app)

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
        app.player.elephantWeaken()

runApp(width = 400, height = 400)