from pygame import font, rect

class Scores:
    def __init__(self, start_text, screen_rect: rect.Rect):

        self.text_color = (0, 0, 0)
        self.start_text = start_text
        self.font = font.SysFont(None, 50)

        self.rect = rect.Rect(0, 0, 200, 50)
        self.rect.centerx = screen_rect.right * 0.9
        self.rect.centery = screen_rect.bottom * 0.1

        self.score = 0

    def set_text(self, text):
        self.image = self.font.render(self.start_text + text, True, self.text_color)
        self.image.get_rect().center = self.rect.center

    def blit(self, screen):
        screen.blit(self.image, self.rect)
