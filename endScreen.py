from cmu_112_graphics import *
from startscreen import *
from helpscreen import *
from gamemode import *
from endScreen import *

#All instance of app.loadImage, app.scaleImage, canvas.create_image are based on 
#instructions from/examples given in
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingFile

#All instance of image.size is based on this example
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#imageSize

#initiates variables for the functions
def endMode_initiate(app):
    app.mode = 'endMode'
    #image taken from
    #https://www.vecteezy.com/vector-art/4904919-green-leaf-background-illustration-vector
    #created by mitasukmaa
    #and modified using google draw
    app.endScreen = app.loadImage('images/endScreen.png')
    sizeOfStart = app.endScreen.size
    app.endwidth = sizeOfStart[0]
    app.endheight = sizeOfStart[1]
    app.endScreen = app.scaleImage(app.endScreen, 4/5)

#draws the help screen
def endMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.endScreen))

#keeps the helpscreen from being resized
#will probably be removed later
def endMode_timerFired(app):
    if (app.width != app.helpScreen.size[0] 
        or app.height != app.helpScreen.size[1]):
        #comes from examining cmu_112_graphics.py line 292
        app.setSize(app.helpScreen.size[0], app.helpScreen.size[1])