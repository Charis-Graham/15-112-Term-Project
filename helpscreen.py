from cmu_112_graphics import *

def helpScreenMode_initiate(app):
    app.mode = 'helpScreenMode'
    #image taken from
    #https://www.vecteezy.com/vector-art/4904919-green-leaf-background-illustration-vector
    #created by mitasukmaa
    #and modified using google draw
    app.helpScreen = app.loadImage('images/helpScreen.png')
    sizeOfStart = app.helpScreen.size
    app.helpwidth = sizeOfStart[0]
    app.helpheight = sizeOfStart[1]

def helpScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.helpScreen))
    #app.setSize(app.helpwidth, app.helpheight)

def helpScreenMode_keyPressed(app, event):
    if event.key == "g":
        app.mode = "gameMode"

def helpScreenMode_timerFired(app):
    if (app.width != app.helpScreen.size[0] 
        or app.height != app.helpScreen.size[1]):
        app.setSize(app.helpScreen.size[0], app.helpScreen.size[1])