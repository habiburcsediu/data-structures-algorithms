def compute_lps(pattern):
    """Build LPS array for KMP"""

    m = len(pattern)
    lps = [0] * m  # LPS array initialization

    i = 1  # Start from second character
    length = 0  # Length of previous longest prefix suffix

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length  # Update LPS value for current index
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # Fallback to previous LPS
            else:
                lps[i] = 0  # No prefix suffix match found
                i += 1
    return lps

def knuth_morris_pratt(text, pattern):
    """Return 1-based indices where pattern matches text"""

    n = len(text)
    m = len(pattern)
    if n < m:
        return []  # Pattern longer than text, no matches

    result = []
    lps = compute_lps(pattern)  # Preprocess pattern
    i = j = 0  # Indexes for text and pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j + 1)  # Match found (1-based)
            j = lps[j - 1]  # Continue searching for next matches
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]  # Use LPS to avoid re-checking chars
            else:
                i += 1  # Move to next char in text
    return result

# Example usage
text = "ababcabcabababd"
pattern = "ababd"
print(knuth_morris_pratt(text, pattern))
