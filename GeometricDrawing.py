import pygame
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))
surface = pygame.Surface((400, 300), pygame.SRCALPHA)

color=(255,0,0)
left=20
top=20
width=20
height=20
radius=10
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
    pygame.draw.circle(screen, color, (100, 100), radius)
    pygame.draw.rect(screen, color, pygame.Rect(100, 200, 100, 100), 10)
    pygame.draw.circle(screen, color, (300, 60), 50, 10)
    pygame.draw.polygon(surface, color, point_list)
    pygame.draw.line(surface, color, (startX, startY), (endX, endY), width)

    pygame.display.flip()
    clock.tick(60)
