from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            x_coordinate = 0
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.pu()
            new_square.setx(x_coordinate)
            x_coordinate -= 20
            self.segments.append(new_square)

    def add_square(self):
        # add a new segment to the snake
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.pu()
        last_square = self.segments[-1]
        new_square.goto(last_square.pos())
        self.segments.append(new_square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            snake_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(snake_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def check_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

