from cmu_112_graphics import *
from classes import *
import random

#GRASS BACKGROUND
def gameMode_grass(app):
    #draws the ground
    #Grass PNGs come from https://opengameart.org/content/grass-texture-pack
    #Under CC0
    #Created by Proxy Games
    app.grassImage = app.loadImage("images/grass/grass3.jpg")
    app.grassImage = app.scaleImage(app.grassImage, 12)
    sizeIm = app.grassImage.size
    app.grassImageHeight = sizeIm[1]
    app.grassImageWidth = sizeIm[0]

#draws the background of the game
def gameMode_drawGround(app, canvas):
    imageGrass = ImageTk.PhotoImage(app.grassImage)
    for dw in range(0, app.width, 384):
        for dh in range(0, app.height, 384):
            canvas.create_image(dw, dh,
                                image = imageGrass)

#GAME BOARD DICTIONARY
def makeGameBoard(app):
    resourcePlacement = {}
    for treeNum in range(5):
        #randome placements
        treeX = random.randint(0, app.width)
        treeY = random.randint(0, app.height)
        treeLeaf = random.randint(70, 100)
        resourcePlacement[f"tree{treeNum}"] = Tree(treeLeaf, treeX, treeY)
    
def statBoard(app, canvas):
    pass