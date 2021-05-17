guest_schdules = [(6,8), (6,12), (6,7), (7,8),
        (7,10), (8,9), (8,10), (9,12),
        (9,10), (10,11), (10,12), (11,12)]
times = []

for schd in guest_schdules:
    times.append(('start', schd[0]))
    times.append(('end', schd[1]))

times_sorted = sorted(times, key=lambda x: x[1])

current_guest = 0
max_time = max_value = 0
for time in times_sorted:
    if time[0] == 'start':
        current_guest += 1
    elif time[0] == 'end':
        current_guest -= 1

    if max_time < time[1]:
        max_time = time[1]
        max_value = current_guest

print("Answer:", "time=", max_time, "num_of_guest=", max_value)
