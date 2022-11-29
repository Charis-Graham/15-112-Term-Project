from cmu_112_graphics import *
from graphics import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *

def appStarted(app):
    #initiate the startscreen
    startScreenInitiate(app)
    
    #initiates the help screen
    helpScreenInitiate(app)

    #draw grass
    grass(app)

    #draws a tree
    app.tree = Tree(100)
    app.tree.treeImage(app)

    #creates an element of class water
    app.water = WateringHole(app, 100)
    app.water.waterImage(app)

    #creates a player of class elephant
    app.player = Elephant(app, "baby", 100, 100, 100)
    #initializes the animations for walking and standing still
    app.player.elephantWalking(app)
    app.player.elephantStandStill(app)

runApp(width = 400, height = 400)