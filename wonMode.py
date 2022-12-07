from cmu_112_graphics import *
from startscreen import *
from helpscreen import *
from gamemode import *
from endScreen import *

#initiates variables for the functions
def wonMode_initiate(app):
    app.mode = 'wonMode'
    #image taken from
    #https://www.reddit.com/r/pics/comments/is1xq/happy_elephant_is_happy/
    #Posted by u/PuppyBreath (the username given with the post)
    #and modified using google draw
    app.winScreen = app.loadImage('images/winScreen.png')
    sizeOfStart = app.winScreen.size
    app.winwidth = sizeOfStart[0]
    app.winheight = sizeOfStart[1]
    app.winScreen = app.scaleImage(app.winScreen, 2/3)

#draws the help screen
def wonMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.winScreen))

#keeps the helpscreen from being resized
def wonMode_timerFired(app):
    if (app.width != app.winScreen.size[0] 
        or app.height != app.winScreen.size[1]):
        app.setSize(app.winScreen.size[0], app.winScreen.size[1])