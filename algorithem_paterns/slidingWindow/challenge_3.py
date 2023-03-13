# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
# Example 1:
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:
# Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".
# Example 3:
# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.

def challenge_3(string: str, pattern: str):
    window_start, matched, sub_str_start = 0,0,0
    window_min_length = len(string) + 1
    frequency_char = {}
    
    for char in string:
        if char not in frequency_char:
            frequency_char[char] = 0
        frequency_char[char] += 1
    
    for window_end in range(len(string)):
        right_char = string[window_end]
        
        if right_char in frequency_char:
            frequency_char[right_char] -= 1
            if frequency_char[right_char] >= 0:
                matched += 1
        
        while matched == len(pattern):
            if window_min_length > window_end - window_start +1:
                window_min_length = window_end - window_start +1
            sub_str_start = window_start
            
            left_char = string[window_start]
            window_start += 1
            
            if left_char in frequency_char:
                if frequency_char[left_char] == 0:
                    matched -= 1
                frequency_char[left_char] += 1
    if window_min_length > len(string):
        return ""
    return string[sub_str_start:sub_str_start+window_min_length]
            
        
        
            