# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insert_end(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n


# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def remove_end(arr, length):
    if length > 0:
        arr[length - 1] = 0


# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insert_at_position(arr, n, i, length):
    # range(start,stop,step)
    # we do 1 minus for length and 1 minus because we need to target next item of the array in each iteration
    for index in range(length - 2, i - 1, -1):
        arr[index + 1] = arr[index]
    arr[i] = n


# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def remove_at_position(arr, i, length):
    # we shift left item of array to right
    for index in range(i + 1, length):
        # we do plus 1 in the passing i because we need to target previous item of array in each iteration
        print(index)
        arr[index - 1] = arr[index]
    print(arr)


remove_at_position([1, 2, 3, 4, 5, 6], 1, 6)

# insert_at_position([1,2,3,4,5,6], 100, 2, 6)