import math

# distance between two GPS points (simple version)
def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def verify_session(gps_points):
    
    if len(gps_points) < 2:
        return "FAKE"
    
    total_distance = 0
    
    for i in range(len(gps_points) - 1):
        p1 = gps_points[i][:2]
        p2 = gps_points[i+1][:2]
        
        dist = calculate_distance(p1, p2)
        
        # ignore GPS noise
        if dist > 0.0001:
            total_distance += dist
    
    start_time = gps_points[0][2]
    end_time = gps_points[-1][2]
    
    total_time = end_time - start_time
    
    if total_time == 0:
        return "FAKE"
    
    speed = total_distance / total_time
    
    # simple classification
    if total_distance < 0.001:
        return "FAKE"
    
    elif speed < 0.0001:
        return "SUSPICIOUS"
    
    else:
        return "VALID"
    
gps_data = [
    (10.0, 20.0, 0),
    (10.0005, 20.0005, 10),
    (10.001, 20.001, 30) ]

print(verify_session(gps_data))