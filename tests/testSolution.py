import sys
import os

# Add the parent directory to the sys path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the solution module
from arrays.twoNumberSum.algoexpertFinalSubmissions.solution1 import twoNumberSum



def test_case_name():
    # Input values for the test case
    input_values = [1, 2, 3, 4, 5]
    target_sum = 7

    # Expected output for the test case
    expected_output = [2, 5]  # For example, the algorithm should return [2, 5] for the given input

    # Call the function from solution1.py with the input values
    actual_output = twoNumberSum(input_values, target_sum)  # Replace `solution_function` with the actual function name

    # Compare the actual output with the expected output
    assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"

