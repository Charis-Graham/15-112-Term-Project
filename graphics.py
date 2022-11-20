from cmu_112_graphics import *

#GRASS BACKGROUND
def drawGround(app, canvas):
    canvas.create_image(0,0,
                        image = ImageTk.PhotoImage(app.grassImage))