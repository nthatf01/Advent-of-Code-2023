#Day 6
#Part 1

import math

times = [51, 92, 68, 90]
distances = [222, 2031, 1126, 1225]
ways = [0, 0, 0, 0]

for i in range(0, 4):
    print(i)
    for j in range(0, times[i]+1):
        distance = j * (times[i] - j)
        #print(f"Distance this run: {distance}")
        if distance > distances[i]:
            ways[i] += 1
    #print(f"Ways to win for race {i}: {ways[i]}")

print(ways[0] * ways[1] * ways[2] * ways[3])

#Part 2

time = 51926890
distance = 222203111261225

#distance < pressed * (time - pressed)
#distance < pressed * time - pressed ^ 2
#222203111261225 < pressed * 51926890 - pressed ^ 2
#0 < -pressed ^ 2 + 51926890 * pressed - 222203111261225

a = -1
b = 51926890
c = -222203111261225

#QUADRATIC FORMULA
x = (((-1) * b) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)

print(x)

y = time - 2 * x

print(y)
