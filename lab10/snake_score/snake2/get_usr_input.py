import pygame 
from pygame.locals import * 
from user import user_inp

pygame.init() 

display = pygame.display.set_mode((400, 400)) 

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
                   return [string, str(user_inp(string))]
    
        screen.fill((0,0,0))
        screen.blit(get_user, (10, 200)) 
        text = font.render(string, 1, (255,255,255)) 
        screen.blit(text, (220,200)) 
        pygame.display.update()
 
print(get_username(display))

            