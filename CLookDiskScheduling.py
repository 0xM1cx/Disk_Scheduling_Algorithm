
import numpy as np
def CLOOK(totalDiskSize, initialHeadPosition, direction, requested_tracks):
    data = requested_tracks
    c_lookDataList= []
    counter = 0

    # requestNumber = int(input("Enter number of request: "))

    # for item in range(1, requestNumber+1):
    #     tempRequestSequence = int(input(f"Process #{item}: "))
    #     data.append(tempRequestSequence)

    # print(f"Unsorted: {data}") # Unsorted Data
    data.sort()
    # print(f"Sorted: {data}") # Sorted Data

    # initialHeadPosition = int(input("Enter Head Position: "))
    initialHeadPosition = initialHeadPosition
    # c_lookDataList.append(initialHeadPosition)
    # totalDiskSize = int(input("Enter Disk Size: "))
    totalDiskSize = totalDiskSize
    # direction = (input("Enter Direction[High / Low]: "))
    direction = direction

    requestNumber = len(data)
    if direction == "high":
        for item in range(requestNumber):
            if data[item] == initialHeadPosition:
                counter = item
                for i in range(requestNumber-item): 
                    c_lookDataList.append(data[item])
                    item+=1

                for j in range(counter):
                    c_lookDataList.append(data[j])

        # print(f"\nProcess: {data}")
        # print(f"Graph: {c_lookDataList}")



    elif direction.lower() == "low":
        for item in range(requestNumber):
            if data[item] == initialHeadPosition:
                for i in range(item+1):
                    c_lookDataList.append(data[item])
                    item-=1
                
                for j in range(requestNumber-len(c_lookDataList)):
                    c_lookDataList.append(data[requestNumber-1])
                    requestNumber-=1

        # print(f"\nProcess: {data}")
        # print(f"Graph: {c_lookDataList}")
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
    for  index in range(len(requested_tracks) - 1):
        total_head_movements += abs(requested_tracks[index] - requested_tracks[index + 1])
        if index == len(requested_tracks) - 1:
            plus_symbol = ""          
        else: 
            plus_symbol = " +"
        if requested_tracks[index] > requested_tracks[index + 1]:
            bigger = requested_tracks[index]
            smaller = requested_tracks[index + 1]
        else:
            bigger = requested_tracks[index + 1]
            smaller = requested_tracks[index]

        head_movements_calculation_string.append("(" + str(bigger) + "-" + str(smaller) + ")" + plus_symbol)

    head_movements_calculation_string = " ".join(head_movements_calculation_string)
    head_movements_calculation_string = head_movements_calculation_string.rstrip('+') 
    return rand_floats, total_head_movements, head_movements_calculation_string, c_lookDataList
