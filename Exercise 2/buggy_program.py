# Exercise 2 - Task 1: Corrected Program
def calculate_even_average(numbers):
    total_sum = 0
    count = 0
    
    # Fix 1 & 2: Clean iteration without out-of-bounds indexing or undefined variables
    for num in numbers:
        if num % 2 == 0:
            total_sum += num
            count += 1
            
    if count == 0:
        return 0
        
    average = total_sum / count
    # Fix 3: Explicitly return the calculated average
    return average


if __name__ == "__main__":
    sample_data = [2, 4, 6, 7, 9]
    result = calculate_even_average(sample_data)
    print("Calculated average of even numbers:", result)