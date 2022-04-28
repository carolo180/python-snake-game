from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_board
import time 

screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("programare snake")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score_board()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.2)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
    
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()