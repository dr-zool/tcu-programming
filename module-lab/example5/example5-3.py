# Python program for searching in unsorted array

def findElement(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    # If the key is not found
    return -1


# Example usage
if __name__ == "__main__":
    # Define an unsorted array
    arr = [4, 2, 7, 1, 9, 3]

    # Key to search for
    key = 7

    # Get the length of the array
    n = len(arr)

    # Call the function
    index = findElement(arr, n, key)

    # Print the result
    if index != -1:
        print(f"Element {key} found at index {index}.")
    else:
        print(f"Element {key} not found in the array.")
