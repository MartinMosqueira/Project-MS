import numpy as np

class Store:
    def __init__(self, numberBoxes):
        self.numberBoxes = numberBoxes
        self.boxes={}
        self.timeBoxes={}
        self.costBox=1000
        self.row = []
        self.timeRow = []
        self.timeRowLimits = []
        
        # time boxes
        self.min_time = float('inf')
        self.max_time = float('-inf')

    def start_boxes(self):
        for box in range(1,self.numberBoxes+1):
            self.boxes[box] = []

    def start_time_boxes(self):
        for box in range(1,self.numberBoxes+1):
            self.timeBoxes[box] = None
    
    def cost_boxes(self):
        return self.numberBoxes*self.costBox

    def attention_time_box(self):
        return np.random.normal(10*60, 5*60, 1)
    
    def min_attention_time_box(self, minTime):
        self.min_time = min(float(minTime), self.min_time)

    def max_attention_time_box(self, maxTime):
        self.max_time = max(float(maxTime), self.max_time)
    
    def min_time_row(self):
        return min(self.timeRowLimits)
    
    def max_time_row(self):
        return max(self.timeRowLimits)

    def start_client(self, time):
        arrival_time = np.random.normal(10*3600, 2*3600)
        
        # client arrival simulation with tolerance of 1 minute
        if 8 * 3600 <= arrival_time <= 12 * 3600:
            if abs(time - arrival_time) <= 60:
                return True
        return False
