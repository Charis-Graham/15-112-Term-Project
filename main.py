#6:40 - 7:32pm
#7:45 - pm

from cmu_112_graphics import *
from graphics import *

def appStarted(app):
    #this function displays the elephant walking left
    elephantWalk(app)

def keyPressed(app, event):
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

def timerFired(app):
    #this runs through the sprite to have the elephant walk at a constant pace
    #this line is copied from timerFired in
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    app.spriteCounter = (1 + app.spriteCounter) % app.numFrames

def redrawAll(app, canvas):
    if app.elephantMoveLeft == True:
        elephant = app.elephantWalkLeft[app.spriteCounter]
    elif app.elephantMoveDown == True:
        elephant = app.elephantWalkDown[app.spriteCounter]
    elif app.elephantMoveUp == True:
        elephant = app.elephantWalkUp[app.spriteCounter]
    elif app.elephantMoveRight == True:
        elephant = app.elephantWalkRight[app.spriteCounter]
    #this puts the position of the elephant via the top-left corner
    canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(elephant))

runApp(width = 400, height = 400)