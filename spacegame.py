# Skriv din kod här för att skapa spelet! Följ dessa steg:
import pygame

pygame.init()

# Skapa en skärm
skärmens_bred = 800
skärmens_höjd = 600

skärm = pygame.display.set_mode((skärmens_bred, skärmens_höjd))

pygame.display.set_caption("space game")

### Ladda in alla sprites och bakgrundsbilder ###

# Sprite för rymdskeppet
original_bild = pygame.image.load("sprites/SpaceShip.png")
sprite_rymdskepp = pygame.transform.scale(original_bild, (original_bild.get_width()//2, original_bild.get_height()//2))

# Ladda in alla bakgrundsbilder
background_mörkblå = pygame.image.load("backgrounds/bg.png")
background_stjärnor = pygame.image.load("backgrounds/Stars-A.png")



# Startvärden på variabler
spelet_körs = True
bg_y = 0
spelare_x = 400                    #skärmens_bress // 2 - 120
spelare_y = 300                     #skärmens_höjd - 200
spelarens_hastighet = 1

#### SPELLOOPEN ####
while (spelet_körs == True):

    # Rita ut bakgrundsbilden
    #skapa en mörk bakgrundsbild
    skärm.blit(background_mörkblå, (0,0))

    #rita ut sjärnorna i bakgrunden
    skärm.blit(background_stjärnor, (0, bg_y))

    #rita en andra backgroundsbild utanför skärmen för att skapa illusionen av en oändlig bakgrund
    skärm.blit(background_stjärnor, (0, bg_y - skärmens_höjd)) #andra bilden som ligger ovanför den första

    #uppdatera båda bildernas position
    bg_y += 2

    #om bilden har rört sig utanför skärmen, sätt den tillbaka till början
    if bg_y >= skärmens_höjd:
        bg_y = 0

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            spelet_körs = False

    skärm.blit(sprite_rymdskepp, (spelare_x, spelare_y))

    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spelare_x > 0:
        spelare_x -= spelarens_hastighet
    if keys[pygame.K_RIGHT] and spelare_x < skärmens_bred - sprite_rymdskepp.get_width():
        spelare_x += spelarens_hastighet
    if keys[pygame.K_UP] and spelare_y > 0:
        spelare_y -= spelarens_hastighet
    if keys[pygame.K_DOWN] and spelare_y < skärmens_höjd - sprite_rymdskepp.get_height() + 26:
        spelare_y += spelarens_hastighet
pygame.quit()








'''
Steg 1 - Skapa en skärm och rita ett skepp
Steg 2 - Lägga till en scrollande stjärnbakgrund
Steg 3 - Sätt jetmotorer på rymdskeppet
Steg 4 - Gör så rymdskeppet kan skjuta
Steg 5 - Slumpa fram Asteroider 
Steg 6 - Detektera kollisioner mellan rymdskeppet och asteroiden
Steg 7 - Skapa explosionseffekten (samt lär dig partikeleffekter)
Steg 8 - Gör så att rymdskeppet kan explodera i kollision med asteroiden
Steg 9 - Gör så att rymdskeppet kan skjuta ner asteroider
Steg 10 - Lägg till musik och ljudeffekter
'''