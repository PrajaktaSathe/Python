import pygame
import pygame.image
from pygame.locals import *
import time
import random

# Size of the block
Size = 40
# Background Color
BC = (0, 0, 0)


# Create Food (the apple)
class Food:
    def __init__(self, parent_screen):
        # insert image into the screen
        self.food = pygame.image.load("img/apple.jpg").convert()
        self.img = pygame.transform.scale(self.food, (40, 40))
        self.parent_screen = parent_screen
        self.move_x = Size * 10
        self.move_y = Size * 10

    # draw into the screen
    def draw(self):
        self.parent_screen.blit(self.img, (self.move_x, self.move_y))
        pygame.display.flip()

    # the food will appear random
    def appear(self):
        self.move_x = random.randint(1, 18) * Size
        self.move_y = random.randint(1, 18) * Size


# Draw the snake
class Snake:
    # insert image into the screen
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("img/ghost.png").convert()
        self.ghost = pygame.transform.scale(self.block, (40, 40))
        self.direction = 'down'

        self.move_x = [Size] * length
        self.move_y = [Size] * length

    # while it crush with food the length increase
    def increase_length(self):
        self.length += 1
        self.move_x.append(-1)
        self.move_y.append(-1)

    # redraw into screen
    def draw(self):
        self.parent_screen.fill(BC)
        for i in range(self.length):
            self.parent_screen.blit(self.ghost, (self.move_x[i], self.move_y[i]))
        pygame.display.flip()

    #  assign the direction
    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_right(self):
        self.direction = "right"

    def move_left(self):
        self.direction = "left"

    # control the snake to move
    def move(self):

        for i in range(self.length - 1, 0, -1):
            self.move_x[i] = self.move_x[i - 1]
            self.move_y[i] = self.move_y[i - 1]

        if self.direction == "up":
            # Replace the first position of the blog
            self.move_y[0] -= Size

        if self.direction == "down":
            self.move_y[0] += Size

        if self.direction == "right":
            self.move_x[0] += Size

        if self.direction == "left":
            self.move_x[0] -= Size

        self.draw()


# Set the screen
class Screen:
    def __init__(self):
        pygame.init()
        # show the caption
        pygame.display.set_caption("Happy Snake Game :D ")
        self.surface = pygame.display.set_mode((800, 700))
        # start with one column (just one blog)
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.food = Food(self.surface)
        self.food.draw()

    # if colision happen
    def accident(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + Size:
            if y2 <= y1 < y2 + Size:
                return True
        return False

    def start(self):
        self.snake.move()
        self.food.draw()
        self.score()
        pygame.display.flip()

        # Coliding happend with food
        if self.accident(self.snake.move_x[0], self.snake.move_y[0], self.food.move_x, self.food.move_y):
            self.snake.increase_length()
            self.food.appear()

        # Coliding with itself
        for i in range(1, self.snake.length):
            if self.accident(self.snake.move_x[0], self.snake.move_y[0], self.snake.move_x[i], self.snake.move_y[i]):
                raise "Game Over"

    # Count the Score and show it
    def score(self):
        font = pygame.font.SysFont('Verdana', 25)
        score = font.render(f"Score: {self.snake.length}", True, (250, 250, 250))
        self.surface.blit(score, (30, 10))

    # When snake die
    def over(self):
        self.surface.fill(BC)
        font = pygame.font.SysFont('Verdana', 25)
        line = font.render(f"Game Over :( ! You score: {self.snake.length}", True, (250, 250, 250))
        self.surface.blit(line, (200, 300))
        line1 = font.render("Press Enter to play again :D ", True, (250, 250, 250))
        self.surface.blit(line1, (200, 350))
        pygame.display.flip()

    # when replay the mark will recount
    def recount(self):
        self.snake = Snake(self.surface, 1)
        self.food = Food(self.surface)

    # the game start to run
    def play(self):
        stay = True
        stop = False

        while stay:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # press the escape key
                    if event.key == K_ESCAPE:
                        stay = False

                    # press enter to replay
                    if event.key == K_RETURN:
                        stop = False

                    # continue the game
                    if not stop:
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                elif event.type == QUIT:
                    stay = False

            # redraw the game screen and show the element like food, snake and score inside
            try:
                if not stop:
                    self.start()

            except Exception as ex:
                self.over()
                stop = True
                # Recount the mark
                self.recount()

            # control the frames per second which mean the speed of snake
            time.sleep(.2)


if __name__ == "__main__":
    screen = Screen()
    screen.play()
