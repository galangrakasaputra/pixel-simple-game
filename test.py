import pygame
import math

pygame.init()
layar = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Tester Pygame")

skor = 0
bullet = []

player = pygame.image.load("orang.png")
peluruGambar = pygame.image.load("peluru.png")
peluru = pygame.transform.scale(peluruGambar, (30,30))
koorPlayer = [100,75]
koorPeluru = [200, 75]
running = True

gerak = {
    "atas": False,
    "bawah": False,
    "kanan": False,
    "kiri": False
}

while running:
            
    layar.fill((255,255,255))
    layar.blit(player, koorPlayer)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            # Tembak
            if event.key == pygame.K_SPACE:
                print("tembak")
            # gerak
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                gerak['atas'] = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                gerak['bawah'] = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                gerak['kanan'] = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                gerak['kiri'] = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("tembak")
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                gerak['atas'] = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                gerak['bawah'] = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                gerak['kanan'] = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                gerak['kiri'] = False
            
        if gerak['atas']:
            koorPlayer[1] -= 5
        elif gerak['bawah']:
            koorPlayer[1] += 5
        elif gerak['kanan']:
            koorPlayer[0] += 5
        elif gerak['kiri']:
            koorPlayer[0] -= 5
            

pygame.quit()