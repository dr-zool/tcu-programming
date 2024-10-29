import array

def insertElement(arr, x, pos):
    n = len(arr)  # Current length of the array
    if pos < 0 or pos > n:  # Validate the position
        raise IndexError("Position out of range")

    # Create a new array with one more element
    new_arr = array.array(arr.typecode, [0] * (n + 1))

    # Copy elements to the new array
    for i in range(pos):
        new_arr[i] = arr[i]
    new_arr[pos] = x
    for i in range(pos, n):
        new_arr[i + 1] = arr[i]

    return new_arr


# Example usage
arr = array.array('i', [1, 2, 3, 4, 5])
x = 1  # Element to insert
pos = 2  # Position to insert the element

# Insert element
arr = insertElement(arr, x, pos)
print(arr.tolist())  # Convert to list for easy viewing
