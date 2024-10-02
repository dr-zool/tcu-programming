def even_or_odd_in_range(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:  # Fixed missing comparison operator '=='
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

# Example usage
even_or_odd_in_range(111, 510)  # Replaced 'l' with '1' to match the example usage
