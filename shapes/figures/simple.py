from .base import Figure
import math


class Circle(Figure):

    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y - self.radius)  # From docs: The center is radius units left of the turtle;
        turtle.pendown()
        turtle.color(self.color)
        turtle.circle(self.radius)


class Square(Figure):

    def __init__(self, side, **kwargs):
        super().__init__(**kwargs)
        self.side = side

    def draw(self, turtle):
        half_side = self.side / 2
        left = self.center_x - half_side
        top = self.center_y + half_side

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)


class Rectangle(Figure):

    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def draw(self, turtle):
        half_width = self.width / 2
        half_height = self.height / 2
        left = self.center_x - half_width
        top = self.center_y + half_height

        turtle.penup()
        turtle.goto(left, top)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.width)
        turtle.left(90)


class NSide(Figure):

    def __init__(self, radius, num_sides, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.num_sides = num_sides

    def draw(self, turtle):
        angle = 360 / self.num_sides
        side = 2.0 * self.radius * math.sin(math.pi/self.num_sides)
        left = self.center_x - self.radius*math.cos(math.pi/self.num_sides)

        turtle.penup()
        turtle.goto(left, self.center_y + side / 2)
        turtle.pendown()
        turtle.color(self.color)
        turtle.forward(1)
        turtle.setheading(270)  # point the turtle down
        for _ in range(self.num_sides):
            turtle.forward(side)
            turtle.left(angle)


class Pie(Figure):

    def __init__(self, radius, arg_degrees, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.arg_degrees = arg_degrees

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.center_x, self.center_y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(90)
        turtle.forward(self.radius)
        turtle.left(90)
        turtle.circle(self.radius, self.arg_degrees)
        turtle.goto(self.center_x, self.center_y)