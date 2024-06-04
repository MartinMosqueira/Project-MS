import numpy as np

class Client:
    def __init__(self):
        self.timeSeconds = 30
        self.costClient = 10000
        self.clientProbability = 1/144
    
    def start_client(self):
        if np.random.rand() < self.clientProbability:
            return True
