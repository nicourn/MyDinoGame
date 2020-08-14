import pygame
from pygame.mixer import Sound

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = pygame.image.load("src/image/go.png")
        self.image = pygame.transform.scale(self.image, (70, 90))
        self.rect: pygame.rect.Rect = self.image.get_rect()
        self.jump = False
        self.sounds = {"jump": Sound("src/sound/jump.ogg"), "down": Sound("src/sound/down.ogg"),
                       "go": Sound("src/sound/go.ogg"), "dead": 4}
        self.speed = 0
        self.down = True


    def move(self, x, y):
        self.rect.centerx = x
        self.rect.bottom = y

    def jump(self):
        self.dino.play_sound("jump")
        self.dino.jump = True
        self.dino.down = False
        self.dino.speed = -12

    def play_sound(self, text):
        if text == "go":
            self.sounds[text].play(loops=1000)
            self.sounds[text].set_volume(0.1)
        elif text == "jump":
            self.sounds[text].play()
            self.sounds[text].set_volume(0.2)
        elif text == "down":
            self.sounds[text].play()
            self.sounds[text].set_volume(0.2)


    def blit(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)

    # TODO заменить на платформу
    def update(self, y):
        if self.rect.bottom < y:
            self.speed += 0.25
        elif not self.jump and self.rect.bottom > y:
            self.speed = 0
            if not self.down:
                self.play_sound("down")
                self.down = True

        if self.jump:
            self.jump = False

        self.rect.y += self.speed

