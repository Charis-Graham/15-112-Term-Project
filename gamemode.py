from cmu_112_graphics import *
from boardGeneration import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *
from endScreen import *
from challenges import *

#initiates the game mode 
def gameMode_initiate(app):

    #create a margin for side scrolling
    app.xScroll = 0
    app.marginScroll = 100

    #keeps track of which challenge the player is on
    app.challengeCount = 1
    app.elephantIntersectCount = 0
    app.elephantWaterShared = 0
    app.elephantFoodShared = 0
    app.elephantIntersected = []
    app.elephantFed = []
    app.elephantWater = []

    #draw grass
    gameMode_grass(app)

    #creates a player of class elephant
    app.player = Elephant(app, "baby", 0, 0, 10, 
                        app.width//2, app.height//2)

    #initializes the animations for walking and standing still
    app.player.elephantWalking(app)
    app.player.elephantStandStill(app)

    #makes the gameboard and challenges elementsB
    gameMode_makeGameBoard(app)
    gameMode_challenges(app)
    gameMode_elephantBones(app)

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
    
    elif event.key == "f":
        for elephant in app.elephantList:
            if app.player.intersectsObject(elephant):
                elephant.hunger += 1
                app.player.shareHunger()
    
    elif event.key == "w":
        for elephant in app.elephantList:
            if app.player.intersectsObject(elephant):
                elephant.thirst += 1
                app.player.shareWater()
        
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
    #checks if the death state is matched
    gameMode_death(app)

    #keeps track of elements for challenges
    gameMode_elephantIntersectCount(app)
    gameMode_checkSharedWater(app)
    gameMode_checkSharedFood(app)
    gameMode_challenge(app)

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

    #initiates the challenges
    gameMode_drawChallenge(app, canvas)
    gameMode_challengeProgression(app, canvas)

    x0, y0, x1, y1 = app.player.getBounds()
    canvas.create_rectangle(x0, y0, x1, y1, fill = "green")
    canvas.create_oval(x0, y0, x0+5, y0+5, fill = "white")
    canvas.create_oval(x1, y1, x1+5, y1+5, fill = "black")

    # for tree in app.treeList:
    #     x, y, xa, ya = tree.getBounds()
    #     canvas.create_rectangle(x, y, xa, ya, fill = "red")
    #     canvas.create_oval(x, y, x+5, y+5, fill = "white")
    #     canvas.create_oval(xa, ya, xa+5, ya+5, fill = "black")
    
    # for water in app.waterList:
    #     x, y, xb, yb = water.getBounds()
    #     canvas.create_rectangle(x, y, xb, yb, fill = "blue")
    #     canvas.create_oval(x, y, x+5, y+5, fill = "white")
    #     canvas.create_oval(xb, yb, xb+5, yb+5, fill = "black")
    
    # for elephant in app.elephantList:
    #     x, y, xb, yb = elephant.getBounds()
    #     canvas.create_rectangle(x, y, xb, yb, fill = "purple")
    #     canvas.create_oval(x, y, x+5, y+5, fill = "white")
    #     canvas.create_oval(xb, yb, xb+5, yb+5, fill = "black")
    #     print("Hunger:", elephant.hunger, "Thirst:", elephant.thirst)


    #draws the player elephant
    if (app.player.elephantMoveLeft == False and 
        app.player.elephantMoveDown == False and
        app.player.elephantMoveRight == False and 
        app.player.elephantMoveUp == False):
        app.player.drawElephantStill(app, canvas)
    else:
        app.player.drawElephantWalk(app, canvas)