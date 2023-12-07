times = [51, 92, 68, 90]
distances = [222, 2031, 1126, 1225]
ways = [0, 0, 0, 0]

for i in range(0, 4):
    print(i)
    for j in range(0, times[i]+1):
        distance = j * (times[i] - j)
        print(f"Distance this run: {distance}")
        if distance > distances[i]:
            ways[i] += 1
    print(f"Ways to win for race {i}: {ways[i]}")

print(ways[0] * ways[1] * ways[2] * ways[3])
