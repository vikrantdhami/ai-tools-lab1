"""
AI Tools Lab (AGCS-25308) - Exercise 2 Task 1: Debugging Demonstration
Author: Vikrant Singh
Repository: ai-tools-lab1
"""

# ==============================================================================
# SECTION 1: ORIGINAL BUGGY IMPLEMENTATION (FOR REFERENCE & LAB EVIDENCE)
# ==============================================================================
"""
def calculate_even_average_buggy(numbers):
    total_sum = 0
    count = 0
    
    # Bug 1: Off-by-one error (range extends past valid indices: len(numbers) + 1)
    # Causes: IndexError: list index out of range
    for i in range(len(numbers) + 1):
        # Bug 2: Wrong variable name (referenced undeclared variable 'num')
        # Causes: NameError: name 'num' is not defined
        if num % 2 == 0:
            total_sum += numbers[i]
            count += 1
            
    if count == 0:
        return 0
        
    average = total_sum / count
    # Bug 3: Missing return statement (silently yields None instead of the result)
"""

# ==============================================================================
# SECTION 2: CORRECTED IMPLEMENTATION
# ==============================================================================
def calculate_even_average(numbers):
    """
    Calculates the arithmetic mean of all even integers in the provided list.
    
    Fixes applied:
    - Replaced index-based range with direct collection iteration (resolves IndexError).
    - Referenced the loop variable directly (resolves NameError).
    - Added explicit return statement returning the calculated float (resolves missing return).
    """
    total_sum = 0
    count = 0
    
    # Direct iteration avoids index manipulation and boundary risks
    for val in numbers:
        if val % 2 == 0:
            total_sum += val
            count += 1
            
    # Guard against division by zero if no even numbers exist
    if count == 0:
        return 0.0
        
    average = total_sum / count
    return average


# ==============================================================================
# SECTION 3: VERIFICATION RUNNER
# ==============================================================================
if __name__ == "__main__":
    sample_data = [2, 4, 6, 7, 9]
    result = calculate_even_average(sample_data)
    print("Calculated average of even numbers:", result)