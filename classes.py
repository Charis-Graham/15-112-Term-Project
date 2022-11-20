from cmu_112_graphics import *
import random
from graphics import *

class Elephant(object):
    def __init__(self, lifeState, hunger, thirst, energy):
        #life stats of the elephant
        self.lifeState = lifeState
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy

        #determines what direction the elephant is moving
        self.image = ''
        self.elephantMoveLeft = False
        self.elephantMoveRight = False
        self.elephantMoveDown = False
        self.elephantMoveUp = True


        #initiates empty lists for the different directions of movement
        self.elephantWalkDown = []
        self.elephantWalkLeft = []
        self.elephantWalkRight = []
        self.elephantWalkUp = []

        self.numFrames = 3
        self.spriteCounter = 0

        self.imageHeight = 0
        self.imageWidth = 0
    
    #Used below as starting basis, but rewrote most of it as my own code
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingFile
    #initializes the graphics for the elephant walking 
    def elephantWalking(self, app):
         #loads in the elephant image
        self.image = app.loadImage('images/elephant.png')
        elephantWalk = self.image

        sizeIm = self.image.size
        self.imageHeight = sizeIm[1]
        self.imageWidth = sizeIm[0]

        #builds the elephant walking down animation
        for frame in range(3):
            elephantDownStep = elephantWalk.crop((self.imageWidth//3*frame, 0, 
                                    self.imageWidth//3+self.imageWidth//3*frame, 
                                    self.imageHeight//4))
            self.elephantWalkDown.append(elephantDownStep)

        #builds the elephant walking left animation
        for frame in range(3):
            elephantStepLeft = elephantWalk.crop((self.imageWidth//3*frame, 
                                    self.imageHeight//4,
                                    self.imageWidth//3+self.imageWidth//3*frame, 
                                    self.imageHeight//2))
            self.elephantWalkLeft.append(elephantStepLeft)
        
        #builds the elephant walking right animation
        for frame in range(3):
            elephantStepRight = elephantWalk.crop((self.imageWidth//3*frame, 
                                    self.imageHeight//2, 
                                    self.imageWidth//3+self.imageWidth//3*frame,
                                    3*(self.imageHeight//4)))
            self.elephantWalkRight.append(elephantStepRight)

        #builds the elephant walking up animation
        for frame in range(3):
            elephantUpStep = elephantWalk.crop((self.imageWidth//3*frame, 
                                    3*(self.imageHeight//4), 
                                    self.imageWidth//3+self.imageWidth//3*frame, 
                                    self.imageHeight))
            self.elephantWalkUp.append(elephantUpStep)

    #draw the elephant walking around
    def drawElephantWalk(self, app, canvas):
        if self.elephantMoveLeft == True:
            elephant = self.elephantWalkLeft[self.spriteCounter]
        elif self.elephantMoveDown == True:
            elephant = self.elephantWalkDown[self.spriteCounter]
        elif self.elephantMoveUp == True:
            elephant = self.elephantWalkUp[self.spriteCounter]
        elif self.elephantMoveRight == True:
            elephant = self.elephantWalkRight[self.spriteCounter]
        #this puts the position of the elephant via the top-left corner
        canvas.create_image(app.width//2, app.height//2, 
                            image=ImageTk.PhotoImage(elephant))

class WateringHole(object):
    def __init__(self, app, waterLevel):
        self.waterLevel = waterLevel
        self.image = app.loadImage("images/water.png")
        self.waterImage = self.image.crop((0, 
                                        app.height//5.7, 
                                        app.width//4.7,
                                        2.2*(app.height//5.7)))

    def drawWater(self, app, canvas):
        canvas.create_image(300, 300,image=ImageTk.PhotoImage(self.waterImage))

class Tree(object):
    def __init__(self, leafLevel, image):
        self.leafLevel = leafLevel
        self.image = image