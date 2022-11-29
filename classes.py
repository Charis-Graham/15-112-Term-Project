from cmu_112_graphics import *
from elephantPlayer import *
import random

class hitBoxInheritance(object):
    pass
#use 15112 Lecture 30 hitbox as example

#creates the elephant class
class Elephant(object):
    def __init__(self, app, lifeState, hunger, thirst, energy):
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
        self.imageX = app.width//2
        self.imageY = app.height//2

        self.hitBox = hitBox(self.imageWidth, self.imageHeight, 
                            self.imageX, self.imageY)
    
    def elephantStandStill(self, app):
        self.elephantStill = self.image
        sizeIm = self.image.size
        self.imageHeight = sizeIm[1]
        self.imageWidth = sizeIm[0]
        self.elephantStill = self.elephantStill.crop(((self.imageWidth//3, 0, 
                                    2*(self.imageWidth//3), 
                                    self.imageHeight//4)))
        stillSize = self.elephantStill.size
        stillImageHeight = sizeIm[1]
        stillImageWidth = sizeIm[0]
        self.hitBox = hitBox(stillImageHeight, stillImageWidth, 
                            self.imageX, self.imageY)
    
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
    
    #for when the herd is further fleshed out, will be one of the functions of bonding
    def elephantShareFood(self, other):
        if self.hitBox.overlap(other):
            self.energy -= 5
            other.energy += 5

#creates the watering hole class
class WateringHole(object):
    def __init__(self, app, waterLevel):
        self.waterLevel = waterLevel
        
        self.image = ''
        self.imageHeight = 0
        self.imageWidth = 0
        self.X, self.Y = 300, 300
        
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
        canvas.create_image(self.X, self.Y,image=ImageTk.PhotoImage(self.image))

    #inspired by getPixel, putPixel example from 
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#events 
    def goMuddy(self, app):
        oldImage = self.image.convert("RGB")
        recolorImage = Image.new(mode="RGB", size=self.image.size)
        for x in range(recolorImage.width):
            for y in range(recolorImage.height):
                r,g,b = oldImage.getpixel((x,y))
                recolorImage.putpixel((x,y), (r, g, 0))
        self.image = recolorImage

#creates the tree object
class Tree(object):
    def __init__(self, leafLevel):
        self.leafLevel = leafLevel
        self.image = ''
        self.imageHeight = 0
        self.imageWidth = 0
        self.X, self.Y = 100, 100
    
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
    
    #inspired by getPixel, putPixel example from 
    #https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#events 
    def goLeaves(self, app):
        oldImage = self.image.convert("RGB")
        recolorImage = Image.new(mode="RGB", size=self.image.size)
        for x in range(recolorImage.width):
            for y in range(recolorImage.height):
                r,g,b = oldImage.getpixel((x,y))
                recolorImage.putpixel((x,y), (r, g, 0))
        self.image = recolorImage

#class to be used as a hitbox to determine when elements are interacting
class hitBox(object):
    def __init__(self, imgWidth, imgHeight, imgX, imgY):
        self.imgWidth = imgWidth
        self.imgHeight = imgHeight
        self.imgX = imgX
        self.imgY = imgY

    #defines the parameters of a hitbox for a given sprite
    def makeHitBox(self):
        #returns a tuple with a rectangular box value for the hitbox
        return (self.imgX, self.imgY, self.imgX + self.imgWidth, 
                    self.imgY+self.imgHeight)
    
    #will determine if two hitboxes are overlapping
    def overlap(self, other):
        pass