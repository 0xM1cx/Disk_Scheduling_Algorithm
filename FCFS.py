import matplotlib.pyplot as plt
import numpy as np
class FCFS:
    currentTime = 0
    def __init__(self):
        pass



    def executeAlgorithm(self, requests):
        rand_floats = [self.currentTime]
        for i in range(len(requests)-1):
            self.currentTime += round(np.random.uniform(0.0, 2.0), 1) 
            rand_floats.append(self.currentTime)


        return rand_floats

        
