from cmu_112_graphics import *

#creates the start screen variables
def startScreenMode_initiate(app):
    app.mode = 'startScreenMode'
    #image taken from
    #https://www.livescience.com/27320-elephants.html
    #and modified using google draw
    app.startScreen = app.loadImage('images/startScreen.png')
    sizeOfStart = app.startScreen.size
    app.width = sizeOfStart[0]
    app.height = sizeOfStart[1]
    app.setSize(app.width, app.height)

#draws the start screen
def startScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.startScreen))

#allows to go to help screen or begin game
def startScreenMode_keyPressed(app, event):
    if event.key == "s":
        app.mode = "gameMode"
    elif event.key == "h":
        app.mode = "helpScreenMode"

#keeps the start screen from being resized
#should be removed later
def startScreenMode_timerFired(app):
    if (app.width != app.startScreen.size[0] 
        or app.height != app.startScreen.size[1]):
        app.setSize(app.startScreen.size[0], app.startScreen.size[1])