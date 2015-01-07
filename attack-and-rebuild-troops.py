from datetime import datetime
from math import *
from random import *

#cocWindow = False

# We are assuming BlueStacks is already running and
# COC is loaded and ready to go (centered, zoomed out, etc.)
cocWindow = App("Bluestacks").window(0)
cocSidebar = Region((cocWindow.x + 6), (cocWindow.y + 185), 468, 690)

timestamps = {
    'start':                False,
    'buildTroops':          False,
    'clearObstacles':       False,
    'collectResources':     False,
    'collectStats':         False,
    'donateTroops':         False,
    '_lastInteraction':     False
}

myArmy = {
    'barbarian':     90,
    'archer':        90,
    'giant':         0,
    'goblin':        0,
    'wallbreaker':   10,
    'balloon':      0,
    'wizard':       0,
    'healer':       0,
    'dragon':       0,
    'pekka':        0
}

# TODO: Fix OCR (Make DE conditional on whether they are high enough to have DE)
minGoldToAttack = 30000
minElixirToAttack = 75000
# minDeToAttack = 0



def attack():
    if startAttacking() == False:
        return False
    
    for i in range(0, 20):
        if isGoodOpponent() == True:
            if deployTroops() == True:
                finishBattleAndGoHome()
                return True
            else:
                return False
        else:
            if nextOpponent() == False:
                return False

    return True



def startAttacking():
    try:
        cocWindow.find("1420258650866.png").click()
        sleep(1)
        cocWindow.find("1420258681129.png").click()
        sleep(1)
        
        if (cocWindow.exists("1420258722056.png")):
            cocWindow.find("1420258740243.png").click()

        cocWindow.wait("1420258809432.png", 30)
        return True
    except:
        print "Error starting the attack process"
        return False
        
            

def nextOpponent():
    cocWindow.find("1420259749784.png").click()
    sleep(3)
    cocWindow.wait("1420258809432.png", 30)
    sleep(3)
    
    return True



def isGoodOpponent():
    ## TODO: Test for high level TH/defense/walls/etc
    try:
        goldRegion        = Region((cocWindow.x + 67), (cocWindow.y + 112), 135, 28)
        elixirRegion      = Region((cocWindow.x + 64), (cocWindow.y + 149), 135, 28)
        # deRegion          = Region((cocWindow.x + 64), (cocWindow.y + 188), 125, 28)
    
        gold = numberOCR(goldRegion, 'opponentLoot')
        elixir = numberOCR(elixirRegion, 'opponentLoot')
        # de = numberOCR(deRegion, 'opponentLoot')
    
        print "Gold: ", gold
        print "Elixir: ", elixir
        # print "Dark Elixir: ", de

        if gold >= minGoldToAttack:
            if elixir >= minElixirToAttack:
                #if de >= minDeToAttack:
                return True

        return False
    except:
        print "Something went wrong :("
        print sys.exc_info()[0]
        print sys.exc_info()[1]
        return False



def deployTroops():
    # TODO: Check for full-ish collectors and deploy troops differently if they exist (around all edges)
    
    print "[+] Deploying troops"
    
    try:
        # landmark = cocWindow.find("attack_landmark.png")
        landmark = cocWindow.find("attack_landmark2.png")
        landmark.highlight(1)
        
        Settings.DelayAfterDrag = 0
        Settings.DelayBeforeDrop = 0.1
        Settings.MoveMouseDelay = 0.2
        dragDrop(landmark.getCenter(), Location(cocWindow.x + 68, cocWindow.y + 462))
        Settings.DelayAfterDrag = 0.3
        Settings.DelayAfterDrop = 0.3
        Settings.MoveMouseDelay = 0.5

        landmark = cocWindow.find("attack_landmark2.png")
        landmark.highlight(1)
        
    except:
        print "[!] Could not find attack landmark. Aborting attack."
        cocWindow.find("1420258809432.png").click()
        return False
        
    deployPoints = []
    # deployPoints.append(Location((landmark.getX() - 70), (landmark.getY() + 250)))
    # deployPoints.append(Location((landmark.getX() - 40), (landmark.getY() + 210)))
    # deployPoints.append(Location((landmark.getX() + 18), (landmark.getY() + 165)))
    # deployPoints.append(Location((landmark.getX() + 70), (landmark.getY() + 125)))
    # deployPoints.append(Location((landmark.getX() + 130), (landmark.getY() + 75)))
    # deployPoints.append(Location((landmark.getX() + 175), (landmark.getY() + 45)))
    # deployPoints.append(Location((landmark.getX() + 225), (landmark.getY() + 10)))
    # deployPoints.append(Location((landmark.getX() + 265), (landmark.getY() - 20)))
    # deployPoints.append(Location((landmark.getX() + 320), (landmark.getY() - 64)))
    # deployPoints.append(Location((landmark.getX() - 30), (landmark.getY() + 420)))

    deployPoints.append(Location((landmark.getX() + 334), (landmark.getY() + 146)))
    deployPoints.append(Location((landmark.getX() + 286), (landmark.getY() + 113)))
    deployPoints.append(Location((landmark.getX() + 237), (landmark.getY() + 78)))
    deployPoints.append(Location((landmark.getX() + 200), (landmark.getY() + 47)))
    deployPoints.append(Location((landmark.getX() + 148), (landmark.getY() + 14)))
    deployPoints.append(Location((landmark.getX() + 110), (landmark.getY() - 20)))
    deployPoints.append(Location((landmark.getX() + 40), (landmark.getY() - 80)))
    deployPoints.append(Location((landmark.getX() + 104), (landmark.getY() - 130)))
    deployPoints.append(Location((landmark.getX() + 160), (landmark.getY() - 169)))
    deployPoints.append(Location((landmark.getX() + 201), (landmark.getY() - 204)))
    deployPoints.append(Location((landmark.getX() + 260), (landmark.getY() - 248)))
    deployPoints.append(Location((landmark.getX() + 315), (landmark.getY() - 290)))
    deployPoints.append(Location((landmark.getX() + 360), (landmark.getY() - 325)))
    deployPoints.append(Location((landmark.getX() + 425), (landmark.getY() - 372)))

 #   deployPoints.append(Location((landmark.getX() + 1000), (landmark.getY() + 241)))
 #   deployPoints.append(Location((landmark.getX() + 1057), (landmark.getY() + 197)))
 #   deployPoints.append(Location((landmark.getX() + 1130), (landmark.getY() + 138)))
 #   deployPoints.append(Location((landmark.getX() + 1190), (landmark.getY() + 90)))
 #   deployPoints.append(Location((landmark.getX() + 1251), (landmark.getY() + 29)))
 #   deployPoints.append(Location((landmark.getX() + 1318), (landmark.getY() - 14)))
 #   deployPoints.append(Location((landmark.getX() + 1352), (landmark.getY() - 42)))
 #   deployPoints.append(Location((landmark.getX() + 1386), (landmark.getY() - 85)))
 #   deployPoints.append(Location((landmark.getX() + 1351), (landmark.getY() - 122)))
 #   deployPoints.append(Location((landmark.getX() + 1279), (landmark.getY() - 176)))
 #   deployPoints.append(Location((landmark.getX() + 1229), (landmark.getY() - 213)))
 #   deployPoints.append(Location((landmark.getX() + 1163), (landmark.getY() - 266)))
 #   deployPoints.append(Location((landmark.getX() + 1100), (landmark.getY() - 312)))
 #   deployPoints.append(Location((landmark.getX() + 1040), (landmark.getY() - 353)))
    
    Settings.MoveMouseDelay = 0.01

    try:
        troops_barbarians     = cocWindow.find("troops_barbarians.png")
    except:
        troops_barbarians = False
    
    try:
        troops_archers        = cocWindow.find("troops_archers.png")
    except:
        troops_archers = False

    try:
        troops_wallbreakers   = cocWindow.find("troops_wallbreakers.png")
    except:
        troops_wallbreakers = False

    try:
        troops_clancastle     = cocWindow.find("troops_clancastle.png")
    except:
        troops_clancastle = False

    try:
        troops_barbking       = cocWindow.find("troops_barbking.png")
    except:
        troops_barbking = False

    try:
        troops_healspell      = cocWindow.find("troops_healspell.png")
    except:
        troops_healspell = False

    left_lower = 0
    left_upper = ((len(deployPoints) / 2) - 1)
    right_lower = (len(deployPoints) / 2)
    right_upper = (len(deployPoints) - 1)

    print "Left bounds: ", left_lower, ", ", left_upper
    print "Right bounds: ", right_lower, ", ", right_upper
    
    # Deploy the barbarians first
    if troops_barbarians != False:
        troops_barbarians.click()

        for i in range(0, myArmy['barbarian']):
            cocWindow.click(deployPoints[randint(left_lower, right_upper)])

        #for i in range(0, (myArmy['barbarian'] / 2)):
        #    cocWindow.click(deployPoints[randint(right_lower, right_upper)])

    # Then the wallbreakers
    if troops_wallbreakers != False:
        troops_wallbreakers.click()

        for i in range(0, (myArmy['wallbreaker'] / 2)):
            loc = randint(left_lower, right_upper)
            cocWindow.click(deployPoints[loc])
            cocWindow.click(deployPoints[loc])

    # Then deploy the archers
    if troops_archers != False:
        troops_archers.click()

        for i in range(0, myArmy['archer']):
            cocWindow.click(deployPoints[randint(left_lower, right_upper)])

        #for i in range(0, (myArmy['archer'] / 2)):
        #    cocWindow.click(deployPoints[randint(right_lower, right_upper)])

    # Then the Barb King if available
    if troops_barbking != False:
        troops_barbking.click()
        cocWindow.click(deployPoints[randint(0, right_upper)])
        sleep(8)
        troops_barbking.click()

    # Then clan castle troops if available
    if troops_clancastle != False:
        troops_clancastle.click()
        cocWindow.click(deployPoints[randint(0, right_upper)])

    print "[+] Troops deployed"

    Settings.MoveMouseDelay = 0.5
    
    return True



def finishBattleAndGoHome():
    # TODO: Collect (via OCR) stats about the battle
    #       and record them for later analysis and review
    cocWindow.wait("1420266239930.png", FOREVER)
    cocWindow.getLastMatch().click()
    
    return True



def trainTroops(troops):
    # Routine to train troops for attack
    # - Train equal amount across all barracks
    # -- 45 Barbs, 45 Archers, 3/2 Wallbreakers
    #
    # - Set timer for 24 minutes to begin next attack
    print "[+] Training troops"
    
    village = Region((cocWindow.x + 210), (cocWindow.y + 85), 1025, 790)

    # Divide up the troops that need to be trained
    # between the 4 barracks we have to train with
    #
    # 0 = Barbarians
    # 1 = Archers
    # 2 = Giants
    # 3 = Goblins
    # 4 = Wall Breakers
    # 5 = Balloons
    # 6 = Wizards
    # 7 = Healers
    # 8 = Dragons
    # 9 = PEKKAs
    theBarracks = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
    ]
    totalTroops = 0

    for troop in troops.keys():
        index = None

        if troop == 'barbarian':
            index = 0
        elif troop == 'archer':
            index = 1
        elif troop == 'giant':
            index = 2
        elif troop == 'goblin':
            index = 3
        elif troop == 'wallbreaker':
            index = 4
        elif troop == 'balloon':
            index = 5
        elif troop == 'wizard':
            index = 6
        elif troop == 'healer':
            index = 7
        elif troop == 'dragon':
            index = 8
        elif troop == 'pekka':
            index = 9
        else:
            print 'Invalid troop specified: ', troop
            continue

        theBarracks[0][index] = floor((troops[troop] / 4))
        theBarracks[1][index] = floor((troops[troop] / 4))
        theBarracks[2][index] = floor((troops[troop] / 4))
        theBarracks[3][index] = floor((troops[troop] / 4))

        totalTroops += troops[troop]

        if (troops[troop] % 4 > 0):
            for i in range(0, (troops[troop] % 4)):
                theBarracks[i][index] += 1

    if totalTroops == 0:
        return

    try:
        village.find(Pattern("1420482460039.png").similar(0.90)).click()
        cocWindow.find("1420240132902.png").click()
        sleep(0.5)

        for i in range(0, 4):
            for (index, qty) in enumerate(theBarracks[i]):
                if qty > 0:
                    if index == 0:
                        target = village.find("1420250869807.png")     # Barbarians
                    elif index == 1:
                        target = village.find("1420250654873.png")     # Archers
                    elif index == 2:
                        target = village.find("1420250670215.png")     # Giants
                    elif index == 3:
                        target = village.find("1420250688621.png")     # Goblins
                    elif index == 4:
                        target = village.find("1420250704041.png")     # Wallbreakers
                    elif index == 5:
                        target = village.find("1420250742705.png")     # Balloons
                    elif index == 6:
                        target = village.find("1420250763244.png")     # Wizards
                    elif index == 7:
                        target = village.find("1420250778051.png")     # Healers
                    elif index == 8:
                        target = village.find("1420250807972.png")     # Dragons
                    elif index == 9:
                        target = village.find("1420250835413.png")     # PEKKAs
                    else:
                        print "Invalid index: ", index
    
                    Settings.MoveMouseDelay = 0.05
                    
                    for n in range(0, qty):
                        target.click()
                    
                    Settings.MoveMouseDelay = 0.5
    
            village.find("1420308052116.png").click()
            sleep(0.5)
            
        village.find("1420240870546.png").click()
        sleep(0.5)
        
    except:
        print "Error training new troops"
        print sys.exc_info()[0]
        print sys.exc_info()[1]



def donateTroops():
    # Routine to donate troops to clan members
    # - Open sidebar
    # - Find/click [Donate] button(s)
    # - Donate troops (Archers?) until icon is gray
    # - Track troops donated
    # - Retrain donated troops
    # - Update timers (_lastInteraction, donate, buildTroops, etc.)
    donations = 0
    _openSidebar()

    try:
        for donate in cocSidebar.findAll(Pattern("1420237685511.png").similar(0.80)):
            donate.click()
            sleep(1)
            donateDialog = Region((donate.x + 88), (donate.y - 175), 765, 435)
            Settings.MoveMouseDelay = 0
            
            while donateDialog.exists(Pattern("1420238079816.png").similar(0.90), 0):
                donateDialog.getLastMatch().click()
                donations += 1
                updateTimestamp('_lastInteraction')
                sleep(0.25)
                
            Settings.MoveMouseDelay = 0.5

            print "Donated ", donations, " archers"
    except:
        print "[!] Error donating troops"
        print sys.exc_info()[0]
        print sys.exc_info()[1]
    
    _closeSidebar()
    updateTimestamp('donateTroops')
    trainTroops({ 'archer': donations })
    
    return
    



def _openSidebar():
    try:
        if cocWindow.exists("1420308399291.png",0):
            click(cocWindow.getLastMatch())
            sleep(1)
            return True
        else:
            print "Sidebar opener doesn't exist"
            return False
    except:
        print "[!] Could not open sidebar"
        return False



def _closeSidebar():
    try:
        if cocWindow.exists("1420238603713.png", 0):
            click(cocWindow.getLastMatch())
            sleep(1)
            return True
        else:
            print "Sidebar closer doesn't exist"
            return False
    except:
        print "[!] Could not close sidebar"
        return False



def collectResources():
    startAndFocusApp()
    
    resources = ["1420235690079.png", "1420231189687.png" ,Pattern("1420230934586.png").similar(0.80)]

    window = Region((cocWindow.x + 210), (cocWindow.y + 85), 1025, 790)
    # window.highlight(1)
    for resource in resources:
        try:
            for _temp in window.findAll(resource):
                _temp.click()
                updateTimestamp('_lastInteraction')
                updateTimestamp('collectResources')
        except:
            print "[!] There was an error collecting resources"

    return



def removeObstacles():
    # Routine to find and remove obstacles
    pass



def observeVillageStats():
    # Routine to collect/OCR village stats
    # And return them in an array/dictionary...
    pass



# Starts BlueStacks Player
# Opens Clash of Clans app
# Centers village on the screen
#
# Returns: True if succeeded, False if anything failed
def startClashOfClans():
    startAndFocusApp()
    waitVanish("1420181477444.png", 60)
    sleep(3)
    cocWindow = App("Bluestacks").window(0)
    recentApps = Region((cocWindow.x + 8), (cocWindow.y + 110), 1430, 150)
    
    try:
        recentApps.find(Pattern("1420182034354.png").exact()).click()
        
        cocWindow.wait("1420182438717.png", 30)
        cocWindow.waitVanish("1420182438717.png", FOREVER)
        # cocWindow.wait("1420225678008.png", FOREVER)
        
        # Test for recent enemy raid dialog
        if cocWindow.exists("1420255908709.png"):
            cocWindow.getLastMatch().click()
            sleep(0.5)
        
        sleep(1)
        
        zoomOutAndCenter()
    except:
        print "[!] Could not find COC icon, assuming game is already started..."

    updateTimestamp('start')
    
    return True


# Takes a string as arg1 and updates that
# timestamp (if it exists) with the current
# datetime.
def updateTimestamp(timer):
    if timer in timestamps:
        timestamps[timer] = datetime.now()
    else:
        print "[!] Invalid timestamp: " + timer

    return




# Zooms the screen all the way out
#
# TODO: Reliably center the village on the map
#
# Returns: True on success, False otherwise
def zoomOutAndCenter():
    try:
        startAndFocusApp()

        print "[+] Zooming out and centering village"
        
        type("-", Key.CTRL)
        sleep(0.5)
        type("-", Key.CTRL)
        sleep(0.5)
        type ("-", Key.CTRL)
        sleep(0.5)

        updateTimestamp('_lastInteraction')
    except:
        print "[!] Something went wrong while trying to zoom out..."
        return False
    
    return True



def startAndFocusApp():
    try:
        switchApp("C:\Program Files (x86)\BlueStacks\HD-StartLauncher.exe")
        sleep(1)
    except:
        print "[!] Could not start/focus the BlueStacks Player"
        return False
    
    return True



# Checks to see if we've been kicked for being idle
# If so, it will reload the game and reset the village
# so we can pick up where we left off.
def checkIdle():
    if (cocWindow.exists("1420184045669.png", 0)):
        cocWindow.find("1420184095574.png").click()
        updateTimestamp('_lastInteraction')
        sleep(60)
        zoomOutAndCenter()

        return True
    else:
        return False



def testOcr():
    switchApp("C:\Program Files\Adobe\Adobe Photoshop CS6 (64 Bit)\Photoshop.exe")
    sleep(1)

    try:
        goldRegion = selectRegion("Select Loot")
        gold = numberOCR(goldRegion, 'opponentLoot')

        print "Loot: ", gold

    except:
        print "Failed :("
        print sys.exc_info()[0]
        print sys.exc_info()[1]

    return



##### Helper Functions
# OCR for numbers
# - Currently calibrated for Gold/Elixir/DE/Gems of your villiage
# - TODO: Calibrate for opponents loot when attacking
def numberOCR(Reg, ocrType):
    if ocrType == 'opponentLoot':
        numberImages = [Pattern("oppLoot_0.png").exact(),Pattern("oppLoot_1.png").exact(),Pattern("oppLoot_2.png").exact(),Pattern("oppLoot_3.png").similar(0.95),Pattern("oppLoot_4.png").similar(0.95),Pattern("oppLoot_5.png").exact(),Pattern("oppLoot_6.png").exact(),Pattern("oppLoot_7.png").similar(0.95),Pattern("oppLoot_8.png").exact(),Pattern("oppLoot_9.png").exact()]
    elif ocrType == 'myLoot':
        numberImages = [Pattern("myLoot_0.png").exact(),Pattern("myLoot_1.png").exact(),Pattern("myLoot_2.png").exact(),Pattern("myLoot_3.png").similar(0.95),Pattern("myLoot_4.png").similar(0.95),Pattern("myLoot_5.png").exact(),Pattern("myLoot_6.png").exact(),Pattern("myLoot_7.png").similar(0.95),Pattern("myLoot_8.png").exact(),Pattern("myLoot_9.png").exact()]
        
    digitalNumber = 0
    resultList = list()
    
    # Reg.highlight(1)
    
    for x in numberImages:
        if Reg.exists(x,0):
            Reg.findAll(x)
            #digital find result into list            
            digitalList = list(Reg.getLastMatches())
            #convert list into tuple(image, digital)
            for y in digitalList:
                #resultList.append(tuple(y,0))
                t = (y,digitalNumber)
                resultList.append(t)
        digitalNumber = digitalNumber+1
    sortedResultList = sorted(resultList,key=lambda x: x[0].x)
    #print sortedResultList
    ret = 0
    listLen = len(sortedResultList)
    for x, i in enumerate(sortedResultList):
        ret += 10 **(listLen - x - 1) * i[1]
    return ret

#if (startClashOfClans() == True):
    # Initiate a while loop here that plays the game for us using
    # the methods defined above...
#    print "COC has started and is ready to go!"

#loop = 10
#for i in range(0, loop):
    # TODO: Make each step/function contingent on the last time the function
    #       was run (timestamp) tracked via updateTimestamp()
#    checkIdle()
#    collectResources()
#    donateTroops()
#    sleep(120)
    # trainTroops(myArmy)

# collectResources()
# donateTroops()
# trainTroops(myArmy)
attack()
# deployTroops()
# finishBattleAndGoHome()