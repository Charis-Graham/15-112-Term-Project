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

#draw the elephant walking around
def drawElephantWalking(app, canvas):
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