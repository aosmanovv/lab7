import pygame
import os
import datetime

def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)

    # draw rectangle around the image
    #pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)



_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False

im=pygame.transform.scale(get_image('images/mickeyclock.jpg'),(800,600))
ar1=pygame.transform.scale(get_image('images/arrow_small.png'),(300,200))
ar2=pygame.transform.scale(get_image('images/arrow_big.png'),(300,200))
angle1=0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(im,(0,0))
    #screen.blit(ar1,or1)
    #screen.blit(ar2,(350,140))
    angle1=-(datetime.datetime.now().hour%12*30-90)
    angle2=-(datetime.datetime.now().minute%60*6-90)
    print(angle2)
    blitRotate(screen,ar1,(400,300),(30,85),angle1)
    blitRotate(screen,ar2,(400,300),(30,105),angle2)
    pygame.display.flip()
    clock.tick(60)