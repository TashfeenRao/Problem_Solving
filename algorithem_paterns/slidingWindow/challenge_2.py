# Given a string and a pattern, find all anagrams of the pattern in the given string.
# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
# Example 1:
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:
# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


def challenge_2(string: str,pattern: str):
    
    window_start,matched, result = 0, 0, []
    char_frequency = {}
    
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
        
    
    for window_end in range(len(string)):
        
        right_char = string[window_end]
        if right_char in char_frequency:
            # we found a char in our frequency we decrement the frequency record by one
            char_frequency[right_char] -= 1
            
            if char_frequency[right_char] == 0:
                # when count get 0 meaning all occurrences of char is in string we found a match
                matched += 1
        # have we found anagram from current window
        if matched == len(char_frequency):
            # matched will become equal to char frequency when all the char are matched meaning count is 0
            result.append(window_start)
            
        if window_end >= len(pattern)-1:
            # we hit the base length of the pattern
            # we will move the window and make the char count back to make sure we find next matching
            left_char = string[window_start]
            window_start += 1
            
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1 # decrement the matched count
                char_frequency[left_char] += 1 # put the character count back
    
    return result


print(challenge_2("ppqp", "pq")) # expects [1,2]
print(challenge_2("abbcabc", "abc")) # expects [2,3,4]