arrival_hr = int(input())
arrival_min = int(input())
departure_hr = int(input())
departure_min = int(input())

arrival_time = arrival_hr * 60 + arrival_min
departure_time = departure_hr * 60 + departure_min

if departure_time < arrival_time:
    departure_time += 24 * 60

total_parking_minute = departure_time - arrival_time
cost = 0

if total_parking_minute <= 15:
    cost += 0
elif total_parking_minute > 15 and total_parking_minute <= 180:
    cost += (total_parking_minute // 60) * 10 
    if total_parking_minute % 60 > 0:
        cost += 10
elif total_parking_minute > 180 and total_parking_minute <= 240:
    cost += 30
    remaining_minutes = total_parking_minute - 180
    if remaining_minutes > 0:
        cost += 20
elif total_parking_minute > 240 and total_parking_minute <= 360:  
    cost += 30  
    cost += 20 
    remaining_minutes = total_parking_minute - 240
    if remaining_minutes > 60:
        cost += (remaining_minutes // 60) * 20
        if remaining_minutes % 60 > 0:
            cost += 20
    elif remaining_minutes > 0:
        cost += 20
elif total_parking_minute > 360:
    cost = 200

print(cost)