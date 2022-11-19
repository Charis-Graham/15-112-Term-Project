from cmu_112_graphics import *

#ELEPHANT

#Used below as starting basis, but rewrote most of it as my own code
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingFile
#initializes the graphics for the elephant walking 
def elephantWalk(app):
    #loads in the elephant image
    app.elephantImage = app.loadImage('images/elephant.png')
    elephantWalk = app.elephantImage

    #builds the elephant walking left animation
    app.elephantWalkLeft = []
    for frame in range(3):
        elephantStepLeft = elephantWalk.crop((100*frame, 100,96+100*frame, 200))
        app.elephantWalkLeft.append(elephantStepLeft)
    
    #builds the elephant walking right animation
    app.elephantWalkRight = []
    for frame in range(3):
        elephantStepRight = elephantWalk.crop((100*frame, 200, 90+100*frame,300))
        app.elephantWalkRight.append(elephantStepRight)
    
    #builds the elephant walking down animation
    app.elephantWalkDown = []
    for frame in range(3):
        elephantDownStep = elephantWalk.crop((100*frame, 0, 96+100*frame, 100))
        app.elephantWalkDown.append(elephantDownStep)

    #builds the elephant walking up animation
    app.elephantWalkUp = []
    for frame in range(3):
        elephantUpStep = elephantWalk.crop((100*frame, 300, 96+100*frame, 400))
        app.elephantWalkUp.append(elephantUpStep)

    #initializes the elephant state of the elephant moving as false
    app.elephantMoveLeft = True
    app.elephantMoveRight = False
    app.elephantMoveDown = False
    app.elephantMoveUp = False

    app.numFrames = 3
    app.spriteCounter = 0


#TREE

#WATER

#GRASS