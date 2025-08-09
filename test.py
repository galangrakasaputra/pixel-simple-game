import pygame
import math

from pygame.locals import *
from random import randint

# pygame.init()
layar = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Tester Pygame")

skor = 0
bullets = []

waktu_muncul = 100
musuh = [[600, 300]]


playerNormal = pygame.image.load("orang.png")
playerShoot = pygame.image.load("orang_nembak.png")
player = playerNormal
gambarMusuh = pygame.image.load("musuh.png")
peluruGambar = pygame.image.load("peluru.png")
peluru = pygame.transform.scale(peluruGambar, (5,5))
koorPlayer = [100,75]
koorPeluru = [200, 75]
running = True

gerak = {
    "atas": False,
    "bawah": False,
    "kanan": False,
    "kiri": False
}

speed = pygame.time.Clock()
while running:
    speed.tick(60)
    layar.fill((255,255,255))
    layar.blit(player, koorPlayer)
    
    for bullet in bullets:
        bullet_index = 0
        bullet[0] += 2
        # bullet[1] += koorPlayer[1] + 10
        if bullet[0] <= 0 or bullet[0] > 600 or bullet[1] <= 0 or bullet[1] > 300:
            bullets.pop(bullet_index)
        bullet_index += 1
        
        for kordBullet in bullets:
            layar.blit(peluru, (kordBullet[0], kordBullet[1]))
            
    
    waktu_muncul -= 1
    if waktu_muncul == 0:
        musuh.append([600, randint(50, 300-32)])
        waktu_muncul = 100
        
    indexMusuh = 0
    for enemy in musuh:
        enemy[0] -= 2
        
        
        if enemy[0] <= 0:
            musuh.pop(indexMusuh)
    
        detFireEnemy = pygame.Rect(gambarMusuh.get_rect())
        detFireEnemy.top = enemy[1]
        detFireEnemy.left = enemy[0]
        
        if detFireEnemy.left <= 0:
            musuh.pop(indexMusuh)
            
        pygame.draw.rect(layar, (0, 255, 0), detFireEnemy, 2)
            
        index_bullet = 0
        for bullet in bullets:
            bullet_rect = pygame.Rect(peluru.get_rect())
            bullet_rect.left = bullet[0]
            bullet_rect.top = bullet[1]
            
            if detFireEnemy.colliderect(bullet_rect):
                skor += 1
                musuh.pop(indexMusuh)
                bullets.pop(index_bullet)
            index_bullet += 1
        indexMusuh += 1
    
    for enemy in musuh:
        layar.blit(gambarMusuh, enemy)
        
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            # Tembak
            if event.key == pygame.K_SPACE:
                bullets.append([koorPlayer[0] + 65, koorPlayer[1] + 10])
                player = playerShoot
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
                player = playerNormal
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