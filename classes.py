from cmu_112_graphics import *

class Elephant(object):
    def __init__(self, app, lifeState, hunger, thirst, energy):
        #life stats of the elephant
        self.lifeState = lifeState
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy

        #determines what direction the elephant is moving
        #loads in the elephant image
        #Elephant PNG comes from https://opengameart.org/content/elephant-rework 
        #Under Creative Commons Attribution (CC BY) version 3.0
        #Copyright/Attribution Notice: 
        #Created by lawnjelly & Jordan Irwin (AntumDeluge)
        self.image = app.loadImage('images/elephant.png')
        self.elephantMoveLeft = False
        self.elephantMoveRight = False
        self.elephantMoveDown = False
        self.elephantMoveUp = False

        #initiates empty lists for the different directions of movement
        self.elephantWalkDown = []
        self.elephantWalkLeft = []
        self.elephantWalkRight = []
        self.elephantWalkUp = []
        self.elephantStill = ''

        self.numFrames = 3
        self.spriteCounter = 0

        self.imageHeight = 0
        self.imageWidth = 0
        self.imageX = app.width//2
        self.imageY = app.height//2
    
    def elephantStandStill(self, app):
        self.elephantStill = self.image
        sizeIm = self.image.size
        self.imageHeight = sizeIm[1]
        self.imageWidth = sizeIm[0]
        self.elephantStill = self.elephantStill.crop(((self.imageWidth//3, 0, 
                                    2*(self.imageWidth//3), 
                                    self.imageHeight//4)))
    
    def drawElephantStill(self, app, canvas):
        canvas.create_image(self.imageX, 
                            self.imageY,
                            image=ImageTk.PhotoImage(self.elephantStill))

    #Used below as starting basis, but rewrote most of it as my own code
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingFile
    #initializes the graphics for the elephant walking 
    def elephantWalking(self, app):
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
        canvas.create_image(self.imageX, self.imageY, 
                            image=ImageTk.PhotoImage(elephant))

class WateringHole(object):
    def __init__(self, app, waterLevel):
        self.waterLevel = waterLevel
        
        self.image = ''
        self.imageHeight = 0
        self.imageWidth = 0
        
    def waterImage(self, app):
        #loads the image
        #Water PNG comes from https://opengameart.org/content/lpc-animated-water-and-fire 
        #Under CC-BY 3.0
        #Created by Sharm
        self.image = app.loadImage("images/water.png")
        #finds the size of the image
        sizeIm = self.image.size
        self.imageHeight = sizeIm[1]
        self.imageWidth = sizeIm[0]
            
        self.image = self.image.crop((0, 
                                    self.imageHeight//4, 
                                    self.imageWidth//2,
                                    2*(self.imageHeight//3.3)))

    def drawWater(self, app, canvas):
        canvas.create_image(400, 400,image=ImageTk.PhotoImage(self.image))

class Tree(object):
    def __init__(self, leafLevel):
        self.leafLevel = leafLevel
        self.image = ''
        self.imageHeight = 0
        self.imageWidth = 0
    
    def treeImage(self, app):
        #Tree PNG comes from https://opengameart.org/content/savannah-tiles 
        #Under CC-BY-SA 3.0
        #Created by Modanung 
        self.image = app.loadImage("images/tree.png")
        sizeIm = self.image.size
        self.imageHeight = sizeIm[1]
        self.imageWidth = sizeIm[0]

    def drawTree(self, app, canvas):
        canvas.create_image(100, 100, image=ImageTk.PhotoImage(self.image))