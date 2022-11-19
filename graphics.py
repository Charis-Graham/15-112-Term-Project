from cmu_112_graphics import *
import random

#ELEPHANT

#Used below as starting basis, but rewrote most of it as my own code
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingFile
#initializes the graphics for the elephant walking 
def elephantWalk(app):
    #loads in the elephant image
    app.elephantImage = app.loadImage('images/elephant.png')
    elephantWalk = app.elephantImage

    #builds the elephant walking down animation
    app.elephantWalkDown = []
    for frame in range(3):
        elephantDownStep = elephantWalk.crop((app.width//4*frame, 0, 
                                            app.width//4+app.width//4*frame, 
                                            app.height//4))
        app.elephantWalkDown.append(elephantDownStep)

    #builds the elephant walking left animation
    app.elephantWalkLeft = []
    for frame in range(3):
        elephantStepLeft = elephantWalk.crop((app.width//4.1*frame, app.height//4,
                                            app.width//4.2+app.width//4*frame, 
                                            app.height//2))
        app.elephantWalkLeft.append(elephantStepLeft)
    
    #builds the elephant walking right animation
    app.elephantWalkRight = []
    for frame in range(3):
        elephantStepRight = elephantWalk.crop((app.width//4.1*frame, 
                                            app.height//2, 
                                            app.width//4.3+app.width//4*frame,
                                            3*(app.height//4)))
        app.elephantWalkRight.append(elephantStepRight)

    #builds the elephant walking up animation
    app.elephantWalkUp = []
    for frame in range(3):
        elephantUpStep = elephantWalk.crop((app.width//4*frame, 
                                            3*(app.height//4), 
                                            app.width//4+app.width//4*frame, 
                                            app.height))
        app.elephantWalkUp.append(elephantUpStep)

    #initializes the elephant state of the elephant moving as false
    app.elephantMoveLeft = True
    app.elephantMoveRight = False
    app.elephantMoveDown = False
    app.elephantMoveUp = False

    app.numFrames = 3
    app.spriteCounter = 0

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

#TREE

#WATER

#GRASS
def tessellationGrassGround(app):
    #based on Eli Courtwright's answer on
    #https://stackoverflow.com/questions/1060090/changing-variable-names-with-python-for-loops
    #creates a dictionary with the five grass tiles
    grassImages = {}
    for panel in range(1, 6):
        app.grassImage["grass"+str(panel)] = app.loadImage(f'images/grass/grass{panel}.jpg')
    
    