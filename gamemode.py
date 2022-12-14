from cmu_112_graphics import *
from boardGeneration import *
from elephantPlayer import *
from classes import *
from startscreen import *
from helpscreen import *
from endScreen import *
from challenges import *

#All instance of image.size is based on this example
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#imageSize

#initiates the game mode 
def gameMode_initiate(app):

    #create a margin for side scrolling
    app.marginScroll = 100

    #keeps track of which challenge the player is on
    app.challengeCount = 1
    app.elephantIntersectCount = 0
    app.elephantWaterShared = 0
    app.elephantFoodShared = 0
    app.elephantIntersected = []
    app.elephantFed = []
    app.elephantWater = []
    app.deadElephants = []
    app.deadElephant = Elephant(app, "baby", 0, 0, 0, 0, 0)
    app.timeWait = 0

    #used in timer fired to know when night is
    app.nightCount = 0
    app.isNight = False

    app.walkCount = 0

    #toggle for all game-play function for demo
    app.isRunNormal = True

    #draw grass
    gameMode_grass(app)

    #creates a player of class elephant
    app.player = Elephant(app, "baby", 0, 0, 20, 
                        app.width//2, app.height//2)

    #initializes the animations for walking and standing still
    app.player.elephantWalking(app)
    app.player.elephantStandStill(app)

    #makes the gameboard and challenges elements
    gameMode_makeGameBoard(app)
    gameMode_challenges(app)

    #initializes night animation
    gameMode_night(app)

#controls the available keyboard interactions
def gameMode_keyPressed(app, event):
    #controls the player moving
    playerMove(app, event)

    #what happens if the elephant drinks water
    if event.key == "d":
        for water in app.waterList:
            if app.player.intersectsObject(water):
                water.goMuddy(app)
                if app.player.thirst > 10:
                    water.waterLevel -= 10
                    app.player.thirst -= 10
       
    #allows the elephant eats    
    elif event.key == "e":
        for tree in app.treeList:
            if app.player.intersectsObject(tree):
                tree.goLeaves(app)
                if app.player.hunger > 10:
                    tree.leafLevel -= 10
                    app.player.hunger -= 10
    
    #allows the elephant to share food
    elif event.key == "f":
        for elephant in app.elephantList:
            if app.player.intersectsObject(elephant):
                elephant.hunger += 1
                app.player.shareHunger()
    
    #allows the elephant to share water
    elif event.key == "w":
        for elephant in app.elephantList:
            if app.player.intersectsObject(elephant):
                elephant.thirst += 1
                app.player.shareWater()
    
    #allows for sleep
    elif event.key == "s" and app.isNight == True:
        app.player.energy += 5
        
    #gets the help screen
    elif event.key == "h":
        app.mode = "helpScreenMode"
    
    #allows for challenge demonstration by turning off death mechanics
    elif event.key == "o":
        app.isRunNormal = not app.isRunNormal

#makes the elephant still when not moving
def gameMode_keyReleased(app, event):
    #controls what happens when the elephant is still
    playerStill(app, event)


#contols the time sensitive elements of game play
def gameMode_timerFired(app):
    #this runs through the sprite to have the elephant walk at a constant pace
    #this line is copied from timerFired in
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#spritesheetsWithCropping
    app.player.spriteCounter = (1 + app.player.spriteCounter) % app.player.numFrames

    #checks if the death state is matched
    gameMode_death(app)

    #keeps track of elements for challenges
    gameMode_elephantIntersectCount(app)
    gameMode_checkSharedWater(app)
    gameMode_checkSharedFood(app)
    gameMode_challenge(app)
    gameMode_checkDeathMet(app)

    if app.player.lifeState == "elder" and len(app.deadElephants) == 0:
        app.deadElephant = app.elephantList[random.randint(0, 6)]
        app.deadElephant.status = "dead"
        app.deadElephants.append(app.deadElephant)

    #keeps the start screen from being resized
    if (app.width != app.startScreen.size[0] 
        or app.height != app.startScreen.size[1]):
        #comes from examining cmu_112_graphics.py line 292
        app.setSize(app.startScreen.size[0], app.startScreen.size[1])

    #deals with logic of night existing
    app.nightCount += 1
    if app.nightCount > 100 and app.nightCount < 125:
        app.isNight = True
    elif app.nightCount >= 125:
        app.isNight = False
        app.nightCount = 0
    
    #stop the player from spamming walking and overloading the system
    if app.walkCount > 15:
        app.player.elephantMoveLeft = False 
        app.player.elephantMoveDown = False
        app.player.elephantMoveRight = False
        app.player.elephantMoveUp = False
        app.walkCount = 0
    else:
        app.walkCount += 1

#draws the board
def gameMode_redrawAll(app, canvas):
    #draws the ground
    gameMode_drawGround(app, canvas)

    #generates and draws the game board
    gameMode_drawGameBoard(app, canvas)

    #draws the player elephant
    if (app.player.elephantMoveLeft == False and 
        app.player.elephantMoveDown == False and
        app.player.elephantMoveRight == False and 
        app.player.elephantMoveUp == False):
        app.player.drawElephantStill(app, canvas)
    else:
        app.player.drawElephantWalk(app, canvas)

    #makes stat board
    gameMode_statBoard(app, canvas)

    #initiates the challenges
    gameMode_drawChallenge(app, canvas)
    gameMode_challengeProgression(app, canvas)

    #draws night
    gameMode_drawNight(app, canvas)