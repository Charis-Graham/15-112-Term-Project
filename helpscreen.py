from cmu_112_graphics import *

#All instance of app.loadImage, app.scaleImage, canvas.create_image are based on 
#instructions from/examples given in
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingFile

#All instance of image.size is based on this example
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#imageSize


#initiates variables for the functions
def helpScreenMode_initiate(app):
    app.mode = 'helpScreenMode'
    #image taken from
    #https://www.vecteezy.com/vector-art/4904919-green-leaf-background-illustration-vector
    #created by mitasukmaa
    #and modified using google draw
    app.helpScreen = app.loadImage('images/helpScreen.png')
    app.helpScreen = app.scaleImage(app.helpScreen, 2/3)
    sizeOfStart = app.helpScreen.size
    app.helpwidth = sizeOfStart[0]
    app.helpheight = sizeOfStart[1]

#draws the help screen
def helpScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.helpScreen))

#allows to go to game mode
def helpScreenMode_keyPressed(app, event):
    if event.key == "g":
        app.mode = "gameMode"

#keeps the helpscreen from being resized
def helpScreenMode_timerFired(app):
    if (app.width != app.helpScreen.size[0] 
        or app.height != app.helpScreen.size[1]):
        #comes from examining cmu_112_graphics.py line 292
        app.setSize(app.helpScreen.size[0], app.helpScreen.size[1])