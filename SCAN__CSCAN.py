import numpy as np

def SCAN(total_tracks, current_head, direction, requested_tracks):
    outermost_track = 0
    innermost_track = total_tracks - 1
    
    track_list = []
    
    if direction.upper() == "U":
        track_list = [innermost_track, current_head]
    elif direction.upper() == "D":
        track_list = [outermost_track, current_head]
    
    track_list.extend(requested_tracks)
    track_list.sort()
    
    sequence = []
    
    if direction.upper() == "U":
        upward_scan = [track for track in track_list if current_head <= track]
        downward_scan = [track for track in reversed(track_list) if current_head > track]
        sequence = upward_scan + downward_scan
    elif direction.upper() == "D":
        upward_scan = [track for track in track_list if current_head < track]
        downward_scan = [track for track in reversed(track_list) if current_head >= track]
        sequence = downward_scan + upward_scan
    
    head_movements_calculation_string = []
    total_head_movements = 0
    
    currentTime = 0
    rand_floats = [currentTime]
    for i in range(len(sequence)-1):
        currentTime += np.random.random_integers(0, 10) 
        if currentTime in rand_floats:
             currentTime += 0.5
        rand_floats.append(currentTime)




    for index in range(len(sequence) - 1):
        total_head_movements += abs(sequence[index] - sequence[index + 1])
        if index == len(sequence) - 1:
                plus_symbol = ""          
        else: 
            plus_symbol = " +"
        if sequence[index] > sequence[index + 1]:
            bigger = sequence[index]
            smaller = sequence[index + 1]
        else:
            bigger = sequence[index + 1]
            smaller = sequence[index]

        head_movements_calculation_string.append("(" + str(bigger) + "-" + str(smaller) + ")" + plus_symbol)

        
    _head_movements_calculation_string = " ".join(head_movements_calculation_string)
    return  rand_floats, total_head_movements, _head_movements_calculation_string, sequence 
    
def CSCAN(total_tracks, current_head, direction, requested_tracks):
    outermost_track = 0
    innermost_track = total_tracks - 1
    
    track_list = [outermost_track, innermost_track, current_head]
    track_list.extend(requested_tracks)
    track_list.sort()
    
    sequence = []
    
    if direction.upper() == "U":
        upward_scan = [track for track in track_list if current_head <= track]
        downward_scan = [track for track in track_list if current_head > track]
        sequence = upward_scan + downward_scan
    elif direction.upper() == "D":
        upward_scan = [track for track in reversed(track_list) if current_head < track]
        downward_scan = [track for track in reversed(track_list) if current_head >= track]
        sequence = downward_scan + upward_scan
    
    

    head_movements_calculation_string = []
    total_head_movements = 0
    
    currentTime = 0
    rand_floats = [currentTime]
    for i in range(len(sequence)-1):
        currentTime += np.random.random_integers(0, 10)
        if currentTime in rand_floats:
             currentTime += 0.5
        rand_floats.append(currentTime)


    for index in range(len(sequence) - 1):
            total_head_movements += abs(sequence[index] - sequence[index + 1])
            if index == len(sequence) - 1:
                    plus_symbol = ""          
            else: 
                plus_symbol = " +"
            if sequence[index] > sequence[index + 1]:
                bigger = sequence[index]
                smaller = sequence[index + 1]
            else:
                bigger = sequence[index + 1]
                smaller = sequence[index]

            head_movements_calculation_string.append("(" + str(bigger) + "-" + str(smaller) + ")" + plus_symbol)

            
    head_movements_calculation_string = " ".join(head_movements_calculation_string)
    head_movements_calculation_string = head_movements_calculation_string.rstrip('+')
    return  rand_floats, total_head_movements, head_movements_calculation_string, sequence  
