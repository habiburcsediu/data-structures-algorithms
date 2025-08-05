"""
Problem: Convert decimal to binary
Approach:
- We repeatedly divide the number `n` by 2, keeping track of the remainders.
- The remainder of each division (either 0 or 1) is a bit in the binary representation.
- We append these remainders (in reverse order) to form the binary string.
- We continue dividing `n` by 2 until `n` becomes 0.
Time Complexity: O(log n)
  - At each step, we divide `n` by 2, so the number of steps is proportional to the logarithm of `n`.
Space Complexity: O(log n)
  - The space complexity is proportional to the number of bits required to represent the binary number (which is O(log n)).
"""

def convert_decimal_to_binary(n):
    if n == 0:
        return "0"

    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2

    return "".join(reversed(bits))

# Example usage
n = 13
print(convert_decimal_to_binary(n))


#-------------------- Using Python's Built-in bin() --------------------#

def convert_decimal_to_binary(n):
    return bin(n)[2:]