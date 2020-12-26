import pygame
from random import randrange
import os

WIDTH = HEIGHT = 48

# загрузка изображения
def load_image(name, color_keys=None):
    full_name = os.path.join(name)

    try:
        image = pygame.image.load(full_name)
        image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    except pygame.error as message:
        print('не удалось загрузить', name)
        raise SystemExit(message)
    return image

floor = [load_image('sprite_down/sprite_down_1.png'),
         load_image('sprite_down/sprite_down_2.png'),
         load_image('sprite_down/sprite_down_3.png'),
         load_image('sprite_down/sprite_down_4.png')]


# Пол
class FloorPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(group)
        self.width = WIDTH
        self.height = HEIGHT
        self.can_wall_jump = False

        self.image = floor[randrange(3)]
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def update(self):
        pass


# Стена
class WallPlatform(FloorPlatform):
    def __init__(self, x, y, group):
        super().__init__(x, y, group)
        self.color = pygame.Color("yellow")
        self.can_wall_jump = True

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = pygame.Rect(x, y, self.width, self.height)


# Двигающаяся платформа
class MovingPlatform(FloorPlatform):
    def __init__(self, x, y, group, dir):
        super().__init__(x, y, group)
        self.color = pygame.Color("red")
        
        self.dir = dir
        self.counter = 0
        self.x = 2 if self.dir == ">" else -2
        self.y = 3 if self.dir == "^" else 0

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = pygame.Rect(x, y, self.width, self.height)

    # Перемещение платформы на промежутке
    def update(self):
        if self.dir == "^":
            if abs(self.counter) >= 100:
                self.y = -self.y

            self.rect = self.rect.move(0, self.y)
            self.counter += self.y
        else:
            
            if abs(self.counter) >= 200:
                self.x = -self.x

            self.rect = self.rect.move(self.x, 0)
            self.counter += self.x
