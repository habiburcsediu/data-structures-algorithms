"""
Problem: Convert binary string to decimal

Approach:
1. Manual Method:
   - Iterate over the binary string from right to left (least significant to most significant bit).
   - For each bit, if it's '1', add the corresponding power of 2 to a running sum.
   - Multiply the power of 2 by 2 at each step to simulate the next higher bit.

2. Built-in Method:
   - Use Python's built-in `int()` function with base 2 to directly convert a binary string to decimal.

Time Complexity:
- Manual: O(n), where n is the length of the binary string.
- Built-in: O(n), since it also processes each character once.

Space Complexity:
- O(1), constant space used (excluding input).
"""


#-------------------- Manual Implementation --------------------#

def convert_binary_to_decimal(binary_string):
    n = len(binary_string)
    summation = 0
    p2 = 1

    for i in range(n - 1, -1, -1):
        if binary_string[i] == "1":
            summation += p2
        p2 *= 2

    return summation

# Example usage
binary_string = "1101"
print(convert_binary_to_decimal(binary_string))  # Output: 13


#-------------------- Built-in Implementation --------------------#

def convert_binary_to_decimal_builtin(binary_string):
    return int(binary_string, 2)
