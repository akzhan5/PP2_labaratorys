import pygame 
import sys
import random 
import time
from pygame.locals import *
pygame.init()

#variables
black = (0,0,0) 
line_col = (50,50,50)
height = 400
width = 400 
cell_width = 20 


#fonts 
font_style = pygame.font.SysFont('Times New Roman', 40) 
font2 = pygame.font.SysFont('Times New Roman', 20)

#classes 
class Point: 
    def __init__(self, x ,y): 
        self.x= x 
        self.y = y

class Food: 
    def __init__(self): 
        self.location = Point(random.randint(0, 19), random.randint(0, 19))

    def draw(self): 
        point = self.location 
        rect = pygame.Rect(point.x * cell_width, point.y * cell_width, cell_width, cell_width) 
        pygame.draw.rect(display, (0, 0, 255), rect)
    
    def generateLocation(self, snake, wall):
        good = False
        while good == False:
            self.location = Point(random.randint(0, 19), random.randint(0, 19))
            good = True
            #check whether false onto level and score: 
            if self.location.x == 10: 
                if self.location.y == 0 or self.location.y == 20: 
                    good = False
            #check whether coor of food fall to the body of the snake 
            for p in snake:
                if p.x == self.location.x:
                    if p.y == self.location.y: #if coor of the food and the snake are the same then good is False and location is generated once again 
                        good = False
                        break 
            #check whether coor of the food fall to the coord of the wall 
            for b in wall: 
                if b.x == self.location.x: 
                    if b.y == self.location.y: #if coord of food and the wall are the same: good is False, while runs again and generates new pos for the food 
                        good = False  
                        break 


food = Food()

class Wall:
    def __init__(self, level):
        self.body = [] #saves all the points of the wall 
        self.level = level #level of the current map 

        f = open('level{}.txt'.format(self.level), 'r') #opens the file in a readible format

        lines = f.readlines() #list of type string
        for y in range (0, len(lines)): #each line as a string
            for x in range(0, 20): #each character of a string
                if lines[y][x] == '#': #runs through the lines and their characters each if its equal to # then we append the point
                   self.body.append(Point(x, y))

    def draw(self): 
        for brick in self.body: 
            rect = pygame.Rect(brick.x * cell_width, brick.y * cell_width, cell_width, cell_width)
            pygame.draw.rect(display, (226, 235,67), rect)

class Snake: 
    def __init__(self): 
        self.body = [Point(10,11)] #list of points 
        self.speed = 5
        self.score = 0 
        self.dx = 0 
        self.dy = 0 #changes in loc of the head 
    
    def move(self): 
        for i in range(len(self.body)-1, 0, -1): 
            self.body[i].x = self.body[i-1].x #the last part takes the pos of the previous parts x coord 
            self.body[i].y = self.body[i-1].y #the last part takes the pos of the prev parts y coord

        self.body[0].x += self.dx #change in loc of x coord head accor to user 
        self.body[0].y += self.dy #change in loc of y coord head accor to user 

    def check_for_bound(self): 
        #if hits the boundaies -> game_over 
        if self.body[0].x * cell_width >= width or self.body[0].x < 0 or self.body[0].y *cell_width>= height or self.body[0].y <0: 
            return True

    def draw(self): 
        #head first 
        rect = pygame.Rect(self.body[0].x * cell_width, self.body[0].y * cell_width, cell_width, cell_width)
        pygame.draw.rect(display, (255,0,0), rect) 
        #loop draw the body 
        for point in self.body[1:]: #below the head till the end 
            rect = pygame.Rect(point.x* cell_width, point.y* cell_width, cell_width, cell_width)
            pygame.draw.rect(display, (0,255,0), rect)

    #check whether snake collides with the food: 
    def collision_food(self, food): 
        if self.body[0].x == food.location.x: 
            if self.body[0].y == food.location.y: 
                self.body.append(Point(food.location.x, food.location.y))
                snake.score +=1 
                return True
        return False

    def collision_wall(self, wall): 
        for b in wall: 
            if self.body[0].x == b.x: 
                if self.body[0].y == b.y: 
                    return True 

    def collision_self(self): 
        for point in self.body[1:]: 
            if self.body[0].x == point.x: 
                if self.body[0].y == point.y: 
                    return True 


snake = Snake()

def main(): 
    global display, clock, last_change_in_y, last_change_in_x
    display = pygame.display.set_mode((height, width)) 
    clock = pygame.time.Clock() 
    display.fill(black) 
    wall = Wall(1)
    print(len(wall.body))
    #game loop 
    while True: 

        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit()
            if event.type == KEYDOWN: 
                if event.key == K_UP: 
                    snake.dy = -1
                    snake.dx = 0
                if event.key == K_DOWN: 
                    snake.dy = 1 
                    snake.dx = 0
                if event.key == K_RIGHT: 
                    snake.dx = 1 
                    snake.dy = 0 
                if event.key == K_LEFT: 
                    snake.dx = -1 
                    snake.dy = 0

        snake.move() #changes in movement// loc of body parts as points 
        #after the change the screen is filled with black, draw grid is done again and the prev frame disappears, the new with the new pos appears
        if(snake.collision_food(food)):
            food.generateLocation(snake.body, wall.body)
            if snake.score % 5==0 and wall.level < 2: 
                wall.level +=1 
                snake.speed += 0.5
        
        display.fill(black) #erases the prev pos 
        drawGrid()
        snake.draw()
        food.draw() 

        if snake.score == 5: 
            wall = Wall(2)
            snake.speed = 6.5

        wall.draw() 

        if snake.collision_wall(wall.body): 
            wall_coll = font_style.render('Wall Collision', True, (255, 0,0)) 
            game_over = font_style.render("GAME OVER", True, (255,0,0))
            display.fill(black) 
            display.blit(wall_coll, (100, 100))
            display.blit(game_over, (100, 200)) 
            pygame.display.update() 
            time.sleep(2)
            pygame.quit()
        
        #if snake.collision_self(): 
            #self_coll = font_style.render('Collision with myself', True, (255, 0, 0)) 
            #game_over = font_style.render("GAME OVER", True, (255,0,0))
            #display.fill(black) 
            #display.blit(self_coll, (100, 100)) 
            #display.blit(game_over, (100, 200)) 
            #pygame.display.update() 
            #time.sleep(2) 
            #pygame.quit() 


        if snake.check_for_bound():
            bound = font_style.render('Out of the area!', True, (255, 0, 0))
            game_over = font_style.render("GAME OVER", True, (255,0,0))
            display.fill(black)
            display.blit(bound, (100, 100))
            display.blit(game_over, (100,200))
            pygame.display.update()
            time.sleep(2) 
            pygame.quit()

        score_card = font2.render('Score: ' + str(snake.score), True, (255, 255, 255))
        level_card = font2.render('Level: ' + str(wall.level), True, (255, 255, 255))
        display.blit(score_card, (10, 0))
        display.blit(level_card, (10, 20))
        pygame.display.update()
        clock.tick(snake.speed) # snake.speed frames per second/ in other words the slower snake moves the less frames are shown in a second 

#in order to make it easier for us to navigate through the display's coord 
def drawGrid(): 
    for x in range(0, width, cell_width): 
        for y in range(0, height, cell_width): 
            rect = pygame.Rect(x,y, cell_width, cell_width)
            pygame.draw.rect(display, line_col, rect, 1)


main()