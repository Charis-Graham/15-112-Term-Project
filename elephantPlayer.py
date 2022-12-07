from cmu_112_graphics import *
import random

#change elephant stats
def gameMode_changePlayerStats(app):
    app.player.travel += 1
    app.player.hunger = round(app.player.hunger + 0.1, 1)
    app.player.thirst = round(app.player.thirst + 0.2, 1)
    app.player.energy = round(app.player.energy - 0.1, 1)

#alters the positions of objects on the board
def gameMode_alterObjectPositions(app, direction, change):
    if direction == "Left":
        for tree in app.treeList:
            tree.X += change
        
        for water in app.waterList:
            water.X += change
        
        for elephant in app.elephantList:
            elephant.imageX += change

    elif direction == "Right":
        for tree in app.treeList:
            tree.X -= change
        
        for water in app.waterList:
            water.X -= change
        
        for elephant in app.elephantList:
            elephant.imageX -= change
    
    elif direction == "Down":
        for tree in app.treeList:
            tree.Y -= change
        
        for water in app.waterList:
            water.Y -= change
        
        for elephant in app.elephantList:
            elephant.imageY -= change

    elif direction == "Up":
        for tree in app.treeList:
            tree.Y += change
        
        for water in app.waterList:
            water.Y += change
        
        for elephant in app.elephantList:
            elephant.imageY += change

#keyboard controls for the player to move
def playerMove(app, event):
    #determines metric levels at each life stage
    if app.player.lifeState == "baby":
        if app.player.thirst > 40 or app.player.hunger > 30 or app.player.energy < 5:
            moveD = 5
        else:
            moveD = 10
    elif app.player.lifeState == "adult":
        if app.player.thirst > 70 or app.player.hunger > 65 or app.player.energy < 10:
            moveD = 5
        else:
            moveD = 10
    elif app.player.lifeState == "elder":
        if app.player.thirst > 100 or app.player.hunger > 115 or app.player.energy < 15:
            moveD = 5
        else:
            moveD = 10

    if event.key == "Left":
        app.player.elephantMoveLeft = True
        app.player.elephantMoveRight = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False

        #changes the position of the player
        app.player.imageX -= (moveD)
            
        #keeps the player on the board
        if app.player.imageX <= app.marginScroll:
            app.player.imageX = app.marginScroll
            gameMode_alterObjectPositions(app, "Left", moveD)
        
        #changes the player stats
        gameMode_changePlayerStats(app) 

        #checks if we do an illegal overlap
        for tree in app.treeList:
            if app.player.noPass(tree):
                app.player.imageX += moveD
    
        for water in app.waterList:
            if app.player.noPass(water):
                app.player.imageX += moveD
        

    elif event.key == "Right":
        app.player.elephantMoveRight = True
        app.player.elephantMoveLeft = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False

        app.player.imageX += moveD
        
        #keeps the player on the board
        if app.player.imageX >= app.width - app.marginScroll:
            app.player.imageX = app.width - app.marginScroll
            gameMode_alterObjectPositions(app, "Right", moveD)
        
        #changes the player stats
        gameMode_changePlayerStats(app) 

        #checks if we do an illegal overlap
        for tree in app.treeList:
            if app.player.noPass(tree):
                app.player.imageX -= moveD
    
        for water in app.waterList:
            if app.player.noPass(water):
                app.player.imageX -= moveD

    elif (event.key == "Down"):
        app.player.elephantMoveDown = True
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False
        app.player.elephantMoveUp = False

        #moves the player
        app.player.imageY += moveD
        
        #keeps the player on the board
        if app.player.imageY >= app.height - app.marginScroll:
            app.player.imageY = app.height - app.marginScroll
            gameMode_alterObjectPositions(app, "Down", moveD)
        
        #changes the player stats
        gameMode_changePlayerStats(app)   

        #checks if we do an illegal overlap
        for tree in app.treeList:
            if app.player.noPass(tree):
                app.player.imageY -= moveD
    
        for water in app.waterList:
            if app.player.noPass(water):
                app.player.imageY -= moveD 

    elif (event.key == "Up"):
        app.player.elephantMoveUp = True
        app.player.elephantMoveDown = False
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False

        #moves the player
        app.player.imageY -= moveD

        if app.player.imageY <= app.marginScroll:
            app.player.imageY = app.marginScroll
            gameMode_alterObjectPositions(app, "Up", moveD)
        
        #changes the player stats
        gameMode_changePlayerStats(app)

        #checks if we do an illegal overlap
        for tree in app.treeList:
            if app.player.noPass(tree):
                app.player.imageX += moveD
    
        for water in app.waterList:
            if app.player.noPass(water):
                app.player.imageX += moveD


#defines what happens if the player is not moving
def playerStill(app, event):
    if event.key in ["Right", "Left", "Up", "Down"]:
        app.player.elephantMoveLeft = False
        app.player.elephantMoveRight = False
        app.player.elephantMoveDown = False
        app.player.elephantMoveUp = False

#creates the conditions for death
def gameMode_death(app):
    if app.isRunNormal == True:
        if ((app.player.hunger > 60 or 
            app.player.thirst > 55 or 
            app.player.energy < 2) 
            and app.player.lifeState == "baby"):
            app.mode = "endMode"
        elif ((app.player.hunger > 100 or 
            app.player.thirst > 95 or 
            app.player.energy < 5)
            and app.player.lifeState == "adult"):
            app.mode = "endMode"
        elif ((app.player.hunger > 160 or 
            app.player.thirst > 155 or 
            app.player.energy < 7) 
            and app.player.lifeState == "elder"):
            app.mode = "endMode"