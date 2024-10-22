from array import array


# Function to search for a key in the array
def findElement(arr, key):
    for i in range(len(arr)):
        # Return the index if key is found
        if arr[i] == key:
            return i
    # Return -1 if key is not found
    return -1


# Function to delete an element from the array
def deleteElement(arr, key):
    # Find position of element to be deleted
    pos = findElement(arr, key)

    if pos == -1:
        print("Element not found")
        return arr

    # Creating a new array with one less element
    new_arr = array(arr.typecode, [0] * (len(arr) - 1))

    # Copy elements except the one to be deleted
    for i in range(pos):
        new_arr[i] = arr[i]
    for i in range(pos + 1, len(arr)):
        new_arr[i - 1] = arr[i]

    return new_arr


# Example usage
arr = array('i', [1, 2, 3, 4, 5])
key_to_delete = 3

# Find the element
print(f"Index of {key_to_delete}: {findElement(arr, key_to_delete)}")

# Delete the element
arr = deleteElement(arr, key_to_delete)
print("Array after deletion:", arr.tolist())
