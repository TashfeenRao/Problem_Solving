# Given a string and a pattern, find out if the string contains any permutation of the pattern.
#
# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
#
# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have
# �
# !
# n! permutations.
#
# Example 1:
#
# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:
#
# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:
#
# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.


def challenge_1(string:str, pattern:str):
    window_start, matched = 0, 0
    char_frequency = {}
    
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
            
    for window_end in range(len(string)):
        right_char = string[window_end]
        
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        if matched == len(char_frequency):
            return True
        
        if window_end >= len(pattern)-1:
            left_char = string[window_start]
            window_start += 1
            
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return False
    
print(challenge_1("oidbcaf","abc")) # expect true
print(challenge_1("odicf","dc")) # expect false
print(challenge_1("bcdxabcdy","bcdyabcdx")) # expect true
