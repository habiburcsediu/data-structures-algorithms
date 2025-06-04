def rabin_karp_string_matching(text, pattern, prime=101):
    """Return a list of indices where a pattern is found in the text using Rabin-Karp string matching algorithm"""

    n = len(text)
    m = len(pattern)

    if m > n:
        return []

    base = 256  # Number of possible characters (ASCII alphabet size)
    result = []

    # Precompute h = base^(m-1) % prime
    h = pow(base, m - 1, prime)

    pattern_hash = 0
    text_hash = 0

    # Compute initial hash values for the first window of the text and the pattern
    for i in range(m):
        text_hash = (base * text_hash + ord(text[i])) % prime
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime

    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        # Check if the current window's hash matches the pattern's hash
        if text_hash == pattern_hash:
            # If hashes match, verify by comparing the actual substring
            if text[i:i + m] == pattern:
                result.append(i)

        # Rolling hash: update hash for next window by removing the leading char and adding the new trailing char
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Make sure hash is positive
            if text_hash < 0:
                text_hash += prime

    return result

print(rabin_karp_string_matching("ababcabcabababd", "ababd"))