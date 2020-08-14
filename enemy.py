import pygame
from pygame.sprite import Group
import random


class Enemy(pygame.sprite.Sprite):
    enemys = []
    imgs = ["src/image/enemy1.png", "src/image/enemy2.png", "src/image/enemy3.png"]
    def __init__(self, img_path):
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = pygame.image.load(img_path)
        k = 70 / self.image.get_width()
        new_width = int(self.image.get_width() * k)
        new_heigth = int(self.image.get_height() * k)
        self.image = pygame.transform.scale(self.image, (new_width, new_heigth))
        self.rect: pygame.rect.Rect = self.image.get_rect()
        print(f"{self.rect.width}, {self.rect.height} -- {img_path}")

    def move(self, x, y):
        self.rect.centerx = x
        self.rect.bottom = y

    @staticmethod
    def random_spawn():
        return Enemy(Enemy.imgs[random.randint(0, 2)])

    @staticmethod
    def random_get(group: Group, time: int,  x_y: tuple):
        scores = 0
        num = random.randint(0, len(Enemy.enemys) - 1)
        enemy: Enemy = Enemy.enemys[num]
        q = random.randint(0, 100)
        if q <= 5 and len(group.sprites()) < 2:
            q = 1
        else:
            q = 120

        if Enemy.enemys[num] not in group.sprites() and time % q == 0 and len(group.sprites()) < 3:
            enemy.move(x_y[0], x_y[1])
            group.add(enemy)

        for enemy in group.sprites():
            if enemy.rect.right < 0:
                group.remove(enemy)
                scores += 1

        return scores


    def update(self):
        self.rect.x -= 6

    def blit(self, screen):
        screen.blit(self.image, self.rect)

