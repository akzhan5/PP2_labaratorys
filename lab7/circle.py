import pygame 

pygame.init()
w = 600 
h = 600
display = pygame.display.set_mode((w, h))
pygame.display.set_caption('Circle')
clock = pygame.time.Clock()

red = (255, 0, 0)
radius = 25.0
x, y = 300, 300
done = False 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                if x+20<w-25:x+=20 
            if event.key == pygame.K_LEFT: 
                if x-20>25: x-=20 
            if event.key == pygame.K_UP: 
                if y-20>25: y-=20
            if event.key == pygame.K_DOWN: 
                if y+20<h-25: y+=20 
    
    display.fill((255,255,255))
    pygame.draw.circle(display, red, (x,y), radius)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()