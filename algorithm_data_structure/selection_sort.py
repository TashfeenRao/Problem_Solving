
def get_minimum(arr):
    lowest_number = arr[0]
    lowest_index = 0
    
    for index, item in enumerate(arr):
        if item < lowest_number:
            lowest_number = item
            lowest_index = index
            
    return lowest_index


def selection_sort(arr):
    sorted_arr = []
    lowest_index = 0
    for item in range(len(arr)):
        lowest_index = get_minimum(arr)
        sorted_arr.append(arr.pop(lowest_index))
    
    return sorted_arr


print(selection_sort([4,3,2,21]))