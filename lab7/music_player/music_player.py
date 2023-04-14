import pygame 
import random 
pygame.init()
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("MusicPLayer")

done = False 
songs = ['I Knew You Were Trouble.mp3', 'I Love You So.mp3', 'The Lost Song.mp3', 'Save Your Goodbye.mp3']
SONG_END = pygame.USEREVENT +1 #number assigned is surely not equal to any other event, since USEREVENT has the highest value in the enum
clock = pygame.time.Clock()
pygame.mixer.music.set_endevent(SONG_END) #sets an event type with the number SONG_END

#SysFont - (name of the font = arial, size) - filtering the text with the sysfont class 
font_style = pygame.font.SysFont('Times New Roman', 20)


def message_intro(msg, color, pos): 
    #render(text, .., color) -> returns a surface with the given text in a colour 
    mesg = font_style.render(msg, True, (0,0,0))
    #blit(blitting surface, (x,y coord of the topleft))
    display.blit(mesg, pos)


#play songs in sequence 
def play_next_song(): 
    global songs 
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()
    songs = songs[1:] + [songs[0]] #move current song to the end of the list 

#play the prev song
def play_prev_song(): 
    global songs 
    pygame.mixer.music.load(songs[-2])
    pygame.mixer.music.play()
    songs = [songs[-1]] + songs[:len(songs)-1]

paused = False

while not done: 
    display.fill((255,255,255))

    message_intro('Start - Enter key', (0,0,0), (100, 100))
    message_intro('Pause and Unpause - Space key', (0,0,0), (100, 200))
    message_intro('Next song - Right key', (0,0,0), (100, 300))
    message_intro('Previous song - Left key', (0,0,0), (100, 400))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RETURN: 
                play_next_song()
            if event.key == pygame.K_RIGHT: 
                play_next_song()
            if event.key == pygame.K_LEFT: 
                play_prev_song()
            if event.key == pygame.K_SPACE: 
                paused = not paused
                if paused: 
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


