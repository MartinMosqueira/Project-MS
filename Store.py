import numpy as np

class Store:
    def __init__(self, numberBoxes, timeSeconds):
        self.numberBoxes = numberBoxes
        self.boxes={}
        self.timeBoxes={}
        self.costBox=1000
        self.row = []
        self.timeSeconds = timeSeconds
        self.clientProbability = 1/10

    def start_boxes(self):
        for box in range(1,self.numberBoxes+1):
            self.boxes[box] = []

    def start_time_boxes(self):
        for box in range(1,self.numberBoxes+1):
            self.timeBoxes[box] = None

    def attention_time_box(self):
        return np.random.normal(10, 5, 1)

    def start_client(self):
        if np.random.rand() < self.clientProbability:
            return True