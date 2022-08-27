def binary_search(find_me_in_list: int, the_list: list):
    the_list = sorted(the_list)
    start = 0
    list_length = len(the_list)
    end = list_length - 1

    while start <= end:
        mid = int((start + end) / 2)
        if the_list[mid] == find_me_in_list:
            return print("Yes! we find it in the sorted list at index", mid)
        elif the_list[mid] < find_me_in_list:
            start = mid + 1
        elif the_list[mid] > find_me_in_list:
            end = mid - 1
    return print("Sorry! we could not find this number in the list")


binary_search(1, [2, 3, 5, 61, 2])
