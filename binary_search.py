import random


def make_random_data(number_of_values=10, max_value=100):
    return [random.randint(1, max_value) for i in range(number_of_values)]


def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while (low <= high):
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


data = make_random_data()
data.sort()
print(data)

print(binary_search(data, 1))
