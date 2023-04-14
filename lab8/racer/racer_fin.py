#imports 
import pygame, time, random, sys
from pygame.locals import * 

#Initialzing 
pygame.init()

#Setting up FPS
clock = pygame.time.Clock() #an object of class CLock 
FPS = 60 #60 frames per second 

#Creating colors
white = (255,255,255)
black = (0,0,0) 
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

#Other Variables for use in the program
speed = 5 
score = 0
height = 600
width = 400
coins_score = 0

#Setting up Fonts
font_style = pygame.font.SysFont('Verdana', 60) #name of the shrift, size of the font
font_smaller = pygame.font.SysFont('Verdana', 20)
game_over = font_style.render('Game Over', True, black)
over_sound = pygame.mixer.Sound('crash.wav')
background = pygame.image.load('AnimatedStreet.png')

#Create a white screen 
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Street Racer')
display.fill(white)

#create classes
class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() #inherits all the att of the parent class Sprite 
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (200, 550) #center of the display 

    def move(self): 
        pressed_keys = pygame.key.get_pressed() #sequence of the pressed keys and bools 
        if self.rect.top > 0: #now player moves in all direct
            if pressed_keys[K_UP]: 
                self.rect.move_ip(0,-5)
        if self.rect.bottom < height: 
            if pressed_keys[K_DOWN]: 
                self.rect.move_ip(0,5)
        if self.rect.right < width: 
            if pressed_keys[K_RIGHT]: 
            #check for boundaries 
                self.rect.move_ip(5,0) #moves 5 pixels to the right if the right key is pressed
        if self.rect.left > 0: 
            if pressed_keys[K_LEFT]: 
                self.rect.move_ip(-5,0)

class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() #inherits the att of the parent class 
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect() 
        self.x = random.randint(40, width - 40)
        self.rect.center = (self.x, 0) #enemy randomly appears from the top 

    def move(self): 
        global score
        self.rect.move_ip(0, speed) #moves the enemy down 5 pixels 
        if self.rect.top > height: #car is under the display 
            self.rect.top =0
            score +=1 #one enemy passed 1 score added 
            self.rect.center = (random.randint(40, width - 40), 0)

#setting up sprites 
P1 = Player() #object of class player 
E1 = Enemy() #object of class enemy 

class Coins(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() #inherits all the att of the class Sprite 
        coin_im = pygame.image.load('coin.png')
        self.image = pygame.transform.scale(coin_im, (30, 30))
        self.rect = self.image.get_rect() 
        self.x = random.randint(15, width - 15)
        self.y = random.randint(55, 550)
        self.rect.center = (self.x, self.y) #so that it is under enemy or above the player 

    def move(self): 
        if self.x == E1.x: self.rect.center = (random.randint(55, width - 55), random.randint(55, height -55)) #so that it is under enemy or above the player 
       

#creating sprites groups 
enemies = pygame.sprite.Group() #object of a container class for many sprites 
enemies.add(E1)

coin = pygame.sprite.Group() 

all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)


#adding a new user event 
INC_SPEED = USEREVENT +1 
pygame.time.set_timer(INC_SPEED, 1000) #calls the vent each 1s in the event queue 

#game loop
while True: 
    #cycles through all events occuring: 
    for event in pygame.event.get(): 
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()

    display.blit(background, (0,0)) #background fits into the display perfectly into top left is (0,0)
    #background must be drawn 1, because pygame surfaces are like layers, the next images will be drawn above the one that was drawn previously 
    score_card = font_smaller.render('Score: '+str(score), True, black)
    display.blit(score_card, (10,10)) #displays the score on the left 
    coin_card = font_smaller.render('Coin: ' + str(coins_score), True, black)
    display.blit(coin_card, (10,30))

    #if the coin was eaten up by the player 
    if len(coin.sprites())==0:  
        coin.add(Coins()) 
    
    for c in coin: 
        c.move()
        display.blit(c.image, c.rect)

    #moves and re draws all sprites: 
    for entity in all_sprites:
       entity.move()
       display.blit(entity.image, entity.rect) 

    #how to make sure that enemy does not appear at the same x pos as a coin? 
    #for ent in enemies: 
        #if ent.x != 

    #to be run if collision occurs 
    if pygame.sprite.spritecollideany(P1, enemies): #player collides with one of the enemies 
        over_sound.play() #object of class sound
        time.sleep(0.5) #delay execution 

        display.fill(red)
        display.blit(game_over, (width/2, height/2))

        for entity in all_sprites: 
            entity.kill() #removes the sprite from all groups 
        pygame.quit()
        sys.exit()

    #to be run if collision between coin and player occurs: 
    if pygame.sprite.spritecollideany(P1, coin): 
        for ent in coin: 
            ent.kill()
        coins_score +=1 

    pygame.display.update() #make all the changes possible on the screen 
    clock.tick(FPS) 


