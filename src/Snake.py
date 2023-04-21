import pygame
from environment import snakeSize


class Snake(pygame.sprite.Sprite):
    size = snakeSize
    initialVelocity = 3

    def __init__(self):
        super().__init__()
        self.x = 45
        self.y = 55

        self.head = [self.x, self.y]
        self.list = []
        self.length = 1

        self.velocityX = 0
        self.velocityY = 0

    def handleDirection(self, eventKey: int):
        if eventKey == pygame.K_UP:
            self.velocityX = 0
            self.velocityY = -Snake.initialVelocity
        elif eventKey == pygame.K_RIGHT:
            self.velocityX = Snake.initialVelocity
            self.velocityY = 0
        elif eventKey == pygame.K_DOWN:
            self.velocityX = 0
            self.velocityY = Snake.initialVelocity
        elif eventKey == pygame.K_LEFT:
            self.velocityX = -Snake.initialVelocity
            self.velocityY = 0

    def slither(self):
        self.x += self.velocityX
        self.y += self.velocityY

        self.head = [self.x, self.y]
        self.list.append(self.head)

        if len(self.list) > self.length:
            self.list.pop(0)

    def handleFoodEaten(self, increment: int = 7):
        self.length += increment
        Snake.initialVelocity += 0.5
