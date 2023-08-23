# false represents a closed door, true represents an open door
# using 101 so we can use the actual index
doors = [False] * 101

# iterate over the doors
for i in range(1, 101):
    # use the outer loop counter as the step and value
    for j in range(i, 101, i):
        doors[j] = not doors[j]

# print out the result
for i in range(1, 101):
    if doors[i] is True:
        print(i, end=", ")
