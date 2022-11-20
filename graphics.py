from cmu_112_graphics import *
import random

#TREE
def tree(app):
    app.treeImage = app.loadImage("images/tree.png")

def drawTree(app, canvas):
    canvas.create_image(100, 100,image=ImageTk.PhotoImage(app.treeImage))

#WATER
def water(app):
    app.waterImage = app.loadImage("images/water.png")
    app.waterImage = app.waterImage.crop((0, 
                                        app.height//5.7, 
                                        app.width//4.7,
                                        2.2*(app.height//5.7)))




#GRASS
def tessellationGrassGround(app):
    app.grass = []
    for panel in range(1, 6):
        app.grassImage = app.loadImage(f"images/grass/grass{panel}.jpg")
        app.grass.append(app.grassImage)

def drawGround(app, canvas):
    for dw in range(0, app.width, 20):
        for dh in range(0, app.height, 20):
            randInd = random.randint(2, 2)
            canvas.create_image(dw,dh,image=ImageTk.PhotoImage(app.grass[randInd]))