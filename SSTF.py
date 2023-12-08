import numpy as np
class SSTF:
    currentTime = 0

    def find_shortest_seek_time(self, data, head):
        return min(data, key=lambda x: abs(x - head))

    def executeAlgorithm(self, requests):
        
        ## Arranging of data
        temp = [requests[i] for i in range(1, len(requests))]
        head = requests[0]
        temp_data = []

        while temp:
            shortest_seek_time_element = self.find_shortest_seek_time(temp, head)
            
            # Append the shortest seek time element to the sorted array
            temp_data.append(shortest_seek_time_element)
            
            # Update the current number for the next iteration
            head = shortest_seek_time_element
            
            # Remove the selected element from my_data
            temp.remove(shortest_seek_time_element)

        temp_data.insert(0, requests[0])
        
        rand_floats = [self.currentTime]
        for i in range(len(requests) - 1):
            # self.currentTime += np.random.random_integers(0, 10)
            self.currentTime += 1
            # if self.currentTime in rand_floats:
            #     self.currentTime += 0.5
            rand_floats.append(self.currentTime)

        head_movements_calculation_string = []
        total_head_movements = 0


        for  index in range(len(temp_data) - 1):
            total_head_movements += abs(temp_data[index] - temp_data[index + 1])
            if index == len(temp_data) - 1:
                plus_symbol = ""          
            else: 
                plus_symbol = " +"
            if temp_data[index] > temp_data[index + 1]:
                bigger = temp_data[index]
                smaller = temp_data[index + 1]
            else:
                bigger = temp_data[index + 1]
                smaller = temp_data[index]

            head_movements_calculation_string.append("(" + str(bigger) + "-" + str(smaller) + ")" + plus_symbol)

        head_movements_calculation_string = " ".join(head_movements_calculation_string)
        head_movements_calculation_string = head_movements_calculation_string.rstrip('+')
        return rand_floats, total_head_movements, head_movements_calculation_string, temp_data



