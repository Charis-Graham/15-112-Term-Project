from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *

#initiates the game mode 
def gameMode_initiate(app):

    #create a margin for side scrolling
    app.xScroll = 0
    app.yScroll = 0 
    app.marginScroll = 100

    #draw grass
    gameMode_grass(app)

    #creates a player of class elephant
    app.player = Elephant(app, "baby", 100, 100, 100, 
                        app.width//2, app.height//2)

    #initializes the animations for walking and standing still
    app.player.elephantWalking(app)
    app.player.elephantStandStill(app)

    #draws a tree
    app.tree = Tree(100, 300, 300)
    app.tree.treeImage(app)

    #creates an element of class water
    app.water = WateringHole(100, 100, 100)
    app.water.waterImage(app)

#controls the available keyboard interactions
def gameMode_keyPressed(app, event):
    #controls the player moving
    playerMove(app, event)

    #to be removed later, these are controls to test certain unfinished 
    #elements of water and tree classes
    if event.key == "d" and app.player.intersectsObject(app.water):
        app.water.goMuddy(app)
        app.water.waterLevel -= 10
    elif event.key == "e" and app.player.intersectsObject(app.tree):
        app.tree.goLeaves(app)
        app.tree.leafLevel -= 10
    elif event.key == "h":
        app.mode = "helpScreenMode"

#makes the elephant still when not moving
def gameMode_keyReleased(app, event):
    #controls what happens when the elephant is still
    playerStill(app, event)


#contols the time sensitive elements of game play
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

#draws the board
def gameMode_redrawAll(app, canvas):
    #draws the ground
    gameMode_drawGround(app, canvas)

    #draws a tree
    app.tree.X -= app.xScroll
    app.tree.drawTree(app, canvas)

    #draw water
    app.water.X -= app.xScroll
    app.water.drawWater(app, canvas)

    #draws the player elephant
    if (app.player.elephantMoveLeft == False and 
        app.player.elephantMoveDown == False and
        app.player.elephantMoveRight == False and 
        app.player.elephantMoveUp == False):
        app.player.drawElephantStill(app, canvas)
    else:
        app.player.imageX -= app.xScroll
        app.player.drawElephantWalk(app, canvas)