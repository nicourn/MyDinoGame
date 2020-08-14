from game import *

def main():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.mixer.init()

    pygame.init()
    game = Game()
    game.init_game_setting()
    game.init_dino()
    game.init_enemy()

    while game:
        game.clock.tick(60)
        game.time += 1
        game.screen.fill((255, 255, 0))

        game.listen_event(pygame.event.get())
        game.collision_chek()
        game.screen_update()

    pygame.quit()

if __name__ == '__main__':
    main()
