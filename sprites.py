import pygame
from setting import *
clock = pygame.time.Clock()

class Button:
    def __init__(self, x, y, colour):
        self.x, self.y = x, y
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour,(self.x, self.y, SIZE_OF_BUTTON, SIZE_OF_BUTTON))

    def clicked(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + SIZE_OF_BUTTON and self.y <= mouse_y <= self.y + SIZE_OF_BUTTON

class TextOnScreen:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 16)
        text = font.render(self.text, True, WHITE)
        screen.blit(text, (self.x, self.y))

class Flash:
    def __init__(self,x,y,size_x,size_y,colour,repeat,screen):
        self.x , self.y = x,y
        self.size_x, self.size_y = size_x, size_y 
        self.colour = colour 
        self.repeat = repeat
        self.screen = screen
    def animation(self):
        main_screen = self.screen.copy()
        flashing = pygame.Surface((self.size_x,self.size_y))
        flashing = flashing.convert_alpha()
        r, g, b = self.colour
        for _ in range(self.repeat):
            for start, end, step in ((0, 255, 1), (255, 0, -1)):
                for alpha in range(start, end, ANIMATION_SPEED * step):
                    self.screen.blit(main_screen, (0, 0))
                    flashing.fill((r, g, b, alpha))
                    self.screen.blit(flashing, (self.x, self.y))
                    pygame.display.update()
                    clock.tick(60)
        self.screen.blit(main_screen, (0, 0))
