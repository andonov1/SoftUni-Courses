from collections import deque

peaks = {'Vihren': 80,
         'Kutelo': 90,
         'Banski Suhodol': 100,
         'Polezhan': 60,
         'Kamenitza': 70}

food = [int(s) for s in input().split(', ')]
stamina = deque([int(s) for s in input().split(', ')])
climbed_peaks = []
food_finished = False

for peak, difficulty in peaks.items():
    while food:
        power = food.pop() + stamina.popleft()

        if power >= difficulty:
            climbed_peaks.append(peak)
            break
    if not food:
        food_finished = True
        break

if len(climbed_peaks) == len(peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if climbed_peaks:
    print(f"Conquered peaks:")
    print(*climbed_peaks, sep='\n')
