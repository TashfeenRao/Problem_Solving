# 1: Given an array of positive numbers and a positive number ‘k’,
# find the maximum sum of any contiguous subarray of size ‘k’.
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
import math


# sliding window algorithm

def contiguous_sum(arr=[2, 1, 5, 1, 3, 2], k=3):
    start_window = 0
    window_sum = 0
    max_sum = 0
    
    for end_window in range(len(arr)):
        window_sum += arr[end_window]
        if end_window >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start_window]
            start_window += 1
    return max_sum


print(contiguous_sum())


# Given an array of positive numbers and a positive number ‘S’,
# find the length of the smallest contiguous subarray whose sum is greater
# than or equal to ‘S’. Return 0, if no such subarray exists.
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

def smallest_contiguous_subarray(arr=[2, 1, 5, 2, 3, 2], s=7):
    window_start = 0
    window_sum = 0
    # length of subarray which is smallest
    min_length = math.inf
    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, (window_end - window_start) + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    if min_length == math.inf:
        return 0
    
    return min_length


print(smallest_contiguous_subarray())


# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# Input: String = "araaci", K = 2
# Output: 4
# Explanation: The
# longest
# substring
# with no more than '2' distinct characters is "araa".

def longest_contiguous_substring(arr='araaci', k=2):
    max_length = 0
    window_start = 0
    frequency = {}
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char not in frequency:
            frequency[right_char] = 0
        frequency[right_char] += 1
        # if we hit the case where frequency got greater characters than allowed distinct char k
        while len(frequency) > k:
            left_char = arr[window_start]
            # we will minus the number
            frequency[left_char] -= 1
            # and delete the extra char in frequency
            if frequency[left_char] == 0:
                del frequency[left_char]
            # shrink the window by moving the start to forward
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(longest_contiguous_substring())

# Given an array of characters where each character represents a fruit tree,
# you are given two baskets and your goal is to put maximum number of fruits in each basket.
# The only restriction is that each basket can have only one type of fruit.
# You can start with any tree, but once you have started you can’t skip a tree.
# You will pick one fruit from each tree until you cannot, i.e.,
# you will stop when you have to pick from a third fruit type.
# Input: Fruit = ['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray
# ['C', 'A', 'C']

def max_fruit_each_basket(str=['A', 'B', 'C', 'A', 'C']):
    frequency = {}
    window_start = 0
    max_length = 0
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in frequency:
            frequency[right_char] = 0
        frequency[right_char] += 1
        while len(frequency) > 2:
            left_char = str[window_start]
            frequency[left_char] -= 1
            if frequency[left_char] == 0:
                del frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    return max_length
    
    
print(max_fruit_each_basket())




# Given a string, find the length of the longest substring which has no repeating characters.
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".


def longest_substring_length(str='aabccbb'):
    max_length = 0
    window_start = 0
    frequency = {}
    for window_end in range(len(str)):
        right_char = str[window_end]
        
        if right_char in frequency:
            window_start = max(window_start,frequency[right_char]+1)
        
        frequency[right_char] = window_end
        max_length = max(max_length, window_end - window_start+1)
    return max_length

print(longest_substring_length())