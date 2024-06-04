import numpy as np

class Store:
    def __init__(self, numberBoxes, timeSeconds):
        self.numberBoxes = numberBoxes
        self.boxes={}
        self.costBox=1000
        self.row = []
        self.timeSeconds = timeSeconds

    def start_boxes(self):
        for box in range(1,self.boxes+1):
            self.boxes[box] = []

    def attention_time_box(self):
        return np.random.normal(10, 5, 1)