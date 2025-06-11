def brute_force_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)

    # Slide the pattern over the text one by one until (n - m + 1)
    for i in range(n - m + 1):
        is_match = True # Assume, it's a match unless proven otherwise

        for j in range(m):
            # Compare each character of the pattern with the corresponding character in the current window of the text
            if pattern[j] != text[i + j]:
                is_match = False
                break
        # If all characters matched, return starting index
        if is_match:
            return i

    # If no match was found
    return -1

print(brute_force_string_matching("abcde", "cd"))   # Output: 2
print(brute_force_string_matching("abcde", "fg"))   # Output: -1

