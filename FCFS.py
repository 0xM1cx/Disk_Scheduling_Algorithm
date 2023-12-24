import numpy as np
class FCFS:
    currentTime = 0

    def executeAlgorithm(self, requests):
        rand_floats = [self.currentTime]
        for i in range(len(requests)-1):
            self.currentTime += np.random.random_integers(0, 10) 
            if self.currentTime in rand_floats:
                self.currentTime += 0.5
            rand_floats.append(self.currentTime)

        head_movements_calculation_string = []
        total_head_movements = 0
        # Calculation of total number of head movements
        for  index in range(len(requests) - 1):
            total_head_movements += abs(requests[index] - requests[index + 1])
            if index == len(requests) - 1:
                plus_symbol = ""          
            else: 
                plus_symbol = " +"
            if requests[index] > requests[index + 1]:
                bigger = requests[index]
                smaller = requests[index + 1]
            else:
                bigger = requests[index + 1]
                smaller = requests[index]

            head_movements_calculation_string.append("(" + str(bigger) + "-" + str(smaller) + ")" + plus_symbol)

        head_movements_calculation_string = " ".join(head_movements_calculation_string)
        head_movements_calculation_string = head_movements_calculation_string.rstrip('+')
        print(f"FCFS: {head_movements_calculation_string}")
        print(f"FCFS: {requests}")
        return rand_floats, total_head_movements, head_movements_calculation_string, requests