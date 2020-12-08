import pygame


pygame.init()
size = WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode(size)


# Класс персонажа
class Hero:
    def __init__(self):
        self.vel = 3 # Скорость персонажа
        self.width = 50
        self.height = 50
        self.x = WIDTH // 2
        self.y = HEIGHT - self.height
        self.isJump = False # Проверка на прыжок
        self.jumpCount = 10 # Параметр квадратичной функции для расчета траектории прыжка
        self.acceleration = 1.5 # Коэффициент ускорения при беге
    
    def draw(self):
        pygame.draw.rect(screen, pygame.Color("green"), (
                self.x, self.y, self.width, self.height
            ))

    def movement(self):
        state = pygame.key.get_pressed()

        if self.x > 0:
            if state[pygame.K_LEFT]:
                self.x -= self.vel
            
            if state[pygame.K_LSHIFT] and state[pygame.K_LEFT]:
                self.x -= self.vel * self.acceleration

        if self.x < WIDTH - self.width:
            if state[pygame.K_RIGHT]:
                self.x += self.vel

            if state[pygame.K_LSHIFT] and state[pygame.K_RIGHT]:
                self.x += self.vel * self.acceleration


clock = pygame.time.Clock()
fps = 60
hero = Hero()
running = True

while running:
    screen.fill(pygame.Color("black"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hero.draw()
    hero.movement()

    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
