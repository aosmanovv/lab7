import pygame


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
#Wimage = pygame.image.load('ball.png')


done = False
is_blue = True
x = 30
y = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y-20>25: y -= 20
    if pressed[pygame.K_DOWN] and y+20<275: y += 20
    if pressed[pygame.K_LEFT] and x-20>25: x -= 20
    if pressed[pygame.K_RIGHT] and x+20<375: x += 20


    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0,0,0), (x, y),25,25)

    pygame.display.flip()
    clock.tick(60)