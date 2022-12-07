#keeps track of all elephants that the player has intersected with
#challenge 2
def gameMode_elephantIntersectCount(app):
    for elephant in app.elephantList[1:]:
        if (app.player.intersectsObject(elephant) and 
            elephant not in app.elephantIntersected):
            app.elephantIntersectCount += 1
            app.elephantIntersected.append(elephant)

#challenge 3
def gameMode_checkSharedWater(app):
    for elephant in app.elephantList:
        if (elephant.thirst > 0 and elephant not in app.elephantWater):
            app.elephantWaterShared += 1
            app.elephantWater.append(elephant)

#challenge 4
def gameMode_checkSharedFood(app):
    for elephant in app.elephantList:
        if (elephant.hunger > 0 and elephant not in  app.elephantFed):
            app.elephantFoodShared += 1
            app.elephantFed.append(elephant)

#challenge 5
def gameMode_checkDeathMet(app):
    #keeps track of five second intervals
    if (app.player.intersectsObject(app.deadElephant) and
        app.timeWait >= 50 and 
        app.challengeCount == 5):
        app.mode = "wonMode"
    elif (app.player.intersectsObject(app.deadElephant) and
        app.timeWait < 50 and 
        app.challengeCount == 5):
        app.timeWait += 1

#controls the challenges
def gameMode_challenge(app):
    if (app.player.intersectsObject(app.elephantList[0]) and 
        app.player.lifeState == "baby"):
        app.challengeCount = 2
        app.player.lifeState = "adult"
    elif (app.challengeCount == 2 and 
            app.elephantIntersectCount >= 3 and 
            app.player.lifeState == "adult"):
        app.challengeCount = 3
    elif (app.challengeCount == 3 and 
            app.elephantFoodShared >= 3 and 
            app.player.lifeState == "adult"):
        app.challengeCount = 4
    elif (app.challengeCount == 4 and 
            app.elephantWaterShared >= 3 and 
            app.player.lifeState == "adult"):
        app.challengeCount = 5
        app.player.lifeState = "elder"