# the challenge:
# Imagine you have 100 doors in a row, that are all initially closed
# You make 100 passes by the doors
# On the first pass, you visit every door in sequence and toggle its state (if the door is open, close it, if its closed, open it)
# On the second pass, you visit every 2nd door and total its state
# On the third pass, you visit every 3rd door and total its state
# ... and this process repeats until you only visit the 100th door on the 100th pass
# The Question: Which doors are open at the end of the last pass?


# false represents a closed door, true represents an open door
# using 101 so we can use the actual index
doors = [False] * 101

# iterate over the doors
for i in range(1, 101):
    # use the outer loop counter as the step and value
    for j in range(i, 101, i):
        print(f"i: {i}; j: {j}; step size: {i}. Toggling door number: {j}.")
        # toggle door state
        doors[j] = not doors[j]

# print out the result
for i in range(1, 101):
    # print out which doors are open
    if doors[i] is True:
        print(f"Door number {i} remains open.")
