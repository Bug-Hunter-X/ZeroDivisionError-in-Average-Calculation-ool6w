def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (will now return 0):
my_list = []
result = calculate_average(my_list)
print(result)  # Output: 0

# Example with non-empty list
my_list = [10, 20, 30]
result = calculate_average(my_list)
print(result) # Output: 20.0