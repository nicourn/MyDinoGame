from pygame.time import Clock
from pygame.sprite import Group
import pygame
from dino import Dino
from enemy import Enemy
from score import Scores
import sys


class Game:
    FPS = 30
    def __init__(self):
        self.screen: pygame.Surface = pygame.display.set_mode((720, 360))
        pygame.display.set_caption("PyDino")

        self.clock: Clock = Clock()
        self.dino = Dino()
        self.enemy = Group()
        self.scores = Scores("Очки: ", self.screen.get_rect())


    def init_enemy(self):
        for i in range(10):
            Enemy.enemys.append(Enemy.random_spawn())

    def init_dino(self):
        self.dino.move(self.screen.get_rect().centerx / 4, self.screen.get_rect().bottom)
        self.dino.play_sound("go")

    def init_game_setting(self):
        self.game_pause = True
        self.game = True
        self.time = -31

    def listen_event(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.dino.rect.bottom >= self.screen.get_rect().bottom:
                    self.dino.play_sound("jump")
                    self.dino.jump = True
                    self.dino.down = False
                    self.dino.speed = -12
                    if self.game_pause: self.game_pause = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and self.dino.speed <= 0:
                    self.dino.speed = 0

    def screen_update(self):
        rect: pygame.Rect = self.screen.get_rect()
        if not self.game_pause:
            self.scores.score += Enemy.random_get(self.enemy, self.time, (rect.right, rect.bottom))
        self.enemy.update()
        self.enemy.draw(self.screen)

        self.dino.update(rect.bottom)
        self.dino.blit(self.screen)

        self.scores.set_text(str(self.scores.score))
        self.scores.blit(self.screen)

        if pygame.sprite.spritecollide(self.dino, self.enemy, False, False):
            print("You lose")
            self.game_pause = True

        pygame.display.flip()

    def collision_chek(self):
        if pygame.sprite.spritecollide(self.dino, self.enemy, False, False):
            print("You lose")
            self.game_pause = True