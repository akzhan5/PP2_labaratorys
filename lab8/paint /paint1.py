#getting a series of events: pygame.event.get() - returns a list of all the events since emptying queue 
#check the event type event.type (attribute of the object) 
#check for events by polling the state of keys or buttons: 
#1 pygame.key.get_pressed() - list of bool that correspond to the key's being pressed or not as an index. Ex: pygame.key.get_pressed()[pygame.K_TAB] = True: K_TAB was get_pressed
#2 pygame.mouse.get_pos() - returns the coord of the mouse cursor. (0,0) - the beginning coord 
#3 pygame.mouse.get_pressed() - returns the state of each mouse button in a tuple: left, middle, right buttons. 
import pygame 
from pygame.locals import * 

pygame.init() 

#variables 
height = 600
width = 600 
radius = 15 
mode = (255,255,255)
points = [] #pos of the mouse during the motion
clock = pygame.time.Clock() #obj of class Clock
#display
display = pygame.display.set_mode((height, width)) 
pygame.display.set_caption('Paint')


#draw line (with circles) 
def drawLine(surface, index, start, end, width, mode): 
    global radius
    c1 = max(0, min(255, 2 * index - 256)) #0
    c2 = max(0, min(255, 2 * index)) #color
    color = (255,255,255)
    #mode is red
    if mode == (255,0,0): 
        color = (c2, c1, c1) 
    #mode is green 
    elif mode == (0,255,0): 
        color = (c1,c2,c1) 
    #mode is blue 
    elif mode == (0,0,255): 
        color = (c1,c1,c2) 
    
    #the process of drawing itself 
    #change in x,y: 
    dx = end[0] - start[0] 
    dy = end[1] - start[1] 
    iterations = max(abs(dx), abs(dy)) 

    for i in range(iterations): 
        progress = 1.0 * i / iterations 
        aprogress = 1 - progress

        x = int(aprogress * start[0] + progress * end[0]) 
        y = int(aprogress * start[1] + progress * end[1]) 

        pygame.draw.circle(surface, color, (x,y), width) #width of the line is actually the radius of the circles 

#loop itself 
done = False 
while not done: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            done = True 
        #check for mouse event
        if event.type == MOUSEBUTTONDOWN: 
            #left click grows radius: 
            if event.button == 1: 
                radius = min (200, radius +1) #no more than 200, but will grow each click +1
            #right click shrinks the radius: 
            if event.button == 3: 
                radius = max (radius-1, 1) #no less than 1, but will shrink each click -1 
        #check for key event 
        if event.type == KEYDOWN: 
            if event.key == K_r: 
                mode = (255, 0, 0) 
            if event.key == K_g: 
                mode = (0,255,0) 
            if event.key == K_b: 
                mode = (0,0,255)
        #check for the motion of the mouse: 
        if event.type == MOUSEMOTION: 
            pos = event.pos 
            points = points + [pos] #add the new elements pos to the end of the list list + [el]
            points = points[-256:] #starting from the 256 elements counting from the back, till the last element. It means that till the moment there are 257 elements all the 256 will be in the list, when there are 257, the first one in the beginning fades away 

    #fill display with black 
    display.fill((0,0,0)) 

    i = 0
    #draw all the pos in the points list till is less than len of points -1 (because index starts from 0)
    while i<len(points)-1: 
        drawLine(display, i, points[i], points[i+1], radius, mode)
        i+=1

    #update the display to show all the changes done 
    pygame.display.update() 
    clock.tick(60) 

