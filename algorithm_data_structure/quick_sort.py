def quick_sort_average_case(array):
    # base case is when array has only one element or empty
    if len(array) < 2:
        return array
    else:
        mid = int((len(array)/2))
        print(mid)
        pivot = array[mid]
        left = [item for item in array[mid:] if item <= pivot]
        right = [item for item in array[mid:] if item >= pivot]
        
    return quick_sort_average_case(left) + [pivot] + quick_sort_average_case(right)
print(quick_sort_average_case([3,2,9,7,3,2]))

# pivot = 7,




# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#
#         less = [item for item in array[1:] if item <= pivot]
#         greater = [item for item in array[1:] if item > pivot]
#
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print(quick_sort([3,6,2,7,3,2]))



''''
dry run for quick sort:

[2,2,3] + [3] + quick_sort([6,7]) => [6,7]
[2,2,3] + [3] + [6,7]
sorted_arr = [2,2,3,3,6,7]
quick_sort([]) => [] + [6] + quick_sort[7] => [7]
returns [6,7]
quick_sort([2,3,2]) returns [2,2,3]
quick_sort([2]) return with [2] + [2] + quick_sort([3])
[2] + [2] + quick_sort([3]) return [3] so it becomes [2,2,3]


step 1: pivot = 3 and less_partition_arr = [2,3,2] and greater_partition_arr = [6,7] we called the recursive function using less
step 2: pivot = 2 and less_partition_arr = [2] and greater_partition_arr = [3] recursive call again using less array
step 3: Now the elements in less array is 1 so it hit the base case and return the array which is [2] + [2] + recursive call with greater array [3]
step 4: the base case again get hit with one element in greater arr which is [3] so this also gets return

'''