from cmu_112_graphics import *

def helpScreenInitiate(app):
    app.mode = 'helpScreenMode'
    #image taken from
    #https://www.livescience.com/27320-elephants.html
    #and modified using google draw
    app.startScreen = app.loadImage('images/helpScreen.png')
    sizeOfStart = app.helpScreen.size
    app.helpwidth = sizeOfStart[0]
    app.helpheight = sizeOfStart[1]

def helpScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.helpScreen))
    #app.setSize(app.helpwidth, app.helpheight)

def helpScreenMode_keyPressed(app, event):
    if event.key == "g":
        app.mode = "gameMode"