# Skriv din kod här för att skapa spelet! Följ dessa steg:
import pygame
import random

pygame.init()

# Skapa en skärm
skärmens_bred = 800
skärmens_höjd = 600

skärm = pygame.display.set_mode((skärmens_bred, skärmens_höjd))

pygame.display.set_caption("space game")

### Ladda in alla sprites och bakgrundsbilder ###

# Sprite för rymdskeppet
original_bild = pygame.image.load("sprites/SpaceShip.png")
sprite_rymdskepp = pygame.transform.scale(original_bild, (original_bild.get_width() // 2, original_bild.get_height() // 2))

# sprite för jetmotorer
sprite_jetmotor = pygame.image.load("sprites/fire.png")

# sprite för skott
sprite_skott = pygame.image.load("sprites/bullet.png")

# sprite för asteroider
sprite_liten_astroid = pygame.image.load("sprites/small-A.png")

# Ladda in alla bakgrundsbilder
background_mörkblå = pygame.image.load("backgrounds/bg.png")
background_stjärnor = pygame.image.load("backgrounds/Stars-A.png")

# Startvärden på variabler
spelet_körs = True
bg_y = 0
spelare_x = 400
spelare_y = 300
spelarens_hastighet = 6

# jet
jet_x = spelare_x + 13
jet_y = spelare_y + 46

# skott
skott_räknare = 0

# asteroid
asteroid_liten_lista = []

# skott lista
skott_lista = []

# asteroid räknare
asteroid_liten_räknare = 0


# liten asteroid logic
class LitenAstroid:
    def __init__(self, asteroid_liten_x, asteroid_liten_y):
        self.x = asteroid_liten_x
        self.y = asteroid_liten_y
        self.hastighet = 4
        self.bild = sprite_liten_astroid

    def flytta(self):
        self.y += self.hastighet

    def rita(self, skärm):
        skärm.blit(self.bild, (self.x, self.y))


class Skott:
    # Sätter alla startvärdena för skottet
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hastighet = 10
        self.bild = sprite_skott

    def flytta(self):
        self.y -= self.hastighet

    def rita(self, skärm):
        skärm.blit(self.bild, (self.x, self.y))


#### SPELLOOPEN ####
while spelet_körs:

    # Rita ut bakgrundsbilden
    skärm.blit(background_mörkblå, (0, 0))
    skärm.blit(background_stjärnor, (0, bg_y))
    skärm.blit(background_stjärnor, (0, bg_y - skärmens_höjd))

    # uppdatera bakgrundens position
    bg_y += 2
    if bg_y >= skärmens_höjd:
        bg_y = 0

    # Hantera events
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            spelet_körs = False

    # Rita ut rymdskeppet och jetmotorn
    skärm.blit(sprite_rymdskepp, (spelare_x, spelare_y))
    jet_x = spelare_x + 13
    jet_y = spelare_y + 46
    skärm.blit(sprite_jetmotor, (jet_x, jet_y))

    # Hantera tangenttryckningar
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spelare_x > 0:
        spelare_x -= spelarens_hastighet
    if keys[pygame.K_RIGHT] and spelare_x < skärmens_bred - sprite_rymdskepp.get_width():
        spelare_x += spelarens_hastighet
    if keys[pygame.K_UP] and spelare_y > 0:
        spelare_y -= spelarens_hastighet
    if keys[pygame.K_DOWN] and spelare_y < skärmens_höjd - sprite_rymdskepp.get_height() + 26:
        spelare_y += spelarens_hastighet
    if keys[pygame.K_SPACE]:
        if skott_räknare > 10:
            skott_lista.append(Skott(spelare_x + 20, spelare_y))
            skott_räknare = 0

    # Hantera asteroidlogik
    asteroid_liten_räknare += 1
    if asteroid_liten_räknare > 20:
        asteroid_liten_lista.append(LitenAstroid(random.randint(0, skärmens_bred), 0))
        asteroid_liten_räknare = 0

    for asteroid_liten in reversed(asteroid_liten_lista):
        asteroid_liten.flytta()
        asteroid_liten.rita(skärm)

        if asteroid_liten.y > skärmens_höjd:
            asteroid_liten_lista.remove(asteroid_liten)

    # Hantera skottlogik
    skott_räknare += 1
    for skott in reversed(skott_lista):
        skott.flytta()
        skott.rita(skärm)

        # Kollision mellan skott och asteroider
        for asteroid_liten in reversed(asteroid_liten_lista):
            if (asteroid_liten.x < skott.x < asteroid_liten.x + sprite_liten_astroid.get_width() and
                    asteroid_liten.y < skott.y < asteroid_liten.y + sprite_liten_astroid.get_height()):
                asteroid_liten_lista.remove(asteroid_liten)
                skott_lista.remove(skott)
                break

        if skott.y < -100:
            skott_lista.remove(skott)

    pygame.display.update()

pygame.quit()