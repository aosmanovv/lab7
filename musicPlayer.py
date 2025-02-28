import pygame
import time

screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3']
ind =False

pygame.mixer.init()
pygame.init()
done=False
def nextSong():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])

def prevSong():
    global _songs
    print(_songs[-1])
    print([_songs[0:-1]])
    _songs = [_songs[-1]] + _songs[0:-1] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])


def StopStart():
    global ind
    ind=not ind
    if (ind==False):
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.play()


pygame.mixer.music.load(_songs[0])
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        StopStart()
        time.sleep(0.2)
    if pressed[pygame.K_LEFT]:
        prevSong()
        time.sleep(0.2)
    if pressed[pygame.K_RIGHT]:
        nextSong()
        time.sleep(0.2)

    pygame.display.flip()
    clock.tick(300)