import random

class Client:
    def __init__(self):
        self.timeSeconds = 30*60
        self.costClient = 10000
        self.color = self.generate_random_color()
    
    def generate_random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)
        