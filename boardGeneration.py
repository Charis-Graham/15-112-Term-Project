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
def gameMode_makeGameBoard(app):
    app.resourcePlacement = {}
    for treeNum in range(5):
        #random placements
        treeX = random.randint(0, app.width)
        treeY = random.randint(0, app.height)
        treeLeaf = random.randint(70, 100)
        tree = Tree(treeLeaf, treeX, treeY)
        app.resourcePlacement.add(tree)

def gameMode_drawGameBoard(app, canvas):
    for item in app.resourcePlacement:
        if isinstance(item, Tree):
            item.drawTree(canvas)
        elif isinstance(item, WateringHole):
            item.drawWater(canvas)

    
def gameMode_statBoard(app, canvas):
    canvas.create_rectangle(10, 10, 150, 250, fill="white", 
                            outline="black", width =5)
    canvas.create_text(80, 50, text = f"Hunger: {app.player.hunger}", 
                        fill = "black", font='Helvetica 20 bold')
    canvas.create_text(80, 100, text = f"Thirst: {app.player.thirst}",
                        fill = "black", font='Helvetica 20 bold')
    canvas.create_text(80, 150, text = f"Energy: {app.player.energy}",
                        fill = "black", font='Helvetica 20 bold')
    canvas.create_text(80, 200, text = f"Age: {app.player.lifeState}",
                        fill = "black", font='Helvetica 20 bold')
                    