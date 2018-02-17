#PaintProject1.0.py
##DUE FRIDAY FEB, 3TH, 2017##
from pygame import * #import all pygame modules
from random import * #imoprt all random functions
from tkinter import filedialog #import the tinker module
import tkinter as tk
from math import * #import all math functions

init() #initiate pygame
root=tk.Tk()
root.withdraw()
mixer.init() #initiate music

RED=(255,0,0) #colours
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
LIGHTBLUE=(0,216,255)
WHITE=(255,255,255)

size=(1200,700) #size of window
screen=display.set_mode(size) #create window
display.set_caption("Destiny Paint") #title of window
running=True
#############################################################################
#VARIABLES
tool='no tool' #program starts off with no tool active
col=BLACK #default colour if black (0,0,0)
drawing=False #boolean to check if user is drawing on canvas
release=True #boolean to check if mouse is released
sliding=False #boolean to check if mouse is using the slider
paused=False #boolean to check if the music is paused or playing
index=0 #index for music playlist
toolThickness=1 #size for all tools
omx,omy=300,300 #old mx and my co-ordinates
#############################################################################
#FONTS
calibriFont=font.SysFont("Calibri",20) #creating a font
#############################################################################
#IMPORT IMAGES
mainBackground=image.load("images/pictures/background.jpg") #loading main images
title=image.load("images/pictures/title.png")
colourSpectrum=image.load("images/pictures/colourSpectrum.jpg")
currentColour=image.load("images/tools/currentColour.png")
#############################################################################
#TOOL IMAGES
pencil=image.load("images/tools/pencil.png") #loading tool images
pencilBW=image.load("images/tools/pencilBW.png")
eraser=image.load("images/tools/eraser.png")
eraserBW=image.load("images/tools/eraserBW.png")
fill=image.load("images/tools/fill.png")
fillBW=image.load("images/tools/fillBW.png")
line=image.load("images/tools/line.png")
lineBW=image.load("images/tools/lineBW.png")
spray=image.load("images/tools/spray.png")
sprayBW=image.load("images/tools/sprayBW.png")
freeform=image.load("images/tools/freeform.png")
freeformBW=image.load("images/tools/freeformBW.png")
rect=image.load("images/tools/rect.png")
rectBW=image.load("images/tools/rectBW.png")
fillrect=image.load("images/tools/fill rect.png")
fillrectBW=image.load("images/tools/fill rectBW.png")
circle=image.load("images/tools/circle.png")
circleBW=image.load("images/tools/circleBW.png")
fillcircle=image.load("images/tools/fill circle.png")
fillcircleBW=image.load("images/tools/fill circleBW.png")
brush=image.load("images/tools/brush.png")
brushBW=image.load("images/tools/brushBW.png")
fillarea=image.load("images/tools/fillarea.png")
fillareaBW=image.load("images/tools/fillareaBW.png")
#############################################################################
#FUNCTION IMAGES
clearCanvas=image.load("images/tools/clearCanvas.png") #loading function images
clearCanvasBW=image.load("images/tools/clearCanvasBW.png")
openfile=image.load("images/tools/open.png")
openfileBW=image.load("images/tools/openBW.png")
savefile=image.load("images/tools/save.png")
savefileBW=image.load("images/tools/saveBW.png")
redo=image.load("images/tools/redo.png")
redoBW=image.load("images/tools/redoBW.png")
undo=image.load("images/tools/undo.png")
undoBW=image.load("images/tools/undoBW.png")
#############################################################################
#TOOL DESCRIPTION IMAGES
dnoTool=image.load("images/tools/dnoTool.png") #loading tool description images
dpencil=image.load("images/tools/dpencil.png")
deraser=image.load("images/tools/deraser.png")
dfill=image.load("images/tools/dfill.png")
dline=image.load("images/tools/dline.png")
dspray=image.load("images/tools/dspray.png")
dfreeform=image.load("images/tools/dfreeform.png")
drect=image.load("images/tools/drect.png")
dfillRect=image.load("images/tools/dfillRect.png")
dcircle=image.load("images/tools/dcircle.png")
dfillCircle=image.load("images/tools/dfillCircle.png")
dbrush=image.load("images/tools/dbrush.png")
dfillarea=image.load("images/tools/dfillarea.png")
#############################################################################
#FUNTION DESCRIPTION IMAGES
dundo=image.load("images/tools/dundo.png") #loading function description images
dredo=image.load("images/tools/dredo.png")
dopen=image.load("images/tools/dopen.png")
dsave=image.load("images/tools/dsave.png")
dclearCanvas=image.load("images/tools/dclearCanvas.png")
dslider=image.load("images/tools/dslider.png")
#############################################################################
#MAIN SCREEN STAMPS
hunterIB=image.load("images/stamps/hunterIB.png") #loading button stamp images
titanIB=image.load("images/stamps/titanIB.png")
warlockIB=image.load("images/stamps/warlockIB.png")
hunterToO=image.load("images/stamps/hunterToO.png")
titanToO=image.load("images/stamps/titanToO.png")
warlockToO=image.load("images/stamps/warlockToO.png")
thorn=image.load("images/stamps/thorn.png")
sparrow=image.load("images/stamps/sparrow.png")
captain=image.load("images/stamps/captain.png")
ghost=image.load("images/stamps/ghost.png")
gjallarhorn=image.load("images/stamps/gjallarhorn.png")
tank=image.load("images/stamps/tank.png")
#############################################################################
#STAMPS
hunterIBStamp=image.load("images/stamps/hunterIBStamp.png") #loading actual stamp images
titanIBStamp=image.load("images/stamps/titanIBStamp.png")
warlockIBStamp=image.load("images/stamps/warlockIBStamp.png")
hunterToOStamp=image.load("images/stamps/hunterToOStamp.png")
titanToOStamp=image.load("images/stamps/titanToOStamp.png")
warlockToOStamp=image.load("images/stamps/warlockToOStamp.png")
thornStamp=image.load("images/stamps/thornStamp.png")
captainStamp=image.load("images/stamps/captainStamp.png")
sparrowStamp=image.load("images/stamps/sparrowStamp.png")
ghostStamp=image.load("images/stamps/ghostStamp.png")
gjallarhornStamp=image.load("images/stamps/gjallarhornStamp.png")
tankStamp=image.load("images/stamps/tankStamp.png")
dStamp=image.load("images/tools/dStamp.png")
#############################################################################
#TRANSFORM STAMPS
hunterIBStamp=transform.scale(hunterIBStamp,(120,263)) #transforming the stamps that will be placed on the canvas
titanIBStamp=transform.scale(titanIBStamp,(120,263))
warlockIBStamp=transform.scale(warlockIBStamp,(120,263))
hunterToOStamp=transform.scale(hunterToOStamp,(120,263))
titanToOStamp=transform.scale(titanToOStamp,(100,263))
warlockToOStamp=transform.scale(warlockToOStamp,(100,263))
thornStamp=transform.scale(thornStamp,(200,111))
captainStamp=transform.scale(captainStamp,(150,200))
sparrowStamp=transform.scale(sparrowStamp,(200,100))
ghostStamp=transform.scale(ghostStamp,(75,75))
gjallarhornStamp=transform.scale(gjallarhornStamp,(200,75))
tankStamp=transform.scale(tankStamp,(200,100))
#############################################################################
#TRANSFORM IMAGES
mainBackground=transform.scale(mainBackground,(1200,700)) #transforming the main images
title=transform.scale(title,(380,140))
colourSpectrum=transform.scale(colourSpectrum,(280,140))
#############################################################################
#ALL RECTANGLE OBJECTS
canvasRect=Rect(400,10,790,502) #creating rectangles for functions
undoRect=Rect(330,180,50,50)
redoRect=Rect(330,250,50,50)
openRect=Rect(330,320,50,50)
saveRect=Rect(330,390,50,50)
clearCanvasRect=Rect(330,460,50,50)
colourSpectrumRect=Rect(20,530,280,140)
currentColourRect=Rect(320,530,60,60)
selectedColourRect=Rect(320,600,60,60)
descriptionRect=Rect(920,530,270,140)
#############################################################################
#TOOL RECTANGLES
pencilRect=Rect(400,530,60,60) #creating rectangles for tools
eraserRect=Rect(480,530,60,60)
fillRect=Rect(560,530,60,60)
lineRect=Rect(640,530,60,60)
sprayRect=Rect(720,530,60,60)
freeFormRect=Rect(800,530,60,60)
rectRect=Rect(400,610,60,60)
rectFillRect=Rect(480,610,60,60)
circleRect=Rect(560,610,60,60)
circleFillRect=Rect(640,610,60,60)
brushRect=Rect(720,610,60,60)
fillAreaRect=Rect(800,610,60,60)
#############################################################################
#STAMP RECTANGLES
hunterIBRect=Rect(252,390,50,120) #creating rectangles for stamps
titanIBRect=Rect(192,390,50,120)
warlockIBRect=Rect(132,390,50,120)
hunterToORect=Rect(252,250,50,120)
titanToORect=Rect(192,250,50,120)
warlockToORect=Rect(132,250,50,120)
thornRect=Rect(20,390,102,55)
sparrowRect=Rect(20,455,102,55)
captainRect=Rect(20,250,102,120)
ghostRect=Rect(20,180,50,50)
gjallarhornRect=Rect(80,180,120,50)
tankRect=Rect(210,180,92,50)
#############################################################################
#LOAD MUSIC
originalDestiny=mixer.Sound("music/Original Destiny.ogg") #loading music
takenKing=mixer.Sound("music/Taken King.ogg")
riseOfIron=mixer.Sound("music/Rise of Iron.ogg")
theTraveler=mixer.Sound("music/The Traveler.ogg")
fromHope=mixer.Sound("music/Excerpt from the Hope.ogg")
fromEcstasy=mixer.Sound("music/Excerpt from the Ecstasy.ogg")
theArchpriest=mixer.Sound("music/The Archpriest.ogg")
bowToNoOne=mixer.Sound("music/Bow To No One.ogg")
dustGiants=mixer.Sound("music/Dust Giants.ogg")
#############################################################################
#DESCRIPTION BOXES FOR MUSIC
dpause=image.load("images/music/dpause.png") #load description images for music boxes
dnext=image.load("images/music/dnext.png")
dlast=image.load("images/music/dlast.png")
#############################################################################
#MUSIC LIST
musicList=[] #empty music list
musicList.append(originalDestiny) #adding the loaded songs to the music playlist
musicList.append(takenKing)
musicList.append(riseOfIron)
musicList.append(theTraveler)
musicList.append(fromHope)
musicList.append(fromEcstasy)
musicList.append(theArchpriest)
musicList.append(bowToNoOne)
musicList.append(dustGiants)
song=musicList[index] #selecting the song based on the index number
musicChannel=mixer.Channel(0)
musicChannel.play(song) #playing the song
#############################################################################
#MUSIC RECTANGLES
playRect=Rect(20,85,45,45) #creating rectangles for music
pauseRect=Rect(20,85,45,45)
nextRect=Rect(70,85,40,20)
lastRect=Rect(70,110,40,20)
musicTextRect=Rect(0,130,175,45)
#############################################################################
#MUSIC IMAGES
playPic=image.load("images/music/playPic.png") #loading music images
pausePic=image.load("images/music/pausePic.png")
nextPic=image.load("images/music/nextPic.png")
lastPic=image.load("images/music/nextPic.png")
#############################################################################
#TRANSFORM MUSIC IMAGES
playPic=transform.scale(playPic,(45,45)) #transforming music images
pausePic=transform.scale(pausePic,(55,55))
nextPic=transform.scale(nextPic,(35,15))
lastPic=transform.rotate(nextPic,180)
#############################################################################
#MAIN BACKGROUND
screen.blit(mainBackground,(0,0)) #placing the main background
screen.blit(title,(10,25)) #placing the "Destiny" title
#############################################################################
#SURFACE FOR PAUSE AND PLAY
playSurface=screen.copy().subsurface(playRect) #taking a copy of the pause/play box
musicTextSurface=screen.copy().subsurface(musicTextRect) #taking a copy of the screen where the song names will be shown
screen.blit(pausePic,(15,80))
#############################################################################
#SURFACE FOR CURRENT COLOUR
selectedSurface=screen.copy().subsurface(selectedColourRect) #taking a copy of the box around "Current Colour"
#############################################################################
#SURFACE FOR CURRENT COLOUR TEXT
#############################################################################
#CANVAS
draw.rect(screen,WHITE,(canvasRect)) #drawing the original canvas
#############################################################################
#OUTLINE OF CANVAS
draw.rect(screen,BLUE,(397,7,796,508),5) #canvas outline
#CORNERS OF CANVAS OUTLINE
draw.circle(screen,BLUE,(396,7),1) #top left corner fill
draw.circle(screen,BLUE,(396,515),1) #bottom left corner fill
draw.circle(screen,BLUE,(1194,7),1) #top right corner fill
draw.circle(screen,BLUE,(1194,515),1) #bottom right corner fill
#OUTLINE OF COLUR SPECTRUM
draw.rect(screen,RED,(18,528,284,144),3)
#############################################################################
#SLIDER RECTANGLES
sliderRect=Rect(870,529+toolThickness,40,10) #creating rectangles related to the slider
handleRect=Rect(885,530,10,109)
toolThicknessRect=Rect(870,530,40,110)
sliderSurface=screen.copy().subsurface(toolThicknessRect) #taking a copy of the slider box
sizeTextRect=Rect(860,630,60,60)
sizeSurface=screen.copy().subsurface(sizeTextRect) #taking a copy of the box around "Size"
#############################################################################
#LISTS
undoList=[screen.copy().subsurface(canvasRect)] #undo list will start with a picture on the blank canvas
redoList=[] #stays empty until the user clicks undo
#############################################################################
#BRUSH TOOL
brushHead=Surface((200,200),SRCALPHA) #creating a brush surface
#############################################################################
while running:
    mx,my=mouse.get_pos() #position of mouse
    mb=mouse.get_pressed() #variable for if mouse gets pressed
    for evt in event.get(): #the event queue loop
        if evt.type==QUIT: #if the quit is clicked
            running=False #quit the program
        if evt.type==KEYDOWN: #if a key is pressed
            if evt.key==K_ESCAPE: #if the key pressed is ESCAPE
                running=False #quit the program
        if evt.type==MOUSEBUTTONDOWN: #if the mouse is pressed
            if evt.button==1: #if the left moouse button is pressed
                start=evt.pos #start is position of the mouse
                startx,starty=mx,my #making startx and starty my and my
                back=screen.copy() #taking a copy of the current screen
            if toolThicknessRect.collidepoint(mx,my): #if the mouse is on the slider
                sliding=True
            if canvasRect.collidepoint(mx,my): #if the mouse is on the canvas
                drawing=True
            if evt.button==4: #if mouse is scrolled up
                if toolThickness>1: #min thickness is 1
                    toolThickness-=1 #subtract one from toolthickness
                    screen.blit(sliderSurface,(870,530))
            if evt.button==5: #if mouse if scrolled down
                if toolThickness<100: #max thickness is 100
                    toolThickness+=1 #add one to toolthickness
                    screen.blit(sliderSurface,(870,530))
        if evt.type==MOUSEBUTTONUP: #if the mouse is released
            if evt.button==1: #if the left mouse button is clicked
                if drawing or openRect.collidepoint(mx,my) or saveRect.collidepoint(mx,my): #if the user is drawing or on the open or save box
                    undoCanvas=screen.subsurface(canvasRect).copy() #copy the current canvas 
                    undoList.append(undoCanvas) #add that picture to the undo list
                if undoRect.collidepoint(mx,my) and mb[0]==1: #if the undo box is clicked
                    if len(undoList)>1: #if there is a picture in the undo list
                        redoList.append(undoList.pop()) #taking the last picture that was undone and putting it into the redo list
                        screen.blit(undoList[-1],canvasRect) #placing the last canvas picture in the list onto the canvas
                if redoRect.collidepoint(mx,my) and mb[0]==1: #if the redo box is clicked
                    if len(redoList)!=0: #if there is a picture in the redo list
                        undoList.append(redoList.pop()) #taking the last picture that was redone and putting it into the undo list
                        screen.blit(undoList[-1],canvasRect) #placing the last canvas picture in the list onto the canvas
                release=True
                drawing=False
                sliding=False
        if not musicChannel.get_busy(): #if music is not playing
            index+=1 #next song in the list
            if index==len(musicList): #if the moving from the last song
                index=0 #go to the beginning of the music playlist
            song=musicList[index] #selecting the song based on the index number
            musicChannel.play(song) #playing the song
#############################################################################
#DRAWING MAIN PAGE
#############################################################################
#TEXT FOR SIZE AND COLOUR
    screen.blit(selectedSurface,(320,600)) 
    currentText=calibriFont.render('Current',True,WHITE) #creating text that says 'Current'
    colourText=calibriFont.render('Colour',True,WHITE)#creating text that says 'Colour' (seperate so it can be placed under 'Current')
    sizeText=calibriFont.render('Size:',True,WHITE) #creating text that says 'Size'
    toolSizeText=str(toolThickness) #puts the toolthickness into a string (ie: '5')
    toolThicknessText=calibriFont.render(toolSizeText,True,WHITE) #creating the toolthickness text
    screen.blit(currentText,(320,600)) #placing the 'Current' text
    screen.blit(colourText,(322,620)) #placing the 'Colour' text
    screen.blit(sizeSurface,(860,630)) #re-blitting the size rectangle to avoid the toolthickness texts showing on-top of eachother when switched
    screen.blit(sizeText,(872,645)) #placing the 'Size' text
    if len(str(toolThickness))==1: #if the toolthickness is 1 digit
        screen.blit(toolThicknessText,(885,665)) #place in different place so it looks centered
    elif len(str(toolThickness))==2: #if the toolthickness is 2 digits
        screen.blit(toolThicknessText,(879,665)) #place in different place so it looks centered
    elif len(str(toolThickness))==3: #if the toolthickness is 3 digits
        screen.blit(toolThicknessText,(874,665)) #place in different place so it looks centered
#############################################################################
#TEXT FOR MUSIC
    if song==originalDestiny: #if the song is...
        screen.blit(musicTextSurface,(0,130)) #re-blitting the size rectangle to avoid the toolthickness texts showing on-top of eachother when switched
        destinyText=calibriFont.render("1. Theme Song",True,WHITE) #create the text for the specific song
        screen.blit(destinyText,(20,150)) #place the text of the current song on the screen
    elif song==takenKing:
        screen.blit(musicTextSurface,(0,130))
        takenKingText=calibriFont.render("2. The Taken King",True,WHITE)
        screen.blit(takenKingText,(20,150))
    elif song==riseOfIron:
        screen.blit(musicTextSurface,(0,130))
        riseOfIronText=calibriFont.render("3. Rise of Iron",True,WHITE)
        screen.blit(riseOfIronText,(20,150))
    elif song==theTraveler:
        screen.blit(musicTextSurface,(0,130))
        theTravelerText=calibriFont.render("4. The Traveler",True,WHITE)
        screen.blit(theTravelerText,(20,150))
    elif song==fromHope:
        screen.blit(musicTextSurface,(0,130))
        fromHopeText=calibriFont.render("5. From Hope",True,WHITE)
        screen.blit(fromHopeText,(20,150))
    elif song==fromEcstasy:
        screen.blit(musicTextSurface,(0,130))
        fromEcstasyText=calibriFont.render("6. From Ecstasy",True,WHITE)
        screen.blit(fromEcstasyText,(20,150))
    elif song==theArchpriest:
        screen.blit(musicTextSurface,(0,130))
        theArchpriestText=calibriFont.render("7. The Archpriest",True,WHITE)
        screen.blit(theArchpriestText,(20,150))
    elif song==bowToNoOne:
        screen.blit(musicTextSurface,(0,130))
        bowToNoOneText=calibriFont.render("8. Bow To No One",True,WHITE)
        screen.blit(bowToNoOneText,(20,150))
    elif song==dustGiants:
        screen.blit(musicTextSurface,(0,130))
        dustGiantsText=calibriFont.render("9. Dust Giants",True,WHITE)
        screen.blit(dustGiantsText,(20,150))
#############################################################################
    draw.rect(screen,BLACK,handleRect) #drawing the slider rectangle
    draw.rect(screen,RED,(870,529+toolThickness,40,10)) #drawing the handle depending on the toolthickness
#############################################################################
#FUNCTIONS
    screen.blit(clearCanvasBW,(330,460)) #placing the black/white function pictures on the screen
    screen.blit(openfileBW,(330,320))
    screen.blit(savefileBW,(330,390))
    screen.blit(redoBW,(330,250))
    screen.blit(undoBW,(330,180))
#############################################################################
#FUNCTION BOXES
    draw.rect(screen,RED,clearCanvasRect,3) #drawing the rectangles around the function pictures
    draw.rect(screen,RED,openRect,3)
    draw.rect(screen,RED,saveRect,3)
    draw.rect(screen,RED,redoRect,3)
    draw.rect(screen,RED,undoRect,3)
#############################################################################
#NON-TOOLS
    screen.blit(colourSpectrum,(20,530)) #placing the colour spectrun on the screen
    screen.blit(dnoTool,(920,530)) #description box at the beginning
#############################################################################
#MUSIC IMAGES
    screen.blit(nextPic,(72,87)) #placing the music pictures on the screen
    screen.blit(lastPic,(73,113))
#############################################################################
#MUSIC BOXES
    draw.rect(screen,RED,playRect,3) #drawing the rectangles around the music boxes
    draw.rect(screen,RED,nextRect,3)
    draw.rect(screen,RED,lastRect,3)
#############################################################################
#NON-TOOL BOXES
    draw.rect(screen,RED,descriptionRect,3) #drawing the rectangles around the colour and description boxes
    draw.rect(screen,col,currentColourRect)
    draw.rect(screen,RED,currentColourRect,3)
#############################################################################
#TOOLS
    screen.blit(pencilBW,(400,530)) #placing the black/white tool pictures on the screen
    screen.blit(eraserBW,(480,530))
    screen.blit(fillBW,(560,530))
    screen.blit(lineBW,(640,530))
    screen.blit(sprayBW,(720,530))
    screen.blit(freeformBW,(800,530))
    screen.blit(rectBW,(400,610))
    screen.blit(fillrectBW,(480,610))
    screen.blit(circleBW,(560,610))
    screen.blit(fillcircleBW,(640,610))
    screen.blit(brushBW,(720,610))
    screen.blit(fillareaBW,(800,610))
#############################################################################
#TOOL BOXES
    draw.rect(screen,RED,pencilRect,3) #drawing the rectangles around the tool boxes
    draw.rect(screen,RED,eraserRect,3)
    draw.rect(screen,RED,fillRect,3)
    draw.rect(screen,RED,lineRect,3)
    draw.rect(screen,RED,sprayRect,3)
    draw.rect(screen,RED,freeFormRect,3)
    draw.rect(screen,RED,rectRect,3)
    draw.rect(screen,RED,rectFillRect,3)
    draw.rect(screen,RED,circleRect,3)
    draw.rect(screen,RED,circleFillRect,3)
    draw.rect(screen,RED,brushRect,3)
    draw.rect(screen,RED,fillAreaRect,3)
#############################################################################
#STAMPS
    screen.blit(hunterIB,(252,390)) #placing the stamp pictures on the screen
    screen.blit(titanIB,(192,390))
    screen.blit(warlockIB,(132,390))
    screen.blit(hunterToO,(252,250))
    screen.blit(titanToO,(192,250))
    screen.blit(warlockToO,(132,250))
    screen.blit(thorn,(20,390))
    screen.blit(sparrow,(20,455))
    screen.blit(captain,(20,250))
    screen.blit(ghost,(20,180))
    screen.blit(gjallarhorn,(80,180))
    screen.blit(tank,(210,180))
#############################################################################
#STAMP BOXES
    draw.rect(screen,RED,hunterIBRect,3) #drawing the rectangles around the stamp boxes
    draw.rect(screen,RED,titanIBRect,3)
    draw.rect(screen,RED,warlockIBRect,3)
    draw.rect(screen,RED,hunterToORect,3)
    draw.rect(screen,RED,titanToORect,3)
    draw.rect(screen,RED,warlockToORect,3)
    draw.rect(screen,RED,thornRect,3)
    draw.rect(screen,RED,sparrowRect,3)
    draw.rect(screen,RED,captainRect,3)
    draw.rect(screen,RED,ghostRect,3)
    draw.rect(screen,RED,gjallarhornRect,3)
    draw.rect(screen,RED,tankRect,3)
#############################################################################
#PAUSE AND PLAY
    if playRect.collidepoint(mx,my) and release and paused==False: #if the play box is clicked while the music is playing
        screen.blit(playSurface,(20,85)) #re-blitting the play surface to avoid the play and pause pictures showing on-top of eachother when switched
        musicChannel.pause() #pause the music
        screen.blit(playPic,(20,85)) #placing the play picture on the screen
        paused=True #music is paused
    elif playRect.collidepoint(mx,my) and release and paused==True: #if the play box is clicked while the music is paused
        screen.blit(playSurface,(20,85)) #re-blitting the play surface to avoid the play and pause pictures showing on-top of eachother when switched
        musicChannel.unpause() #play the music
        screen.blit(pausePic,(15,80)) #placing the pause picture on the screen
        paused=False #music is playing
#############################################################################
#SKIP SONG
    if nextRect.collidepoint(mx,my) and release: #if the next button is pressed
        musicChannel.stop() #stop the current song
        index+=1 #go to the next song in the playlist
        if index==len(musicList): #if the moving from the last song
            index=0 #go to the beginning of the playlist
        song=musicList[index] #selecting the song depending on the index number
        musicChannel.play(song) #playing the song
        screen.blit(playSurface,(20,85)) #re-blitting the play surface to avoid the play and pause pictures showing on-top of eachother when switched
        screen.blit(pausePic,(15,80)) #placing the pause picture on the screen
        paused=False #music is playing
#############################################################################
#LAST SONG
    if lastRect.collidepoint(mx,my) and release:
        musicChannel.stop()
        index-=1 #go to the previous song in the playlist
        if index==0-len(musicList): #if the moving from the last song
            index=0 #go to the beginning of the playlist
        song=musicList[index] #selecting the song depending on the index number
        musicChannel.play(song) #playing the song
        screen.blit(playSurface,(20,85)) #re-blitting the play surface to avoid the play and pause pictures showing on-top of eachother when switched
        screen.blit(pausePic,(15,80)) #placing the pause picture on the screen
        paused=False #music is playing
#############################################################################
#HOVER OVER TOOL
    if pencilRect.collidepoint(mx,my): #if the mouse hovers over a certain tool box
        screen.blit(pencil,(400,530)) #place the non-black/white version of the tool picture on the screen
        draw.rect(screen,LIGHTBLUE,pencilRect,3) #draw a light blue rectangle around the tool picture
    elif eraserRect.collidepoint(mx,my):
        screen.blit(eraser,(480,530))
        draw.rect(screen,LIGHTBLUE,eraserRect,3)
    elif fillRect.collidepoint(mx,my):
        screen.blit(fill,(560,530))
        draw.rect(screen,LIGHTBLUE,fillRect,3)
    elif lineRect.collidepoint(mx,my):
        screen.blit(line,(640,530))
        draw.rect(screen,LIGHTBLUE,lineRect,3)
    elif sprayRect.collidepoint(mx,my):
        screen.blit(spray,(720,530))
        draw.rect(screen,LIGHTBLUE,sprayRect,3)
    elif freeFormRect.collidepoint(mx,my):
        screen.blit(freeform,(800,530))
        draw.rect(screen,LIGHTBLUE,freeFormRect,3)
    elif rectRect.collidepoint(mx,my):
        screen.blit(rect,(400,610))
        draw.rect(screen,LIGHTBLUE,rectRect,3)
    elif rectFillRect.collidepoint(mx,my):
        screen.blit(fillrect,(480,610))
        draw.rect(screen,LIGHTBLUE,rectFillRect,3)
    elif circleRect.collidepoint(mx,my):
        screen.blit(circle,(560,610))
        draw.rect(screen,LIGHTBLUE,circleRect,3)
    elif circleFillRect.collidepoint(mx,my):
        screen.blit(fillcircle,(640,610))
        draw.rect(screen,LIGHTBLUE,circleFillRect,3)
    elif brushRect.collidepoint(mx,my):
        screen.blit(brush,(720,610))
        draw.rect(screen,LIGHTBLUE,brushRect,3)
    elif fillAreaRect.collidepoint(mx,my):
        screen.blit(fillarea,(800,610))
        draw.rect(screen,LIGHTBLUE,fillAreaRect,3)
#############################################################################
#HOVER OVER STAMP
    if hunterIBRect.collidepoint(mx,my): #if the mouse hovers over a certain stamp box
        draw.rect(screen,LIGHTBLUE,hunterIBRect,3) #draw a light blue rectangle around the stamp picture
    elif titanIBRect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,titanIBRect,3)
    elif warlockIBRect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,warlockIBRect,3)
    elif hunterToORect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,hunterToORect,3)
    elif titanToORect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,titanToORect,3)
    elif warlockToORect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,warlockToORect,3)
    elif thornRect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,thornRect,3)
    elif captainRect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,captainRect,3)
    elif sparrowRect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,sparrowRect,3)
    elif ghostRect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,ghostRect,3)
    elif gjallarhornRect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,gjallarhornRect,3)
    elif tankRect.collidepoint(mx,my):
        draw.rect(screen,LIGHTBLUE,tankRect,3)
#############################################################################
#HOVER OVER FUNCTION
    if clearCanvasRect.collidepoint(mx,my): #if the mouse hover over a specific funtion box
        screen.blit(clearCanvas,(330,460)) #place the non-black/white version of the tool picture on the screen
        draw.rect(screen,LIGHTBLUE,clearCanvasRect,3) #draw a light blue rectangle around the function picture
    elif openRect.collidepoint(mx,my):
        screen.blit(openfile,(330,320))
        draw.rect(screen,LIGHTBLUE,openRect,3)
    elif saveRect.collidepoint(mx,my):
        screen.blit(savefile,(330,390))
        draw.rect(screen,LIGHTBLUE,saveRect,3)
    elif redoRect.collidepoint(mx,my):
        screen.blit(redo,(330,250))
        draw.rect(screen,LIGHTBLUE,redoRect,3)
    elif undoRect.collidepoint(mx,my):
        screen.blit(undo,(330,180))
        draw.rect(screen,LIGHTBLUE,undoRect,3)
#############################################################################
#CLICK ON TOOL
    if evt.type==MOUSEBUTTONUP:
        if evt.button==1: #Only if left click (To avoid it selecting when scroll is used)
            if pencilRect.collidepoint(mx,my) and release: #if mouse is released on a specific tool rectangle
                screen.blit(pencil,(400,530)) #place the non-black/white image of the tool on the screen
                tool='pencil' #the current tool becomes...
            elif eraserRect.collidepoint(mx,my) and release:
                screen.blit(eraser,(480,530))
                tool='eraser'
            elif fillRect.collidepoint(mx,my) and release:
                screen.blit(fill,(560,530))
                tool='fill'
            elif lineRect.collidepoint(mx,my) and release:
                screen.blit(line,(640,530))
                tool='line'
            elif sprayRect.collidepoint(mx,my) and release:
                screen.blit(spray,(720,530))
                tool='spray'
            elif freeFormRect.collidepoint(mx,my) and release :
                screen.blit(freeform,(800,530))
                tool='free form'
            elif rectRect.collidepoint(mx,my) and release :
                screen.blit(rect,(400,610))
                tool='rect'
            elif rectFillRect.collidepoint(mx,my) and release :
                screen.blit(fillrect,(480,610))
                tool='fill rect'
            elif circleRect.collidepoint(mx,my) and release :
                screen.blit(circle,(560,610))
                tool='circle'
            elif circleFillRect.collidepoint(mx,my) and release :
                screen.blit(fillcircle,(640,610))
                tool='fill circle'
            elif brushRect.collidepoint(mx,my) and release :
                screen.blit(brush,(720,610))
                tool='brush'
            elif fillAreaRect.collidepoint(mx,my) and release :
                screen.blit(fillarea,(800,610))
                tool='fill area'
#############################################################################
#CLICK ON STAMP
    if evt.type==MOUSEBUTTONUP:
        if evt.button==1: #Only if left click (To avoid it selecting when scroll is used)
            if hunterIBRect.collidepoint(mx,my) and release: #if the mouse was released on a specific stamp rectangle
                tool='hunterIB' #the current tool becomes...
            elif titanIBRect.collidepoint(mx,my) and release:
                tool='titanIB'
            elif warlockIBRect.collidepoint(mx,my) and release:
                tool='warlockIB'
            elif hunterToORect.collidepoint(mx,my) and release:
                tool='hunterToO'
            elif titanToORect.collidepoint(mx,my) and release:
                tool='titanToO'
            elif warlockToORect.collidepoint(mx,my) and release:
                tool='warlockToO'
            elif thornRect.collidepoint(mx,my) and release:
                tool='thorn'
            elif captainRect.collidepoint(mx,my) and release:
                tool='captain'
            elif sparrowRect.collidepoint(mx,my) and release:
                tool='sparrow'
            elif ghostRect.collidepoint(mx,my) and release:
                tool='ghost'
            elif gjallarhornRect.collidepoint(mx,my) and release:
                tool='gjallarhorn'
            elif tankRect.collidepoint(mx,my) and release:
                tool='tank'
#############################################################################
#CLICK ON FUNCTION
    if clearCanvasRect.collidepoint(mx,my) and mb[0]==1: #if the mouse is pressed on a specific funtion
        screen.blit(clearCanvas,(330,460)) #place the non-black/white image of the function on the screen
        draw.rect(screen,BLUE,clearCanvasRect,3) #draw a blue rectangle around the function image
    elif openRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(openfile,(330,320))
        draw.rect(screen,BLUE,openRect,3)
    elif saveRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(savefile,(330,390))
        draw.rect(screen,BLUE,saveRect,3)
    elif redoRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(redo,(330,250))
        draw.rect(screen,BLUE,redoRect,3)
    elif undoRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(undo,(330,180))
        draw.rect(screen,BLUE,undoRect,3)
#############################################################################
#SELECTED TOOL
    if tool=='no tool': #if no tool is selected
        screen.blit(dnoTool,(920,530)) #place the 'no tool' image in the description rectangle
        draw.rect(screen,BLUE,descriptionRect,3) #draw a blue rectangle around the tool image
    elif tool=='pencil': #if the current tool is...
        screen.blit(pencil,(400,530)) #place the non-black/white image of the tool on the screen
        screen.blit(dpencil,(920,530)) #place the description image of that tool in the description rectangle
        draw.rect(screen,BLUE,descriptionRect,3) #draw a blue rectangle around the description rectangle
        draw.rect(screen,BLUE,pencilRect,3) #draw a blue rectangle around the tool image
    elif tool=='eraser':
        screen.blit(eraser,(480,530))
        screen.blit(deraser,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,eraserRect,3)
    elif tool=='fill':
        screen.blit(fill,(560,530))
        screen.blit(dfill,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,fillRect,3)
    elif tool=='line':
        screen.blit(line,(640,530))
        screen.blit(dline,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,lineRect,3)
    elif tool=='spray':
        screen.blit(spray,(720,530))
        screen.blit(dspray,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,sprayRect,3)
    elif tool=='free form':
        screen.blit(freeform,(800,530))
        screen.blit(dfreeform,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,freeFormRect,3)
    elif tool=='rect':
        screen.blit(rect,(400,610))
        screen.blit(drect,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,rectRect,3)
    elif tool=='fill rect':
        screen.blit(fillrect,(480,610))
        screen.blit(dfillRect,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,rectFillRect,3)
    elif tool=='circle':
        screen.blit(circle,(560,610))
        screen.blit(dcircle,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,circleRect,3)
    elif tool=='fill circle':
        screen.blit(fillcircle,(640,610))
        screen.blit(dfillCircle,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,circleFillRect,3)
    elif tool=='brush':
        screen.blit(brush,(720,610))
        screen.blit(dbrush,(920,530)) 
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,brushRect,3)
    elif tool=='fill area':
        screen.blit(fillarea,(800,610))
        screen.blit(dfillarea,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,BLUE,fillAreaRect,3)
#############################################################################
#SELECTED STAMP
    if tool=='hunterIB': #is the current tool (stamp) is...
        draw.rect(screen,BLUE,hunterIBRect,3) #draw a blue rectangle around the stamp image
        screen.blit(dStamp,(920,530)) #place the description image of that tool in the description rectangle
        draw.rect(screen,BLUE,descriptionRect,3) #draw a blue rectangle around the description rectangle
    elif tool=='titanIB':
        draw.rect(screen,BLUE,titanIBRect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='warlockIB':
        draw.rect(screen,BLUE,warlockIBRect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='hunterToO':
        draw.rect(screen,BLUE,hunterToORect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='titanToO':
        draw.rect(screen,BLUE,titanToORect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='warlockToO':
        draw.rect(screen,BLUE,warlockToORect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='thorn':
        draw.rect(screen,BLUE,thornRect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='captain':
        draw.rect(screen,BLUE,captainRect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='sparrow':
        draw.rect(screen,BLUE,sparrowRect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='ghost':
        draw.rect(screen,BLUE,ghostRect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='gjallarhorn':
        draw.rect(screen,BLUE,gjallarhornRect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif tool=='tank':
        draw.rect(screen,BLUE,tankRect,3)
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
#############################################################################
#HOVER OVER TOOL (DESCRIPTION RECT)
    if pencilRect.collidepoint(mx,my): #if the mouse is hovered over a specific tool...
        screen.blit(dpencil,(920,530)) #place the description image of that tool in the description rectangle
        draw.rect(screen,BLUE,descriptionRect,3) #draw a blue rectangle around the description rectangle
    elif eraserRect.collidepoint(mx,my):
        screen.blit(deraser,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif fillRect.collidepoint(mx,my):
        screen.blit(dfill,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif lineRect.collidepoint(mx,my):
        screen.blit(dline,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif sprayRect.collidepoint(mx,my):
        screen.blit(dspray,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif freeFormRect.collidepoint(mx,my):
        screen.blit(dfreeform,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif rectRect.collidepoint(mx,my):
        screen.blit(drect,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif rectFillRect.collidepoint(mx,my):
        screen.blit(dfillRect,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif circleRect.collidepoint(mx,my):
        screen.blit(dcircle,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif circleFillRect.collidepoint(mx,my):
        screen.blit(dfillCircle,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
    elif brushRect.collidepoint(mx,my):
       screen.blit(dbrush,(920,530)) 
       draw.rect(screen,BLUE,descriptionRect,3)
    elif fillAreaRect.collidepoint(mx,my):
        screen.blit(dfillarea,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
#############################################################################
#HOVER OVER FUNCTION (DESCRIPTION RECT)
    if clearCanvasRect.collidepoint(mx,my): #if the mouse if hovered over a specific function
        screen.blit(dclearCanvas,(920,530)) #place the description image of that function in the description rectangle
        draw.rect(screen,BLUE,(descriptionRect),3) #draw a blue rectangle around the description rectangle
    elif openRect.collidepoint(mx,my):
        screen.blit(dopen,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif saveRect.collidepoint(mx,my):
        screen.blit(dsave,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif redoRect.collidepoint(mx,my):
        screen.blit(dredo,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif undoRect.collidepoint(mx,my):
        screen.blit(dundo,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
#############################################################################
#HOVER OVER STAMP
    if hunterIBRect.collidepoint(mx,my): #if the mouse if hovered over a specific stamp box
        screen.blit(dStamp,(920,530)) #place the description image of that stamp in the description rectangle
        draw.rect(screen,BLUE,(descriptionRect),3) #draw a blue rectangle around the description rectangle
    elif titanIBRect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif warlockIBRect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif hunterToORect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif titanToORect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif warlockToORect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif thornRect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif captainRect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif sparrowRect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif ghostRect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif gjallarhornRect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
    elif tankRect.collidepoint(mx,my):
        screen.blit(dStamp,(920,530))
        draw.rect(screen,BLUE,(descriptionRect),3)
#############################################################################
#HOVER OVER MUSIC #placed after the other hovers and clicks so it will show up on the screen
    if playRect.collidepoint(mx,my): #if the mouse hovers over a specific music box
        screen.blit(dpause,(920,530)) #place the description of that box on the screen
        draw.rect(screen,BLUE,descriptionRect,3) #draw a blue rectangle around the description rectangle 
        draw.rect(screen,LIGHTBLUE,playRect,3) #draw a light blue rectangle around the music picture
    elif nextRect.collidepoint(mx,my):
        screen.blit(dnext,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,LIGHTBLUE,nextRect,3)
    elif lastRect.collidepoint(mx,my):
        screen.blit(dlast,(920,530))
        draw.rect(screen,BLUE,descriptionRect,3)
        draw.rect(screen,LIGHTBLUE,lastRect,3)
#############################################################################
#CLICK ON MUSIC
    if playRect.collidepoint(mx,my) and mb[0]==1: #if the mouse is pressed on a specific music button
        draw.rect(screen,BLUE,playRect,3) #draw a blue rectangle around that button
    elif nextRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,BLUE,nextRect,3)
    elif lastRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,BLUE,lastRect,3)
#############################################################################
#CHANGE COLOUR
    if colourSpectrumRect.collidepoint(mx,my) and mb[0]==1: #if the mouse id pressed on the colour spectrum rectangle
        col=screen.get_at((mx,my)) #change the current colour to whatever colour the pixel that the mouse clicked on is
        draw.rect(screen,col,currentColourRect) #draw a rectangle of the current colour (indicates the current colour)
        draw.rect(screen,RED,currentColourRect,3) #draw a red rectangle around the current colour rectangle
#############################################################################
#CLEAR CANVAS
    if clearCanvasRect.collidepoint(mx,my) and release: #if the mouse clicks on the clear canvas function
        draw.rect(screen,WHITE,canvasRect) #draw a white rectangle on the canvas (clear is)
        undoCanvas=screen.subsurface(canvasRect).copy() ##copy the current canvas
        undoList.append(undoCanvas) #add that picture to the undo list
#############################################################################
#USING SLIDER
    if mb[0]==1: #if the left mouse button is clicked
        if toolThicknessRect.collidepoint(mx,my) and sliding: #if the mouse if hovering over the slider rectangle and the handle is moving (sliding)
            screen.blit(sliderSurface,(870,530)) #re-blitting the slider rectangle to avoid the many rectangles showing on-top of eachother when moved
            if my<535: #if the mouses vertical position becomes lower than 535
                sliderRect.centery=535 #the slider will automatically be set to 535 so it stays on the handle
            elif my>634: #if the mouses vertical position becomes higher than 634
                sliderRect.centery=634 #the slider will automatically be set to 634 so it stays on the handle
            else: #if the mouse is between these two values
                sliderRect.centery=my #the slider will be set to wherever the mouse is on the handle
            draw.rect(screen,BLACK,handleRect) #draw the handle rectangle
            draw.rect(screen,RED,sliderRect) #draw the slider rectangle based on its y co-ordinate
            toolThickness=sliderRect.centery-534 #thickness becomes a  new number based on where the slider is moved to
    if toolThicknessRect.collidepoint(mx,my): #if the mouse is hovered on the slider rectangle
        screen.blit(dslider,(920,530)) #place the description slider rectangle in the description rectangle
        draw.rect(screen,BLUE,(descriptionRect),3) #draw a blue rectangle around the description rectangle
#############################################################################
#USING TOOL
    if canvasRect.collidepoint(mx,my) and mb[0]==1: #if the mouse is pressed on the canvas
        screen.set_clip(canvasRect) #Only the canvas can be changed
        if tool=='pencil': #if the tool is...
            if toolThickness==1: #if the toolthickness is 1
                draw.line(screen,col,(mx,my),(omx,omy),1) #draw a line based on the old and current mx and my co-ordinates
            else: #if the toolthickness is not one (divide by 2 because the thickness is the radius of the circle, I want it to be the diameter)
                dx=mx-omx #get the change in x
                dy=my-omy #get the change in y
                dist=int(sqrt(dx**2+dy**2))+1 #total distance the mouse has moved
                for i in range(1,dist+1): #for each pixel the mouse has moved
                    dotX=int(omx+i*dx/dist) #get the x-pos of the next circle
                    dotY=int(omy+i*dy/dist) #get the y-pos of the next circle
                    draw.circle(screen,col,(dotX,dotY),toolThickness//2) #draw the circle
        elif tool=='eraser':
            if toolThickness==1: #if the toolthickness is 1
                draw.line(screen,WHITE,(mx,my),(omx,omy),1) #draw a line based on the old and current mx and my co-ordinates
            else: #if the toolthickness is not one (divide by 2 because the thickness is the radius of the circle, I want it to be the diameter)
                dx=mx-omx #get the change in x
                dy=my-omy #get the change in y
                dist=int(sqrt(dx**2+dy**2))+1 #total distance the mouse has moved
                for i in range(1,dist+1): #for each pixel the mouse has moved
                    dotX=int(omx+i*dx/dist) #get the x-pos of the next circle
                    dotY=int(omy+i*dy/dist) #get the y-pos of the next circle
                    draw.circle(screen,WHITE,(dotX,dotY),toolThickness//2) #draw the circle
        elif tool=='fill':
            draw.rect(screen,col,(canvasRect)) #making the entire canvas the selected colour
        elif tool=='line':
            screen.blit(back,(0,0)) #re-bliting the canvas so the line is not repeatedly placed on the screen
            if toolThickness==1: #if the toolthickness is 1
                draw.line(screen,col,start,(mx,my),toolThickness) #draw a line based on the beginning and current mx and my co-ordinates
            else: #if the toolthickness is not one (divide by 2 because the thickness is the radius of the circle, I want it to be the diameter)
                dx=mx-start[0] #get the change in x
                dy=my-start[1] #get the change in y
                dist=int(sqrt(dx**2+dy**2))+1 #total distance the mouse has moved
                for i in range(1,dist+1): #for each pixel the mouse has moved
                    dotX=int(start[0]+i*dx/dist) #get the x-pos of the next circle
                    dotY=int(start[1]+i*dy/dist) #get the y-pos of the next circle
                    draw.circle(screen,col,(dotX,dotY),toolThickness//2) #draw the circle (line)
            
        elif tool=='spray':
            if toolThickness==1: #if the toolthickness is 1
                for i in range(toolThickness): #determines how fast the spray tool will work
                    x=randint(-1*toolThickness//2,toolThickness//2) #generate a random x value between half of the negative and positive toolthickness
                    y=randint(-1*toolThickness//2,toolThickness//2) #generate a random y value between half of the negative and positive toolthickness
                    if hypot(x,y)<=toolThickness//2: #if the point is within the range of the toolthickness circle
                        screen.set_at((x+mx,y+my),col) #change that specific pixel the selected colour
            else: #if the toolthickness is not one (divide by 2 because the thickness is the radius of the circle, I want it to be the diameter)
                for i in range(toolThickness//2): #determines how fast the spray tool will work
                    x=randint(-1*toolThickness//2,toolThickness//2) #generate a random x value between half of the negative and positive toolthickness
                    y=randint(-1*toolThickness//2,toolThickness//2) #generate a random y value between half of the negative and positive toolthickness
                    if hypot(x,y)<=toolThickness//2: #if the point is within the range of the toolthickness circle
                        screen.set_at((x+mx,y+my),col) #change that specific pixel the selected colour
        elif tool=='free form':
            pointList=[(mx, my)] #point list, starts with where the mouse first clicks
            while True:
                for evt in event.get(): #the event queue loop
                    if evt.type==MOUSEBUTTONDOWN: #if the mouse is pressed
                        point=evt.pos #get the coordinates of where the mouse clicks
                        pointList.append(point) #add that point to a list
                        draw.lines(screen,col,False,pointList,1) #draw a line based on two co-ordinates in the pointList
                        display.update() #draw each line as a new point is put into the list
                        drawing=False #no longer drawing
                if evt.type==KEYDOWN: #is a key is pressed
                    if evt.key==K_RETURN: #if the pressed key is ENTER
                        try: #while there are more than 2 points in the pointList
                            draw.lines(screen,col,True,pointList,1) #draw the final line that uses the last two points in the list
                            undoCanvas=screen.subsurface(canvasRect).copy() #copy the current canvas
                            undoList.append(undoCanvas) #add that picture to the undo list
                            break #end the loop (no longer using this tool)
                        except ValueError: #is there is only two points in the pointList when enter is clicked (avoids crashing)
                            undoCanvas=screen.subsurface(canvasRect).copy() #copy the current canvas
                            undoList.append(undoCanvas) #add that picture to the undo list
                            break #end the loop (no longer using this tool)
        elif tool=='rect':
            if toolThickness%2==1: #if thickness is odd
                screen.blit(back,(0,0)) #re-bliting the canvas so the rectangle is not repeatedly placed on the screen
                draw.rect(screen,col,(start[0],start[1],mx-start[0],my-start[1]),toolThickness) #rectagle
                draw.rect(screen,col,(start[0]-toolThickness//2,start[1]-toolThickness//2,toolThickness,toolThickness)) #top left fill
                draw.rect(screen,col,(start[0]-toolThickness//2-(start[0]-mx+1),start[1]-toolThickness//2,toolThickness,toolThickness)) #top right fill
                draw.rect(screen,col,(start[0]-toolThickness//2,start[1]-toolThickness//2-(start[1]-my+1),toolThickness,toolThickness)) #bottom left fill
                draw.rect(screen,col,(start[0]-toolThickness//2-(start[0]-mx+1),start[1]-toolThickness//2-(start[1]-my+1),toolThickness,toolThickness)) #bottom right fill
            elif toolThickness%2==0: #if thickness is even
                screen.blit(back,(0,0)) #re-bliting the canvas so the rectangle is not repeatedly placed on the screen
                draw.rect(screen,col,(start[0],start[1],mx-start[0],my-start[1]),toolThickness) #rectagle
                draw.rect(screen,col,(start[0]-toolThickness//2+1,start[1]-toolThickness//2+1,toolThickness,toolThickness)) #top left fill
                draw.rect(screen,col,(start[0]-toolThickness//2-(start[0]-mx),start[1]-toolThickness//2+1,toolThickness,toolThickness)) #top right fill
                draw.rect(screen,col,(start[0]-toolThickness//2+1,start[1]-toolThickness//2-(start[1]-my),toolThickness,toolThickness)) #bottom left fill
                draw.rect(screen,col,(start[0]-toolThickness//2-(start[0]-mx),start[1]-toolThickness//2-(start[1]-my),toolThickness,toolThickness)) #bottom right fill
                draw.rect(screen,col,[start[0],start[1],mx-start[0],my-start[1]],toolThickness)
        elif tool=='fill rect':
            screen.blit(back,(0,0)) #re-bliting the canvas so the rectangle is not repeatedly placed on the screen
            draw.rect(screen,col,[start[0],start[1],mx-start[0],my-start[1]]) #draw the filled rectangle on the screen
        elif tool=='circle':
            try:
                screen.blit(back,(0,0)) #re-bliting the canvas so the circle is not repeatedly placed on the screen
                ellRect=Rect(start[0],start[1],mx*1.1-start[0],my*1.1-start[1]) #creating the circle
                ellRect.normalize() #normalizing the circle (all values become positive)
                draw.ellipse(screen,col,ellRect,toolThickness) #drawing the circle with thickness
            except ValueError: #if the thickness is greater than the radius
                draw.ellipse(screen,col,ellRect) #draw a filled circle
        elif tool=='fill circle':
            screen.blit(back,(0,0)) #re-bliting the canvas so the circle is not repeatedly placed on the screen
            ellRect=Rect(start[0],start[1],mx*1.1-start[0],my*1.1-start[1]) #creating the circle
            ellRect.normalize() #normalizing the circle (all values pecome positive)
            draw.ellipse(screen,col,ellRect) #draw a filled circle
        elif tool=='brush':
            if toolThickness==1: #if the toolthickness is 1
                draw.circle(brushHead,(col[0],col[1],col[2],5),(toolThickness,toolThickness),toolThickness)  #draw an opaque circle onto a transparent surface (brushhead)
                dx=mx-omx #get the change in x
                dy=my-omy #get the change in y
                dist=int(sqrt(dx**2+dy**2))+1 #total distance the mouse has moved
                for i in range(1,dist+1): #for each pixel the mouse has moved
                    dotX=int(omx+i*dx/dist) #get the x-pos of the next circle
                    dotY=int(omy+i*dy/dist) #get the y-pos of the next circle
                    screen.blit(brushHead,(dotX-toolThickness,dotY-toolThickness)) #draw the brush head and the transparent circle to the screen
            else: #if the toolthickness is not one (divide by 2 because the thickness is the radius of the circle, I want it to be the diameter)
                draw.circle(brushHead,(col[0],col[1],col[2],5),(toolThickness,toolThickness),toolThickness//2) #draw an opaque circle onto a transparent surface (brushhead)
                dx=mx-omx #get the change in x
                dy=my-omy #get the change in y
                dist=int(sqrt(dx**2+dy**2))+1 #total distance the mouse has moved
                for i in range(1,dist+1): #for each pixel the mouse has moved
                    dotX=int(omx+i*dx/dist) #get the x-pos of the next circle
                    dotY=int(omy+i*dy/dist) #get the y-pos of the next circle
                    screen.blit(brushHead,(dotX-toolThickness,dotY-toolThickness)) #draw the brush head and the transparent circle to the screen
        elif tool=='fill area':
            mainColour=screen.get_at((mx,my)) #get the pixel colour of there the mouse click
            pointList=[(mx,my)] #pointList for where the mouse first clicks
            usedPointSet=set() #set for all used points so they do not get used again
            while len(pointList)>0: #if there is a value in the pointList
                pixel=pointList.pop() #the last value in the pointList is removed and is now the 'pixel' variable
                if mainColour==screen.get_at(pixel) and pixel not in usedPointSet: #if the pixel is the same colour as the pixel first clicked on and it has not already been changed/used
                    screen.set_at(pixel,col) #change that pixel to the selected colour
                    pointList.append((pixel[0]+1,pixel[1])) #add the point to the right of the pixel to the pointList for it to be checked next
                    pointList.append((pixel[0]-1,pixel[1])) #add the point to the left of the pixel to the pointList for it to be checked next
                    pointList.append((pixel[0],pixel[1]+1)) #add the point to the bottom of the pixel to the pointList for it to be checked next
                    pointList.append((pixel[0],pixel[1]-1)) #add the point to the top of the pixel to the pointList for it to be checked next
                usedPointSet.add(pixel) #add the changed/used pixel to the usedPointSet
        elif tool=='clear canvas':
            draw.rect(screen,WHITE,canvasRect) #draw a white rectangle on the canvas (clearing it)
#############################################################################
#USING STAMP TOOL
        elif tool=='hunterIB': #if the current stamp (tool) is...
            screen.blit(back,(0,0)) #re-blit the original screen so the stamo does not overlap on itself
            screen.blit(hunterIBStamp,(mx-60,my-102)) #blit the stamp onto the screen (subtract from mx and my to center the mouse on the stamp)
        elif tool=='titanIB':
            screen.blit(back,(0,0))
            screen.blit(titanIBStamp,(mx-70,my-112))
        elif tool=='warlockIB':
            screen.blit(back,(0,0))
            screen.blit(warlockIBStamp,(mx-60,my-122))
        elif tool=='hunterToO':
            screen.blit(back,(0,0))
            screen.blit(hunterToOStamp,(mx-50,my-112))
        elif tool=='titanToO':
            screen.blit(back,(0,0))
            screen.blit(titanToOStamp,(mx-50,my-112))
        elif tool=='warlockToO':
            screen.blit(back,(0,0))
            screen.blit(warlockToOStamp,(mx-35,my-122))
        elif tool=='thorn':
            screen.blit(back,(0,0))
            screen.blit(thornStamp,(mx-100,my-56))
        elif tool=='captain':
            screen.blit(back,(0,0))
            screen.blit(captainStamp,(mx-80,my-90))
        elif tool=='sparrow':
            screen.blit(back,(0,0))
            screen.blit(sparrowStamp,(mx-110,my-50))
        elif tool=='ghost':
            screen.blit(back,(0,0))
            screen.blit(ghostStamp,(mx-50,my-40))
        elif tool=='gjallarhorn':
            screen.blit(back,(0,0))
            screen.blit(gjallarhornStamp,(mx-100,my-27))
        elif tool=='tank':
            screen.blit(back,(0,0))
            screen.blit(tankStamp,(mx-100,my-50))
        screen.set_clip(None) #everything else can now be changed/edited
#############################################################################
#SAVE FILE
    if saveRect.collidepoint(mx,my) and release: #if mouse if released on the save box
        fname=filedialog.asksaveasfilename(defaultextension=".png") #ask for file name
        if fname: #if there is a file name inputed
            image.save(screen.subsurface(canvasRect),fname) #save the image/drawing from the canvas to the computer
            undoCanvas=screen.subsurface(canvasRect).copy() #copy the current canvas
            undoList.append(undoCanvas) #add that picture to the undo list
#############################################################################
#OPEN FILE
    if openRect.collidepoint(mx,my) and release: #if mouse if released on the open box
        fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.bmp")]) #ask for file name
        if fname: #if there is a file name chosen
            fname=image.load(fname) #load the selected image
            fname=transform.scale(fname,(790,502)) #make the selected image the size and scale of the canvas
            draw.rect(screen,WHITE,canvasRect) #will help if the picture loaded is transparent
            screen.blit(fname,(400,10)) #placing the picture on the screen
            undoCanvas=screen.subsurface(canvasRect).copy() #copy the current canvas
            undoList.append(undoCanvas) #add that picture to the undo list
#############################################################################
    omx,omy=mx,my #reseting old mx and old my
    brushHead=Surface((200,200),SRCALPHA) #reseting the brush tool
    release=False #mouse is no longer released
    display.flip() #update the full display Surface to the screen
quit()
#############################################################################
