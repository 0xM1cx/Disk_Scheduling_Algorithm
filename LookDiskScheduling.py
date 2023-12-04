
data = []
lookDataList= []
counter = 0

requestNumber = int(input("Enter number of request: "))

for item in range(1, requestNumber+1):
    tempRequestSequence = int(input(f"Process #{item}: "))
    data.append(tempRequestSequence)

print(f"Unsorted: {data}") # Unsorted Data
data.sort()
print(f"Sorted: {data}") # Sorted Data

initialHeadPosition = int(input("Enter Head Position: "))
# c_lookDataList.append(initialHeadPosition)
totalDiskSize = int(input("Enter Disk Size: "))
direction = (input("Enter Direction[High / Low]: "))


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
            

    print(f"\nProcess: {data}")
    print(f"Graph: {lookDataList}")



