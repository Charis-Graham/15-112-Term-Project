from cmu_112_graphics import *
import random

#GRASS BACKGROUND
def drawGround(app, canvas):
    for dw in range(0, app.width, 100):
        for dh in range(0, app.width, 100):
            canvas.create_image(dw, dh,
                                image = ImageTk.PhotoImage(app.grassImage))