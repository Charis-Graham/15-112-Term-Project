from cmu_112_graphics import *

#GRASS BACKGROUND
def grass(app):
    #draws the ground
    #Grass PNGs come from https://opengameart.org/content/grass-texture-pack
    #Under CC0
    #Created by Proxy Games
    app.grassImage = app.loadImage(f"images/grass/grass3.jpg")
    sizeIm = app.grassImage.size
    app.grassImageHeight = sizeIm[1]
    app.grassImageWidth = sizeIm[0]

def drawGround(app, canvas):
    for dw in range(0, app.width, 20):
        for dh in range(0, app.height, 20):
            canvas.create_image(dw, dh,
                                image = ImageTk.PhotoImage(app.grassImage))