#6:40 - 7:32pm, 52 min
#7:45 - 8:46pm, 1 hr, 1 min
#9:05 - 10:00pm, 55 min
#1:30 - 1:48am
#1:50 - 


from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *

def appStarted(app):
    #this function displays the elephant walking left
    elephantWalk(app)
    tessellationGrassGround(app)
    tree(app)

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
    drawGround(app, canvas)
    drawElephantWalking(app, canvas)
    drawTree(app, canvas)

runApp(width = 400, height = 400)