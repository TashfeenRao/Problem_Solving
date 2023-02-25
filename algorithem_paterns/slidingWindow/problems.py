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