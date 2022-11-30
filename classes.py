from cmu_112_graphics import *
from elephantPlayer import *
from graphics import *
import random

#creates the elephant class
class Elephant(object):
    def __init__(self, app, lifeState, hunger, thirst, energy, x, y):
        #life stats of the elephant
        self.lifeState = lifeState
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.travel = 0

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
        self.stillImageHeight = 0
        self.stillImageWidth = 0
        self.imageX = x
        self.imageY = y
    
    def elephantStandStill(self, app):
        self.elephantStill = self.image
        sizeIm = self.image.size
        self.imageHeight = sizeIm[1]
        self.imageWidth = sizeIm[0]
        self.elephantStill = self.elephantStill.crop(((self.imageWidth//3, 0, 
                                    2*(self.imageWidth//3), 
                                    self.imageHeight//4)))
        stillSize = self.elephantStill.size
        self.stillImageHeight = stillSize[1]
        self.stillImageWidth = stillSize[0]
    
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

    def elephantWeaken(self):
        healthMetrics = [self.hunger, self.thirst, self.energy]
        if (self.travel >= 5 and healthMetrics[0] > 0 or 
                healthMetrics[1] > 0 or healthMetrics[2] > 0):
            healthMetrics[random.randint(0,2)] -= 5
        else:
            self.elephantMoveLeft = False
            self.elephantMoveRight = False
            self.elephantMoveDown = False
            self.elephantMoveUp = False
    
    #Copied from game object class developed in Lecture 1
    #Tuesday, November 22, 2022 by Pat Virtue
    #which was based on side scroller #3 on 
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
    def getBounds(self):
    # returns absolute bounds, not taking xScroll into account
        (x0, y1) = (self.imageX, self.stillImageHeight/2 - self.imageY)
        (x1, y0) = (x0 + self.stillImageWidth, y1 - self.stillImageHeight)
        print(x0, y0, x1, y1)
        return x0, y0, x1, y1

    def intersectsObject(self, other):
        # return l2<=r1 and t2<=b1 and l1<=r2 and t1<=b2
        (ax0, ay0, ax1, ay1) = self.getBounds()
        (bx0, by0, bx1, by1) = other.getBounds()
        return ((ax1 >= bx0) and (bx1 >= ax0) and
                (ay1 >= by0) and (by1 >= ay0))
                
#creates the watering hole class
class WateringHole(object):
    def __init__(self, waterLevel, x, y):
        self.waterLevel = waterLevel
        self.image = ''
        self.imageHeight = 0
        self.imageWidth = 0
        self.X, self.Y = x, y
        
    #crops the water image
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

    #generates a random new coordinate for the water
    def randomWaterSpawn(self, app):
        self.X = random.randint(0, app.width)
        self.Y = random.randint(0, app.height)
            
    #draws the water on the canvas
    def drawWater(self, app, canvas):
        canvas.create_image(self.X, self.Y, image=ImageTk.PhotoImage(self.image))

    #water low image
    def goMuddy(self, app):
        #loads the image
        #Water PNG comes from https://opengameart.org/content/lpc-animated-water-and-fire 
        #Under CC-BY 3.0
        #Created by Sharm
        #Modified by me with recoloring
        if self.waterLevel > 50:
            self.image = app.loadImage("images/waterDrunk.png")
        elif self.waterLevel > 0:
            self.image = app.loadImage("images/waterDry.png")

    #Copied from game object class developed in Lecture 1
    #Tuesday, November 22, 2022 by Pat Virtue
    #which was based on side scroller #3 on 
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
    def getBounds(self):
    # returns absolute bounds, not taking xScroll into account
        (x0, y1) = (self.X, self.imageHeight/2 - self.Y)
        (x1, y0) = (x0 + self.imageWidth, y1 - self.imageHeight)
        return x0, y0, x1, y1

#creates the tree object
class Tree(object):
    def __init__(self, leafLevel, x, y):
        self.leafLevel = leafLevel
        self.image = ''
        self.imageHeight = 0
        self.imageWidth = 0
        self.X, self.Y = x, y
    
    #crops the tree image
    def treeImage(self, app):
        #Tree PNG comes from https://opengameart.org/content/savannah-tiles 
        #Under CC-BY-SA 3.0
        #Created by Modanung 
        self.image = app.loadImage("images/tree.png")
        sizeIm = self.image.size
        self.imageHeight = sizeIm[1]
        self.imageWidth = sizeIm[0]

    #draws the tree image
    def drawTree(self, app, canvas):
        canvas.create_image(self.X, self.Y, image=ImageTk.PhotoImage(self.image))
    
    #allows for random placement of the image
    def randomTreeSpawn(self, app):
        self.X = random.randint(0, app.width)
        self.Y = random.randint(0, app.height)
    
    #image of tree being stripped
    def goLeaves(self, app):
        #Tree PNGs comes from https://opengameart.org/content/savannah-tiles 
        #Under CC-BY-SA 3.0
        #Created by Modanung 
        #Modified by me with recoloring
        if self.leafLevel > 50:
            self.image = app.loadImage("images/treeEaten.png")
        elif self.leafLevel > 0:
            self.image = app.loadImage("images/treeStripped.png")
    
    
    #Copied from game object class developed in Lecture 1
    #Tuesday, November 22, 2022 by Pat Virtue
    #which was based on side scroller #3 on 
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#sidescrollerExamples
    def getBounds(self):
    # returns absolute bounds, not taking xScroll into account
        (x0, y1) = (self.X, self.imageHeight/2 - self.Y)
        (x1, y0) = (x0 + self.imageWidth, y1 - self.imageHeight)
        return x0, y0, x1, y1