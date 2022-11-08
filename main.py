from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

user_selected_speed = screen.textinput(title="Speed", prompt="Select speed: slow / medium / fast ")

if user_selected_speed == "fast":
    speed = .05
elif user_selected_speed == "medium":
    speed = .1
elif user_selected_speed == "slow":
    speed = .15
else:
    speed = .1

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.add_score()
        snake.add_square()

    # Detect collision with wall

    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False

    for x in range(-300, 300):
        if snake.head.distance(300, x) < 1 or snake.head.distance(x, 300) < 1 \
                or snake.head.distance(-300, x) < 1 or snake.head.distance(x, -300) < 1:
            scoreboard.reset()
            snake.reset()

    if snake.check_collision():
        scoreboard.reset()
        snake.reset()

screen.exitonclick()
