from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *
from gamemode import *

#initiates the basic starting elements and sets the beginning game mode
def appStarted(app):
    #initiates the app features for different modes
    startScreenMode_initiate(app)
    helpScreenMode_initiate(app)
    gameMode_initiate(app)

    #game mode based on idea from Using Modes (aka Screens) Example on
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes 
    app.mode = "startScreenMode"
    

runApp(width = 400, height = 400)