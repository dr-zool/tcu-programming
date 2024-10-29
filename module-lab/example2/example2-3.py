#Exam
def find_perfect_number(limit):
    for num in range(2, limit):
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        if divisors_sum == num:
            print(f"{num} is a perfect number")
            break  # Exit after finding the first perfect number
    else:
        print("No perfect number found in the range")

# Example usage
find_perfect_number(1000)  # Expected: 6 is a perfect number
