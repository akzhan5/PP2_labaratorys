import pygame 
import math 
from pygame.locals import * 

pygame.init() 

#variables 
display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()  

prevX = -1 
prevY = -1 
currentX = -1 
currentY= -1 
isMouseButtonDown = False 

baseLayer = pygame.Surface((800,800))

def caclulateCircleRadius(x1, y1, x2,y2): 
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    rad = d/2 
    center = ((x1+x2)/2, (y1+y2)/2) 
    return rad, center
    
while True: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 

        if event.type == MOUSEBUTTONDOWN: 
            if event.button == 1: #right button of the mouse was pushed down 
                isMouseButtonDown = True 
                prevX = event.pos[0] 
                prevY = event.pos[1] 
                currentX = event.pos[0]
                currentY = event.pos[1] 

        if event.type == MOUSEBUTTONUP: 
            isMouseButtonDown = False 
            prevX = -1 
            prevY = -1 
            currentX = -1 
            currentY = -1 
            #blit is used to blit child surface on parent surface on a given coord 
            baseLayer.blit(display, (0,0))

        if event.type == MOUSEMOTION: 
            if isMouseButtonDown: #mousedown then current pos of the mouse should be updated each time is it moving while mouse is pressed
                currentX = event.pos[0] 
                currentY = event.pos[1] 

    #if mouse is pressed and the prev and current pos are changed then basaelayer is blitted on the display and rect is calculated and drawn on the display 
    if isMouseButtonDown == True and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1: 
        display.blit(baseLayer, (0,0)) 
        rad, center = caclulateCircleRadius(prevX, prevY, currentX, currentY) 
        pygame.draw.circle(display, (255,255,255), center, rad, 1)

    pygame.display.update() 
    clock.tick(60) 