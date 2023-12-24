import numpy as np
def LOOK(totalDiskSize, initialHeadPosition, direction, requested_tracks):
    data = requested_tracks
    lookDataList= []
    counter = 0

    data.sort()

    initialHeadPosition = initialHeadPosition
    # c_lookDataList.append(initialHeadPosition)
    totalDiskSize = totalDiskSize
    direction = direction

    requestNumber = len(data)

    
    if direction == "high":
        for item in range(requestNumber):
            if data[item] == initialHeadPosition:
                counter = item
                for i in range(requestNumber-item): 
                    lookDataList.append(data[item])
                    item+=1

                for j in range(counter):
                    lookDataList.append(data[counter-1])
                    counter-=1

        print(f"\nProcess: {data}")
        print(f"Graph: {lookDataList}")
        counter = 0



    elif direction.lower() == "low":
        for item in range(requestNumber):
            if data[item] == initialHeadPosition:
                counter = item
                for i in range(item+1):
                    lookDataList.append(data[item])
                    item-=1

                for j in range(requestNumber-len(lookDataList)):
                    lookDataList.append(data[requestNumber-1])
                    requestNumber-=1


    currentTime = 0
    rand_floats = [currentTime]
    for i in range(len(requested_tracks)-1):
        currentTime += np.random.random_integers(1, 10) 
        if currentTime in rand_floats:
            currentTime += 0.5 + np.random.random_integers(1, 10) + np.random.uniform(0.1, 0.9)
        rand_floats.append(currentTime)

    head_movements_calculation_string = []
    total_head_movements = 0
    # Calculation of total number of head movements
    for  index in range(len(lookDataList) - 1):
        total_head_movements += abs(lookDataList[index] - lookDataList[index + 1])
        if index == len(lookDataList) - 1:
            plus_symbol = ""          
        else: 
            plus_symbol = " +"
        if lookDataList[index] > lookDataList[index + 1]:
            bigger = lookDataList[index]
            smaller = lookDataList[index + 1]
        else:
            bigger = lookDataList[index + 1]
            smaller = lookDataList[index]

        head_movements_calculation_string.append("(" + str(bigger) + "-" + str(smaller) + ")" + plus_symbol)

    head_movements_calculation_string = " ".join(head_movements_calculation_string)
    head_movements_calculation_string = head_movements_calculation_string.rstrip('+')
    return rand_floats, total_head_movements, head_movements_calculation_string, lookDataList