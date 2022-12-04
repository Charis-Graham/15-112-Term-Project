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

#keyboard controls for the player to move
def playerMove(app, event):
    if event.key == "Left":
        app.player.elephantMoveLeft = True
        app.player.elephantMoveRight = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False

        app.player.imageX -= 10
        gameMode_changePlayerStats(app)
        gameMode_makePlayerVisible(app)

    elif event.key == "Right":
        app.player.elephantMoveRight = True
        app.player.elephantMoveLeft = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False

        app.player.imageX += 10
        
        gameMode_changePlayerStats(app)
        gameMode_makePlayerVisible(app)

    elif event.key == "Down":
        app.player.elephantMoveDown = True
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False
        app.player.elephantMoveUp = False

        app.player.imageY += 10
        
        gameMode_changePlayerStats(app)
        gameMode_makePlayerVisible(app)

    elif event.key == "Up":
        app.player.elephantMoveUp = True
        app.player.elephantMoveDown = False
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False

        app.player.imageY -= 10
        
        gameMode_changePlayerStats(app)
        gameMode_makePlayerVisible(app)

#defines what happens if the player is not moving
def playerStill(app, event):
    if event.key in ["Right", "Left", "Up", "Down"]:
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False