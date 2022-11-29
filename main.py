from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *
from gamemode import *

def appStarted(app):
    #initiates the app features for different modes
    startScreenMode_initiate(app)
    helpScreenMode_initiate(app)
    gameMode_initiate(app)

    app.mode = "startScreenMode"

runApp(width = 400, height = 400)