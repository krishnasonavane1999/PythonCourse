from turtle import *
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10 


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []


    def create_car(self):
       random_chance = random.randint(1, 6)
       if random_chance == 1:
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(COLORS[random.randint(0, 5)])
        new_y = random.randint(0, 280)
        new_car.goto(300, new_y)
        self.all_cars.append(new_car)


    def move(self):
        for vehicle in self.all_cars:
            vehicle.backward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT

