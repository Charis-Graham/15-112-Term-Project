from cmu_112_graphics import *
from boardGeneration import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *

#initiates the game mode 
def gameMode_initiate(app):

    #create a margin for side scrolling
    app.xScroll = 0
    app.marginScroll = 100

    app.timerDelay = 1

    #draw grass
    gameMode_grass(app)

    #creates a player of class elephant
    app.player = Elephant(app, 0, 0, 0, 100, 
                        app.width//2, app.height//2)

    #initializes the animations for walking and standing still
    app.player.elephantWalking(app)
    app.player.elephantStandStill(app)

    gameMode_makeGameBoard(app)

#controls the available keyboard interactions
def gameMode_keyPressed(app, event):
    #controls the player moving
    playerMove(app, event)

    #what happens if the elephant drinks water
    if event.key == "d":
        for water in app.waterList:
            if app.player.intersectsObject(water):
                water.goMuddy(app)
                if app.player.thirst > 10:
                    water.waterLevel -= 10
                    app.player.thirst -= 10
       
    #if the elephant eats    
    elif event.key == "e":
        for tree in app.treeList:
            if app.player.intersectsObject(tree):
                tree.goLeaves(app)
                if app.player.hunger > 10:
                    tree.leafLevel -= 10
                    app.player.hunger -= 10
        
    #gets the help screen
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

    #gameMode_refusePlayerOverlap(app)

    #keeps the game mode from being resized
    #will probably be removed later
    if (app.width != app.helpScreen.size[0] 
        or app.height != app.helpScreen.size[1]):
        app.setSize(app.helpScreen.size[0], app.helpScreen.size[1])

#draws the board
def gameMode_redrawAll(app, canvas):
    #draws the ground
    gameMode_drawGround(app, canvas)

    #generates and draws the game board
    gameMode_drawGameBoard(app, canvas)
    gameMode_statBoard(app, canvas)

    #draws the player elephant
    if (app.player.elephantMoveLeft == False and 
        app.player.elephantMoveDown == False and
        app.player.elephantMoveRight == False and 
        app.player.elephantMoveUp == False):
        app.player.drawElephantStill(app, canvas)
    else:
        app.player.drawElephantWalk(app, canvas)
    