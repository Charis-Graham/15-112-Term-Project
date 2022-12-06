from cmu_112_graphics import *
import random

#Copied and slightly modified from
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
def gameMode_makePlayerVisible(app):
    # scroll to make player visible as needed
    if (app.player.imageX < app.xScroll + app.marginScroll):
        app.xScroll = app.player.imageX - app.marginScroll
    if (app.player.imageX > app.xScroll + app.width - app.marginScroll):
        app.xScroll = app.player.imageX - app.width + app.marginScroll

#change elephant stats
def gameMode_changePlayerStats(app):
    app.player.travel += 1
    app.player.hunger = round(app.player.hunger + 0.1, 1)
    app.player.thirst = round(app.player.thirst + 0.2, 1)
    app.player.energy = round(app.player.energy - 0.1, 1)

def gameMode_alterObjectPositions(app, direction):
    if direction == "Left":
        for tree in app.treeList:
            tree.X -= app.xScroll
        
        for water in app.waterList:
            water.X -= app.xScroll
    elif direction == "Right":
        for tree in app.treeList:
            tree.X += app.xScroll
        
        for water in app.waterList:
            water.X += app.xScroll


#keyboard controls for the player to move
def playerMove(app, event):
    if app.player.lifeState == "baby":
        if app.player.thirst > 10 or app.player.hunger > 12 or app.player.energy < 5:
            moveD = 5
        else:
            moveD = 10
    elif app.player.lifeState == "adult":
        if app.player.thirst > 12 or app.player.hunger > 15 or app.player.energy < 10:
            moveD = 5
        else:
            moveD = 10
    elif app.player.lifeState == "elder":
        if app.player.thirst > 15 or app.player.hunger > 17 or app.player.energy < 15:
            moveD = 5
        else:
            moveD = 10

    if event.key == "Left" and app.player.imageX > -app.width:
        app.player.elephantMoveLeft = True
        app.player.elephantMoveRight = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False

        #changes the position of the player
        app.player.imageX -= (moveD + app.xScroll)
            
        #alters the players stats and adjusts the positions of the objects
        gameMode_changePlayerStats(app)
        gameMode_alterObjectPositions(app, "Left")
        

    elif event.key == "Right" and app.player.imageX < 2*app.width:
        app.player.elephantMoveRight = True
        app.player.elephantMoveLeft = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False

        app.player.imageX += moveD + app.xScroll
        
        gameMode_changePlayerStats(app)
        gameMode_alterObjectPositions(app, "Right")

    elif event.key == "Down" and app.player.imageY < app.height:
        app.player.elephantMoveDown = True
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False
        app.player.elephantMoveUp = False

        app.player.imageY += moveD
        
        gameMode_changePlayerStats(app)

    elif event.key == "Up" and app.player.imageY > 0:
        app.player.elephantMoveUp = True
        app.player.elephantMoveDown = False
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False

        app.player.imageY -= moveD
        
        gameMode_changePlayerStats(app)
    
    gameMode_makePlayerVisible(app)


#defines what happens if the player is not moving
def playerStill(app, event):
    if event.key in ["Right", "Left", "Up", "Down"]:
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False
    gameMode_makePlayerVisible(app)

#creates the conditions for death
def gameMode_death(app):
    # if ((app.player.hunger > 25 or 
    #     app.player.thirst > 20 or 
    #     app.player.energy < 2) 
    #     and app.player.lifeState == "baby"):
    #     app.mode = "endMode"
    # elif ((app.player.hunger > 30 or 
    #     app.player.thirst > 25 or 
    #     app.player.energy < 10)
    #     and app.player.lifeState == "adult"):
    #     app.mode = "endMode"
    # elif ((app.player.hunger > 35 or 
    #     app.player.thirst > 30 or 
    #     app.player.energy < 15) 
    #     and app.player.lifeState == "old"):
    #     app.mode = "endMode"
    pass
    