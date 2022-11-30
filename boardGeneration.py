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
def gameMode_createRandomStats(app):
    X = random.randint(0, app.width)
    Y = random.randint(0, app.height)
    level = random.randint(70, 100)
    return X, Y, level

#creates a game board with 5 random generated trees and 5 randomly generated 
#waterholes
def gameMode_makeGameBoard(app):
    #creates five randomly spawned trees
    tree1X, tree1Y, tree1Leaf = gameMode_createRandomStats(app)
    app.tree1 = Tree(tree1Leaf, tree1X, tree1Y)
    app.tree1.treeImage(app)

    tree2X, tree2Y, tree2Leaf = gameMode_createRandomStats(app)
    app.tree2 = Tree(tree2Leaf, tree2X, tree2Y)
    app.tree2.treeImage(app)

    tree3X, tree3Y, tree3Leaf = gameMode_createRandomStats(app)
    app.tree3 = Tree(tree3Leaf, tree3X, tree3Y)
    app.tree3.treeImage(app)

    tree4X, tree4Y, tree4Leaf = gameMode_createRandomStats(app)
    app.tree4 = Tree(tree4Leaf, tree4X, tree4Y)
    app.tree4.treeImage(app)

    tree5X, tree5Y, tree5Leaf = gameMode_createRandomStats(app)
    app.tree5 = Tree(tree5Leaf, tree5X, tree5Y)
    app.tree5.treeImage(app)

    #creates 5 randomly spawned watering holes
    tree1X, tree1Y, tree1Leaf = gameMode_createRandomStats(app)
    app.water1 = WateringHole(tree1Leaf, tree1X, tree1Y)
    app.water1.waterImage(app)

    tree2X, tree2Y, tree2Leaf = gameMode_createRandomStats(app)
    app.water2 = WateringHole(tree2Leaf, tree2X, tree2Y)
    app.water2.waterImage(app)

    tree3X, tree3Y, tree3Leaf = gameMode_createRandomStats(app)
    app.water3 = WateringHole(tree3Leaf, tree3X, tree3Y)
    app.water3.waterImage(app)

    tree4X, tree4Y, tree4Leaf = gameMode_createRandomStats(app)
    app.water4 = WateringHole(tree4Leaf, tree4X, tree4Y)
    app.water4.waterImage(app)

    tree5X, tree5Y, tree5Leaf = gameMode_createRandomStats(app)
    app.water5 = WateringHole(tree5Leaf, tree5X, tree5Y)
    app.water5.waterImage(app)
    
#draws the randomly spawned background
def gameMode_drawGameBoard(app, canvas):
    #draws trees
    app.tree1.drawTree(canvas)
    app.tree2.drawTree(canvas)
    app.tree3.drawTree(canvas)
    app.tree4.drawTree(canvas)
    app.tree5.drawTree(canvas)

    #draws water
    app.water1.drawWater(canvas)
    app.water2.drawWater(canvas)
    app.water3.drawWater(canvas)
    app.water4.drawWater(canvas)
    app.water5.drawWater(canvas)

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
                    