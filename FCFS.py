import numpy as np
class FCFS:
    currentTime = 0.0
    def __init__(self, head_Disk, requests):
        self.requests = requests
        self.requests.append(head_Disk)

    def executeAlgorithm(self):
        pass     
