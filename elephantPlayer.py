from cmu_112_graphics import *

#keyboard controls for the player to move
def playerMove(app, event):
    if event.key == "Left":
        app.elephantMoveLeft = True
        app.elephantMoveRight = False
        app.elephantMoveDown = False
        app.elephantMoveUp = False
    elif event.key == "Right":
        app.elephantMoveRight = True
        app.elephantMoveLeft = False
        app.elephantMoveDown = False
        app.elephantMoveUp = False
    elif event.key == "Down":
        app.elephantMoveDown = True
        app.elephantMoveLeft = False
        app.elephantMoveRight = False
        app.elephantMoveUp = False
    elif event.key == "Up":
        app.elephantMoveUp = True
        app.elephantMoveDown = False
        app.elephantMoveLeft = False
        app.elephantMoveRight = False