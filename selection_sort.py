# Selection Sort:
# - Find the smallest element in the array and exchange it with the element in the first position
# - Repeat: Find the second smallest element in the array and exchange it with the element in the second position
# - Repeat: Continue the pattern above until all elements have been sorted


def get_min_value(data):
    min = 0
    for i in range(len(data)):
        if data[i] < data[min]:
            min = i
    return data[min]


def selection_sort(data):
    """
    inplace selection sort function
    """
    for i in range(len(data) - 1):
        # find the minimum value in unsorted region
        min_index = i
        for j in range(i + 1, len(data)):
            # update the min_index if the value at j is lower than the current minimum value
            if data[j] < data[min_index]:
                min_index = j
        # after finding the minimum value in the unsorted region, swap the first unsorted value
        data[i], data[min_index] = data[min_index], data[i]


data = [3, 2, 1, 5, 4, 6, 9]
selection_sort(data)
print(data)
