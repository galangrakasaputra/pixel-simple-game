import pygame

from pygame.locals import *


window = pygame.display.set_mode((600, 300))
gambar = pygame.image.load("orang.png")

run = True

gerak = {
    "atas": False,
    "bawah": False,
    "kiri": False,
    "kanan": False
}

while run:
    window.fill((255,255,255))
    window.blit(gambar, [100, 100])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()