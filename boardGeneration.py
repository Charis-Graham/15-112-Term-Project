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
    app.grassImage = app.scaleImage(app.grassImage, 20)
    sizeIm = app.grassImage.size
    app.grassImageHeight = sizeIm[1]
    app.grassImageWidth = sizeIm[0]
    print(app.grassImageHeight, app.grassImageWidth)

    #makes the random coordinates for the water and tree objects on the board
    app.boardXCoords = ([random.randint(x, x+200) for x in range(-app.width,0, 250)]+
                    [random.randint(x, x+200) for x in range(0, app.width, 250)]+
                    [random.randint(x, x+200) for x in range(app.width, 2*app.width, 250)])
    app.boardYCoords = [random.randint(0, app.height) for y in range(16)]
    app.boardTreeLevels = [random.randint(70,100) for i in range(20)]

#draws the background of the game
def gameMode_drawGround(app, canvas):
    imageGrass = ImageTk.PhotoImage(app.grassImage)
    for dw in range(-app.width, 2*app.width, 640):
        for dh in range(0, app.height, 640):
            canvas.create_image(dw, dh,
                                image = imageGrass)

#GAME BOARD DICTIONARY
#makes tree objects
def gameMode_treeObjects(app):
    app.treeList = [Tree(app, app.boardTreeLevels[0], 
                        app.boardXCoords[0], app.boardYCoords[0]),
                    Tree(app, app.boardTreeLevels[2], 
                        app.boardXCoords[2], app.boardYCoords[2]),
                    Tree(app, app.boardTreeLevels[3], 
                        app.boardXCoords[3], app.boardYCoords[3]),
                    Tree(app, app.boardTreeLevels[7], 
                        app.boardXCoords[7], app.boardYCoords[7]),
                    Tree(app, app.boardTreeLevels[8],
                        app.boardXCoords[8], app.boardYCoords[8]),
                    Tree(app, app.boardTreeLevels[10], 
                        app.boardXCoords[10], app.boardYCoords[10]),
                    Tree(app, app.boardTreeLevels[11],
                        app.boardXCoords[11], app.boardYCoords[11]),
                    Tree(app, app.boardTreeLevels[13],
                        app.boardXCoords[13], app.boardYCoords[13])]

#makes water objects
def gameMode_waterObjects(app):
    app.waterList = [
                    WateringHole(app, app.boardTreeLevels[1], 
                        app.boardXCoords[1], app.boardYCoords[1]),
                    WateringHole(app, app.boardTreeLevels[4],
                        app.boardXCoords[4], app.boardYCoords[4]),
                    WateringHole(app, app.boardTreeLevels[5], 
                        app.boardXCoords[5], app.boardYCoords[5]),
                    WateringHole(app, app.boardTreeLevels[6], 
                        app.boardXCoords[6], app.boardYCoords[6]),
                    WateringHole(app, app.boardTreeLevels[9], 
                        app.boardXCoords[9], app.boardYCoords[9]),
                    WateringHole(app, app.boardTreeLevels[12],
                        app.boardXCoords[12], app.boardYCoords[12]),
                    WateringHole(app, app.boardTreeLevels[14], 
                        app.boardXCoords[14], app.boardYCoords[14]),
                    WateringHole(app, app.boardTreeLevels[15], 
                        app.boardXCoords[15], app.boardYCoords[15])]


def gameMode_elephants(app):
    coords = []
    while len(coords) < 7:
        rand = random.randint(0, 15)
        if rand not in coords:
            coords.append(rand)
    print(coords)

    app.elephantList = [
                    Elephant(app, "mom", 0, 0, 10, 
                        app.boardXCoords[coords[0]]+30, 
                        app.boardYCoords[coords[0]]+30),
                    Elephant(app, "adult", 0, 0, 10, 
                        app.boardXCoords[coords[1]]+30, 
                        app.boardYCoords[coords[1]]+30),
                    Elephant(app, "adult", 0, 0, 10,
                        app.boardXCoords[coords[2]]+30, 
                        app.boardYCoords[coords[2]]+30),
                    Elephant(app, "adult", 0, 0, 10,
                        app.boardXCoords[coords[3]]+30, 
                        app.boardYCoords[coords[3]]+30),
                    Elephant(app, "adult", 0, 0, 10, 
                        app.boardXCoords[coords[4]]+30, 
                        app.boardYCoords[coords[4]]+30),
                    Elephant(app, "adult", 0, 0, 10, 
                        app.boardXCoords[coords[5]]+30, 
                        app.boardYCoords[coords[5]]+30),
                    Elephant(app, "adult", 0, 0, 10, 
                        app.boardXCoords[coords[6]]+30, 
                        app.boardYCoords[coords[6]]+30)]
    
    for elephant in app.elephantList:
        elephant.elephantStandStill(app)

#creates a game board with 5 random generated trees and 5 randomly generated 
#waterholes
def gameMode_makeGameBoard(app):
    #creates 15 randomly spawned trees
    gameMode_treeObjects(app)
    gameMode_waterObjects(app)
    gameMode_elephants(app)
    
#draws the randomly spawned background
def gameMode_drawGameBoard(app, canvas):
    for item in app.treeList:
        item.drawTree(canvas)
    
    for item in app.waterList:
        item.drawWater(canvas)
    
    for item in app.elephantList:
        item.drawElephantStill(app, canvas)


def gameMode_statBoard(app, canvas):
    canvas.create_rectangle(10, 10, 150, 250, fill="white", 
                            outline="black", width =5)
    canvas.create_text(80, 50, text = f"Hunger: {round(app.player.hunger,1)}", 
                        fill = "black", font='Helvetica 20 bold')
    canvas.create_text(80, 100, text = f"Thirst: {round(app.player.thirst,1)}",
                        fill = "black", font='Helvetica 20 bold')
    canvas.create_text(80, 150, text = f"Energy: {round(app.player.energy,1)}",
                        fill = "black", font='Helvetica 20 bold')
    canvas.create_text(80, 200, text = f"Age: {app.player.lifeState}",
                        fill = "black", font='Helvetica 20 bold')            