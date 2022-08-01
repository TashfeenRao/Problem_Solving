"""
recursion is when function call itself again and again until it hit the base case we have two cases in recursion
the base case which tells use when we will finish and returned recursive case which will continue the operations
 until we hit base case for return recursion uses the stack internally; which follows the LIFO(last in first out);
 stack has two functions pop and push.
 rule. recursion is same as call stack in programming languages interpreter every function call creates a memory and
 implementation code stack box; if we call multiple function inside one function than the every function call create
it's own memory box for implementation of that function; each function has access to it's own memory others
function can't access it.
"""


# Q1: you have given an array return the total sum of all elements in array using the recursive call

def total_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + total_sum(arr[1:])


# step 1: 3 + total_sum([2,4]) => this returns 3 + 6 (return value from executing the total_sum([2,4)) = 9
# step 2: 2 + total_sum([4]) => this returns 2 + 4 (return value from executing the total_sum([4)) = 6
# step 3: 4 + total_sum([]) => this returns 4 + 0 (return value from executing the total_sum([]))
# step 4:  hit the base case => this returns 0

total_sum([3, 2, 4])