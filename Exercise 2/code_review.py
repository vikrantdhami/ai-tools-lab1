"""
AI Tools Lab (AGCS-25308) - Exercise 2 Task 3: AI Code Review
Author: Vikrant Singh
Repository: ai-tools-lab1
"""

# ==============================================================================
# 1. ORIGINAL MESSY FUNCTION (BEFORE REVIEW)
# ==============================================================================
# Problems:
# - Cryptic variable names ('l', 'x', 't')
# - Violates PEP 8 naming conventions (PascalCase/CamelCase for functions)
# - Redundant manual list accumulation instead of Pythonic idioms
# - No type hints or docstrings
# - Crashes on empty list or non-numeric items

def ProcessData(l):
    x = []
    for t in range(len(l)):
        if l[t] > 10 and l[t] % 2 == 0:
            x.append(l[t] * 2)
    return x


# ==============================================================================
# 2. AI CODE REVIEW FINDINGS
# ==============================================================================
"""
Review Summary:
1. Readability & Conventions (PEP 8):
   - Function name 'ProcessData' violates PEP 8 snake_case convention; should be 'process_even_multipliers'.
   - Single-letter identifiers ('l', 'x', 't') obscure the domain purpose.
   - Missing docstrings and type annotations.

2. Code Smells & Pythonic Idioms:
   - Index-based looping `range(len(l))` is anti-idiomatic in Python. Iterating directly or using list comprehensions is cleaner and faster.
   - Filtering and transformation can be achieved in a single readable list comprehension or generator.

3. Edge Cases & Robustness:
   - Fails if the collection contains `None` or non-integer elements.
   - Input type is not validated, potentially failing with TypeError.
"""


# ==============================================================================
# 3. REFACTORED CLEAN CODE (AFTER REVIEW)
# ==============================================================================
from typing import List, Union

def process_even_multipliers(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Filters a sequence of numbers, selecting even values greater than 10,
    and returns a list with each matching value doubled.

    Parameters:
        numbers (List[Union[int, float]]): The list of numeric values to filter.

    Returns:
        List[Union[int, float]]: Doubled values of matching numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input 'numbers' must be a list of numeric types.")

    return [num * 2 for num in numbers if isinstance(num, (int, float)) and num > 10 and num % 2 == 0]


# ==============================================================================
# 4. VERIFICATION RUNNER
# ==============================================================================
if __name__ == "__main__":
    raw_dataset = [4, 10, 12, 15, 18, 21, 24]
    
    print("Testing Original Messy Function:")
    print("Output:", ProcessData(raw_dataset))
    
    print("\nTesting Refactored Function:")
    print("Output:", process_even_multipliers(raw_dataset))
    