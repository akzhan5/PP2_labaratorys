import pygame 
import os 
from datetime import datetime

pygame.init()

#getting an image 
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

screen = pygame.display.set_mode((800, 600))
screen.fill("white")
pygame.display.set_caption("MickeyMouse")

clock = pygame.time.Clock()

body = get_image('image.jpg')
body = pygame.transform.scale(body, (800, 600))
# short hand is responsible for minutes :
short_hand = get_image('hand_hours.png').convert_alpha()  # to improve image quality
# long hand is responsible for seconds :
long_hand = get_image('hand_mins.png').convert_alpha()  # to improve image quality

font = pygame.font.SysFont('Arial', 30)

# a function that's responsible for the rotation of mickey's body
def blitRotateCenter(surf, image, coord, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = coord).center)

    surf.blit(rotated_image, new_rect)

x = 800 // 2
y = 600 // 2
radius = 10
color = (0, 0, 0)

done = False

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(body, (0, 0)) 

    time = datetime.now()
    lg_angle = - 6 * time.second
    sh_angle = - 6 * time.minute

    text = font.render(f'{time : %H:%M:%S}', True, (0, 0, 0), (255, 255, 255))
    screen.blit(text,(10, 10))

    blitRotateCenter(screen, long_hand, (390, 190), lg_angle)
    blitRotateCenter(screen, short_hand, (390, 190), sh_angle) 

    pygame.draw.circle(screen, color, (x, y), radius) 

    pygame.display.flip()

pygame.quit()