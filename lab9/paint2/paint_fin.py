import pygame 
from pygame.locals import *
import math
pygame.init() 
#variables 
display = pygame.display.set_mode((800,800)) 
clock = pygame.time.Clock() 

display.fill((0,0,0)) 
baseLayer = pygame.Surface((800, 800))

#colors 
red = (255,0,0) 
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

isMouseButtonDown = False

def getRect(x1, x2, y1, y2): 
    return Rect(min(x1,x2), min(y1,y2), abs(x1 -x2), abs(y1-y2))

#classes: 
class Colors: 
    def __init__(self): 
        self.am = white
color = Colors()

class Width: 
    def __init__(self): 
        self.am = 1
width = Width()

class Pen: 
    def __init__(self):
        self.prevX = -1 
        self.prevY = -1 
        self.currentX = -1 
        self.currentY = -1
        self.on = True

    def use(self, surface, color, width): 
        pygame.draw.line(surface, color, (self.prevX, self.prevY), (self.currentX, self.currentY), width)
        self.prevX = self.currentX
        self.prevY = self.currentY 
pen = Pen()

class Rectangle: 
    def __init__(self): 
        self.prevX = -1 
        self.prevY = -1 
        self.currentX = -1 
        self.currentY = -1
        self.on = False 

    def calculateRect(self): 
        return Rect(min(self.prevX,self.currentX), min(self.prevY, self.currentY), abs(self.prevX - self.currentX), abs(self.prevY- self.currentY))
    
    def use (self, surface, color, rect, width): 
        global baseLayer
        surface.blit(baseLayer, (0,0))
        pygame.draw.rect(surface, color, Rect(rect), width)    
rect = Rectangle()

class Circlee: 
    def __init__(self): 
        self.prevX = -1 
        self.prevY = -1 
        self.currentX = -1 
        self.currentY = -1
        self.on = False

    def caclulateCircleRadius(self): 
        d = math.sqrt((self.currentX - self.prevX)**2 + (self.currentY - self.prevY)**2)
        rad = d/2 
        return rad
    
    def calculateCircleCenter(self): 
         center = ((self.prevX+ self.currentX)/2, (self.prevY+ self.currentY)/2) 
         return center

    def use(self, surface, color, rad, center, width): 
        global baseLayer 
        surface.blit(baseLayer, (0,0)) 
        pygame.draw.circle(display, color, center, rad, width)
circle = Circlee()

class Square: 
     def __init__(self): 
        self.prevX = -1 
        self.prevY = -1 
        self.currentX = -1 
        self.currentY = -1
        self.on = False

     def calculateVertices(self):
        r = getRect(self.prevX, self.currentX, self.prevY, self.currentY)
        p1 = r.topleft
        p2 = (r.left + r.height, r.top)
        p3 = (r.left + r.height, r.bottom)
        p4 = r.bottomleft
        return [p1, p2, p3, p4]
     
     def use(self, surface, color, vertices, width): 
        global baseLayer 
        surface.blit(baseLayer, (0,0)) 
        pygame.draw.polygon(surface, color, vertices, width) 
square = Square()

class Eraser: 
    def __init__(self):
        self.prevX = -1 
        self.prevY = -1 
        self.currentX = -1 
        self.currentY = -1
        self.on = False

    def use(self, surface, width): 
        pygame.draw.line(surface, (0,0,0), (self.prevX, self.prevY), (self.currentX, self.currentY), width)
        self.prevX = self.currentX
        self.prevY = self.currentY 
eraser = Eraser() 

class RightTriangle: 
    def __init__(self): 
        self.prevX = -1 
        self.prevY = -1 
        self.currentX = -1 
        self.currentY = -1
        self.on = False
    
    def calculateVertices(self): 
        #rectangle we would work with 
        r = getRect(self.prevX,self.currentX,self.prevY,self.currentY)
        if self.currentX>self.prevX: 
            p1 = r.topleft
            p2 = r.bottomleft
            p3 = r.bottomright
        elif self.currentX<=self.prevX: 
            p1 = r.topright 
            p2 = r.bottomright
            p3 = r.bottomleft
        return [p1, p2, p3]
    
    def use(self, surface, color, vertices, width): 
        global baseLayer 
        surface.blit(baseLayer, (0,0)) #blit the baseLayer which saved all the prev changes on the display on the clear updated display 
        pygame.draw.polygon(surface, color, vertices, width) 
right = RightTriangle()

class EquilateralTriangle: 
    def __init__(self): 
        self.prevX = -1 
        self.prevY = -1 
        self.currentX = -1 
        self.currentY = -1
        self.on = False
    
    def calculateVertices(self): 
        r = getRect(self.prevX, self.currentX, self.prevY, self.currentY)
        p1 = r.bottomleft
        p2 = r.bottomright
        #median length of equilat triangle h = 0.75 * a**2 where a - is the width of rect 
        p3 = (r.centerx, r.bottom - math.sqrt(0.75 * r.width**2))
        return [p1, p2, p3]
    
    def use (self, surface, color, vertices, width): 
        global baseLayer 
        surface.blit(baseLayer, (0,0)) 
        pygame.draw.polygon(surface, color, vertices, width)
equi = EquilateralTriangle()

class Rhombus: 
    def __init__(self): 
        self.prevX = -1 
        self.prevY = -1 
        self.currentX = -1 
        self.currentY = -1
        self.on = False
    
    def calculateVertices(self):
        r = getRect(self.prevX, self.currentX, self.prevY, self.currentY)
        p1 = r.midtop
        p2 = r.midleft
        p3 = r.midbottom
        p4 = r.midright
        return [p1, p2, p3, p4]
    
    def use(self, surface, color, vertices, width): 
        global baseLayer 
        surface.blit(baseLayer, (0,0)) 
        pygame.draw.polygon(surface, color, vertices, width)
romb = Rhombus()

instruments = [pen, rect, circle, square, eraser, right, equi, romb]

while True: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
        
        if event.type == KEYDOWN: 
            if event.key == K_p: 
                for i in instruments: 
                    if i==pen: i.on = True
                    else: i.on = False
            if event.key == K_r: 
                for i in instruments: 
                    if i==rect: i.on = True
                    else: i.on = False
            if event.key == K_c: 
                for i in instruments: 
                    if i==circle: i.on = True
                    else: i.on = False
            if event.key == K_s: 
                for i in instruments: 
                    if i==square: i.on = True
                    else: i.on = False
            if event.key == K_e: 
                for i in instruments: 
                    if i==eraser: i.on = True
                    else: i.on = False
            if event.key == K_t:
                for i in instruments: 
                    if i==right: i.on = True
                    else: i.on = False
            if event.key == K_l: 
                for i in instruments: 
                    if i==equi: i.on = True
                    else: i.on = False
            if event.key == K_o: 
                for i in instruments: 
                    if i==romb: i.on = True
                    else: i.on = False
            if event.key == K_UP: 
                width.am+=1
            if event.key == K_DOWN: 
                if width.am>=2:
                    width.am -=1
                

        if event.type == MOUSEBUTTONDOWN: 
            if event.button  == 1: 
                isMouseButtonDown = True 
                if event.pos[1] >=20 and event.pos[1] <=40: 
                    if event.pos[0] >= 10 and event.pos[0] <=30: color.am = red
                    elif event.pos[0] >= 40 and event.pos[0] <=60: color.am = green 
                    elif event.pos[0] >= 70 and event.pos[0] <= 90: color.am = blue
                    elif event.pos[0] >=100 and event.pos[0] <= 120: color.am = white
                else: 
                    for i in instruments: 
                        if i.on: 
                            i.prevX = event.pos[0] 
                            i.prevY = event.pos[1] 
                            i.currentX = event.pos[0]
                            i.currentY = event.pos[1]
                            break
                

        if event.type == MOUSEBUTTONUP: 
            isMouseButtonDown = False 
            baseLayer.blit(display, (0,0))
            for i in instruments: 
                    if i.on: 
                        i.prevX = -1
                        i.prevY = -1
                        i.currentX = -1
                        i.currentY = -1

        #mouse motion if mouse moved add the point to the list 
        if event.type == MOUSEMOTION: 
            #event.pos attribute of the tuple of the pos of the event 
            if isMouseButtonDown:
                for i in instruments: 
                    if i.on: 
                        i.currentX = event.pos[0]
                        i.currentY = event.pos[1]

    #color panel 
    pygame.draw.rect(display, red, Rect(10, 20, 20, 20))
    pygame.draw.rect(display, green, Rect(40, 20, 20, 20)) 
    pygame.draw.rect(display, blue, Rect(70, 20, 20, 20))
    pygame.draw.rect(display, white, Rect(100, 20, 20, 20))

    if isMouseButtonDown: 
        for i in instruments: 
            if i.on: 
                if i.currentX != -1 and i.currentY != -1 and i.prevX != -1 and i.prevY != -1: 
                    if i == rect: 
                        r = i.calculateRect()
                        i.use(display, color.am, r, width.am)
                    elif i == circle: 
                        rad = circle.caclulateCircleRadius() 
                        center = circle.calculateCircleCenter()
                        i.use (display, color.am, rad, center, width.am)
                    elif i==pen: i.use(display, color.am, width.am)
                    elif i==eraser: i.use(display, width.am)
                    else: 
                        vertices = i.calculateVertices()
                        i.use(display, color.am, vertices, width.am)

    pygame.display.update() 
    clock.tick(60)


        
        
