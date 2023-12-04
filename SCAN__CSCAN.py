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
    
    head_movements = []
    total_head_movements = 0
    
    print("SCAN Disk Scheduling")
    print(f"Number of Tracks: {total_tracks}")
    print(f"\t- Outermost Track: {outermost_track}")
    print(f"\t- Innermost Track: {innermost_track}")
    
    if direction.upper() == "U":
        print("Movement Direction: Upward")
    elif direction.upper() == "D":
        print("Movement Direction: Downward")
        
    print(f"Requested Tracks: {requested_tracks}\n")
    
    print("Sequence: ", end="")
    print(*sequence, sep=" => ")
            
    for index in range(len(sequence) - 1):
        head_movements.append(abs(sequence[index] - sequence[index + 1]))
        total_head_movements += abs(sequence[index] - sequence[index + 1])
            
    print("Head Movements: ", end="")
    print(*head_movements, sep=" + ")
    
    print(f"Total Head Movements: {total_head_movements} Tracks")
    
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
    
    head_movements = []
    total_head_movements = 0
    
    print("C-SCAN Disk Scheduling")
    print(f"Number of Tracks: {total_tracks}")
    print(f"\t- Outermost Track: {outermost_track}")
    print(f"\t- Innermost Track: {innermost_track}")
    
    if direction.upper() == "U":
        print("Movement Direction: Upward")
    elif direction.upper() == "D":
        print("Movement Direction: Downward")
        
    print(f"Requested Tracks: {requested_tracks}\n")
    
    print("Sequence: ", end="")
    print(*sequence, sep=" => ")
            
    for index in range(len(sequence) - 1):
        head_movements.append(abs(sequence[index] - sequence[index + 1]))
        total_head_movements += abs(sequence[index] - sequence[index + 1])
            
    print("Head Movements: ", end="")
    print(*head_movements, sep=" + ")
    
    print(f"Total Head Movements: {total_head_movements} Tracks")
    
    
SCAN(200, 70, "U", [118, 59, 110, 25, 105, 63, 100, 28, 80])
print()
print("-" * 100)
print()
SCAN(200, 70, "D", [118, 59, 110, 25, 105, 63, 100, 28, 80])
print()
print("-" * 100)
print()
CSCAN(200, 70, "U", [118, 59, 110, 25, 105, 63, 100, 28, 80])
print()
print("-" * 100)
print()
CSCAN(200, 70, "D", [118, 59, 110, 25, 105, 63, 100, 28, 80])