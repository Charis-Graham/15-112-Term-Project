#6:40 - 7:32pm
#7:45 - 8:46pm
#9:05 - 


from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *

def appStarted(app):
    #this function displays the elephant walking left
    elephantWalk(app)

def keyPressed(app, event):
    #controls the player moving
    playerMove(app, event)
    

def timerFired(app):
    #this runs through the sprite to have the elephant walk at a constant pace
    #this line is copied from timerFired in
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    app.spriteCounter = (1 + app.spriteCounter) % app.numFrames

def redrawAll(app, canvas):
    #draws the elephant walking
    drawElephantWalking(app, canvas)

runApp(width = 400, height = 400)