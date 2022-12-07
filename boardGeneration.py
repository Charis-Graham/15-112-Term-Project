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

    #makes the random coordinates for the water and tree objects on the board
    app.boardXCoords = ([random.randint(x, x+200) for x in range(-app.width,0, 250)]+
                    [random.randint(x, x+200) for x in range(0, app.width, 250)]+
                    [random.randint(x, x+200) for x in range(app.width, 2*app.width, 250)])
    app.boardYCoords = [random.randint(100, app.height-150) for y in range(16)]
    app.boardTreeLevels = [random.randint(70,100) for i in range(20)]

#draws the background of the game
def gameMode_drawGround(app, canvas):
    imageGrass = ImageTk.PhotoImage(app.grassImage)
    for dw in range(-app.width, 2*app.width, 640):
        for dh in range(-app.height//2, app.height+app.height//2, 640):
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

#makes the elephants in the herd
def gameMode_elephants(app):
    coords = []
    while len(coords) < 7:
        rand = random.randint(0, 15)
        if rand not in coords:
            coords.append(rand)

    app.elephantList = [
                    Elephant(app, "mom", 0, 0, 10, 
                        200, 
                        200),
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
    
    if app.player.lifeState == "baby":
        app.elephantList[0].drawElephantStill(app, canvas)
    elif app.player.lifeState == "adult" or app.player.lifeState == "elder":
        for item in app.elephantList:
            item.drawElephantStill(app, canvas)

#CHALLENGES
#creates the popups for the challenges
def gameMode_challenges(app):
    #Images created using Google Draw
    app.challenge1 = app.loadImage("images/challenge1.png")
    app.challenge2 = app.loadImage("images/challenge2.png")
    app.challenge3 = app.loadImage("images/challenge3.png")
    app.challenge4 = app.loadImage("images/challenge4.png")
    app.challenge5 = app.loadImage("images/challenge5.png")
    app.challenge1 = app.scaleImage(app.challenge1, 0.75)
    app.challenge2 = app.scaleImage(app.challenge2, 0.75)
    app.challenge3 = app.scaleImage(app.challenge3, 0.75)
    app.challenge4 = app.scaleImage(app.challenge4, 0.75)
    app.challenge5 = app.scaleImage(app.challenge5, 0.75)

#draws the challenge popups
def gameMode_drawChallenge(app, canvas):
    if app.challengeCount == 1:
        canvas.create_image(500, app.height-100, image=ImageTk.PhotoImage(app.challenge1))
    elif app.challengeCount == 2:
        canvas.create_image(500, app.height-100, image=ImageTk.PhotoImage(app.challenge2))
    elif app.challengeCount == 3:
        canvas.create_image(500, app.height-100, image=ImageTk.PhotoImage(app.challenge3))
    elif app.challengeCount == 4:
        canvas.create_image(500, app.height-100, image=ImageTk.PhotoImage(app.challenge4))
    elif app.challengeCount == 5:
        canvas.create_image(500, app.height-100, image=ImageTk.PhotoImage(app.challenge5))
 
#makes the statboard on the game
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

#keeps track of the challenge progression to show the player how far they are on a challenge
def gameMode_challengeProgression(app, canvas):
    if app.challengeCount == 1:
        status = "No"
        metric = "Found:"
    elif app.challengeCount == 2:
        status = app.elephantIntersectCount
        metric = "Met:"
    elif app.challengeCount == 3:
        status = app.elephantFoodShared
        metric = "Shared:"
    elif app.challengeCount == 4:
        status = app.elephantWaterShared
        metric = "Shared:"
    elif app.challengeCount == 5:
        metric = "Timer:"
        if app.timeWait == 0:
            status = 0
        elif app.timeWait < 10:
            status = 1
        elif app.timeWait < 20:
            status = 2
        elif app.timeWait < 30:
            status = 3
        elif app.timeWait < 40:
            status = 4
        elif app.timeWait <= 50:
            status = 5
        else:
            status = app.timeWait
    canvas.create_text(855, 745, text = f"{metric} {status}",
                        fill = "black", font='Helvetica 20 bold') 