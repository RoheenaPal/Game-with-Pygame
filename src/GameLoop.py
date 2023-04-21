import os, pygame
import sys

from Food import Food
from Snake import Snake
from Window import Window
from environment import fps, white, red, black, eatingRadius, screenWidth, screenHeight


def isFoodEaten(snake: Snake, food: Food):
    return abs(food.x - snake.x) < eatingRadius and abs(food.y - snake.y) < eatingRadius


# Creating game loop
def gameLoop(window: Window):
    snake = Snake()
    food = Food()

    # Game specific variables
    # when this becomes true, we will ask whether he wants to quit the game or play another round
    gameOver = False

    # fps = frame per second
    score = 0
    highScore = 0

    if not os.path.exists("high_score.txt"):
        with open("high_score.txt", "w") as f:
            f.write("0")

    with open("high_score.txt", "r") as f:
        highScore = int(f.read())

    while True:  # this loop is created so that the game window stays till the user exits it
        if gameOver:
            with open("high_score.txt", "w") as f:
                f.write(str(highScore))
            window.showGameOver()
            break

        for event in pygame.event.get():  # this consists of all the activities we do with the mouse or keyboard
            if event.type == pygame.QUIT:  # if exit button is pressed
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                snake.handleDirection(event.key)

        snake.slither()

        if isFoodEaten(snake, food):
            score += 10
            window.playSuccessMusic()
            food.changePosition()
            snake.handleFoodEaten()
            if score > highScore:
                highScore = score

        window.fillScreenWithColor(white)
        window.showScore(score, highScore)

        if (
            snake.head in snake.list[:-1]
            or snake.x < 0
            or snake.x > screenWidth
            or snake.y < 0
            or snake.y > screenHeight
        ):
            # if the snake collides with itself, i.e., coordinate of the head matches with any other element in the list
            gameOver = True
            window.playGameOverMusic()

        window.plotFood(food, red)
        window.plotSnake(snake, black)
        window.clock.tick(fps)
        pygame.display.update()
