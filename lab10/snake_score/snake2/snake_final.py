import pygame 
import sys
import random 
import time
from pygame.locals import *
from user import user_inp
from score import score 

pygame.init()

#variables
black = (0,0,0) 
line_col = (50,50,50)
height = 400
width = 400 
cell_width = 20 
im = pygame.image.load('apple.png')
apple_i= pygame.transform.scale(im,(cell_width, cell_width))

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
            #check whether coord of food fall to the body of the snake 
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

class FoodExtra: 
    def __init__(self, image): 
        self.image = image 
        self.location = Point(random.randint(0,19), random.randint(0,19)) 
        
    def rect(self): 
        point = self.location 
        rect = pygame.Rect(point.x*cell_width, point.y*cell_width, cell_width, cell_width) 
        return rect

    def generateLocation(self, snake, wall):
        good = False
        while good== False: 
            self.location = Point(random.randint(0,19), random.randint(0,19)) 
            good = True
            #check whether false onto level and score: 
            if self.location.x == 10: 
                if self.location.y == 0 or self.location.y == 20: 
                    good = False
            #check whether food falls onto the snake body when location is generated 
            for p in snake: 
                if p.x == self.location.x: 
                    if p.y == self.location.y: 
                        good = False 
                        break 
            #check whether food falls on the walls when location is generated 
            for b in wall:
                if b.x == self.location.x: 
                    if b.y == self.location.y: 
                        good = False 
                        break 
apple = FoodExtra(apple_i)
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
        self.speed = 7
        self.score = 0 
        self.dx = 0 
        self.dy = 0 #changes in loc of the head 
    
    def move(self): 
        for i in range(len(self.body)-1, 0, -1): 
            self.body[i].x = self.body[i-1].x #the last part takes the pos of the previous parts x coord 
            self.body[i].y = self.body[i-1].y #the last part takes the pos of the prev parts y coord

        self.body[0].x += self.dx #change in loc of x coord head accor to user input
        self.body[0].y += self.dy #change in loc of y coord head accor to user input

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

foods = [food, apple] 

#set the timer for an event to disappear after 3s and appear in a new location 
disappear = USEREVENT +1 
pygame.time.set_timer(disappear, 3000)

display = pygame.display.set_mode((height, width)) 
clock = pygame.time.Clock() 


def main(): 
    global display, clock 
    wall = Wall(1)

    name = get_username(display)

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
            #after 3s, disappear event is called on the event queue and the current food's new location is generated
            if event.type == disappear: 
                if f==food: 
                    #f = random.choice(foods) #random food is chosen after each 3s, however when it is commented the food will change its pos till its eaten by the user
                    food.generateLocation(snake.body, wall.body) #foods pos is upd
                else: 
                    #f = random.choice(foods) 
                    apple.generateLocation(snake.body, wall.body)

        snake.move() #changes in movement// loc of body parts as points 

        #check for self collision with its body
        if snake.collision_self(): 
            self_coll = font_style.render('Collision with myself', True, (255, 0, 0)) 
            game_over = font_style.render("GAME OVER", True, (255,0,0))

            #add the userscore and level to the table  
            score(name, snake.score, wall.level)

            display.fill(black) 
            display.blit(self_coll, (50, 100)) 
            display.blit(game_over, (100, 200)) 
            pygame.display.update() 
            time.sleep(2) 
            pygame.quit() 

        #after the change the screen is filled with black, draw grid is done again and the prev frame disappears, the new with the new pos appears
        for fo in foods: 
            if(snake.collision_food(fo)):
                #apple has more weight than the simple food 
                if fo==apple: snake.score += 3 
                else: snake.score +=1 
                #after the collision the next type of food is randomly chose and its new location is generated
                f = random.choice(foods)
                f.generateLocation(snake.body, wall.body)
                if snake.score % 5==0 and wall.level < 2: 
                    wall.level +=1 
                    snake.speed += 0.5
        
        display.fill(black) #erases the prev pos 
        drawGrid()
        
        snake.draw()
        #first food is always the simple one, afterwards they are randomly generated
        if snake.score ==0: f = food #now food must be randomly generated either apple or simple food
        #after the 1st collision the new food is drawn on its new loc
        if f == food: 
            f.draw() 
        else: 
            display.blit(f.image, f.rect())

        if snake.score == 5: 
            wall = Wall(2)
            snake.speed = 6.5
        wall.draw() 

        if snake.collision_wall(wall.body): 
            wall_coll = font_style.render('Wall Collision', True, (255, 0,0)) 
            game_over = font_style.render("GAME OVER", True, (255,0,0))

            #add the users's score and level to the table 
            score(name, snake.score, wall.level)

            display.fill(black) 
            display.blit(wall_coll, (100, 100))
            display.blit(game_over, (100, 200)) 
            pygame.display.update() 
            time.sleep(2)
            pygame.quit()

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

def get_username(screen): 
    intro = True
    font = pygame.font.SysFont('Times New Roman', 20) 
    get_user = font.render('Enter username: ', True, (255,255,255)) 
    #a loop is entered while the user is typing 
    string = ''

    while intro: 
        keys = pygame.key.get_pressed() #sequence of whether the key was pressed or not 

        for event in pygame.event.get(): 
            #if event.type == QUIT: 
                #pygame.quit()

            if event.type == pygame.KEYDOWN: 
                key = pygame.key.name(event.key) #returns string id of pressed key 

                if len(key) ==1: #getting one letter not a command 
                    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]: #getting the big letter of a letter 
                        string += key.upper() #getting the upper letter because of shift 
                    elif key == 'return': #finished typing 
                        user_inp(string) 
                        intro = False
                        break
                    else: string += key

                if key == 'backspace': 
                    string = string[:len(string)-1] #the last letter is omitted or deleted  

                if key == 'space': 
                    string += ' '

                if key == 'return': #finished typing 
                    user_inp(string) 
                    return string
    
        screen.fill((0,0,0))
        screen.blit(get_user, (10, 200)) 
        text = font.render(string, 1, (255,255,255)) 
        screen.blit(text, (220,200)) 
        pygame.display.update()

main()