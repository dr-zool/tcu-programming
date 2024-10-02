def classify_number(n):
    if 0 < n <= 10:
        return "Small"
    elif 10 < n <= 100:
        return "Medium"
    elif n > 100:
        return "Large"
    else:
        return "Invalid"

# Example usage
print(classify_number(-1))   # Expected: Small
print(classify_number(-50))  # Expected: Medium
print(classify_number(150)) # Expected: Large
