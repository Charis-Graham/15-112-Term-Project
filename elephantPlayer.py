from cmu_112_graphics import *

#keyboard controls for the player to move
def playerMove(app, event):
    if event.key == "Left":
        app.player.elephantMoveLeft = True
        app.player.elephantMoveRight = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False
    elif event.key == "Right":
        app.player.elephantMoveRight = True
        app.player.elephantMoveLeft = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False
    elif event.key == "Down":
        app.player.elephantMoveDown = True
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False
        app.player.elephantMoveUp = False
    elif event.key == "Up":
        app.player.elephantMoveUp = True
        app.player.elephantMoveDown = False
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False