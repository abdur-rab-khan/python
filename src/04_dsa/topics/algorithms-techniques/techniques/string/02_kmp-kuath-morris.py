"""
    <====================> Kuth Morris Pratt (KMP) Algorithm <====================>

    ◉ KMP Algorithm is used to find "pattern" in a "text". It compares character by character from
        "left" to "right", but it avoid to re-checking characters after miss-match.
    ◉ Whenever miss-match happen after some matches, we already know part of the pattern has matched
        earlier. So KMP algorithm use that information through pre-processed LPS (Longest Prefix
        Suffix) array, to shift pattern efficiently, without restarting from the next character in
        the text.
    ◉ That reduce the time complexity from o(n * m) to o(m + n), where "n" is the length of "txt"
        and "m" in length of pattern.

    <====================> How to use LPS Table <====================>

    ◉ So LPS (Longest Prefix and Suffix) is a "Longest Prefix" which is also a "suffix".
    ◉ Let's Generate LPS (Longest Prefix and Suffix):

    ◉ ====================> Example 1 <=====================

    ptr = "ababc"
    lps = [0, 0, 0, 0]
    i = 1;
    length = 0;

    ◉ Step 1: lsp[0] is always 0.
                ◈ A single character has no prefix and suffix.
                lps = [0, ?, ?, ?]

    ◉ Step 2: i = 1 ('b')
                ◈ Compair ptr[i] == ptr[length], a == b;
                ◈ They don't match. length is already = 0, we can't go back otherwise we will.
                ◈ lps[i] = lps[1] = 0;
                ◈ Pattern: a "b" a b c
                ◈ Substring: "ab"
                ◈ Prefixes: "a"
                ◈ Suffixes: "b"
                ◈ Result: No match. Length is 0.
                ◈ LPS: [0, 0, ?, ?, ?]

    ◉ Step 3: i = 2 ('a')
                ◈ Compair ptr[i] == ptr[length], a == a;
                ◈ They match!
                ◈ Increase length by "1", Set lps[i] to length;
                ◈ Pattern: a b "a" b c
                ◈ Substring: "aba"
                ◈ Prefixes: "a", "ab"
                ◈ Suffixes: "a", "ba"
                ◈ Result:  The longest match is "a" (length 1).
                ◈ LPS: [0, 0, 1, 2, ?]

    ◉ Step 4: i = 3 ('b')
                ◈ Compair ptr[i] == ptr[length], b == b;
                ◈ They match!
                ◈ Increase length to "2", Set lps[i] to length, lps[3] becomes 2;
                ◈ Pattern: a b a "b" c
                ◈ Substring: "abab"
                ◈ Prefixes: "a", "ab", "aba"
                ◈ Suffixes: "a", "ab", "bab"
                ◈ Result:  The longest match is "a" (length 1).
                ◈ LPS: [0, 0, 1, 2, ?]

    ◉ Step 5: i = 4 ('c')
                ◈ Compair ptr[i] == ptr[length], c == b;
                ◈ They don't match. length is already = 0, we can't go back otherwise we will.
                ◈ At there instead of making lps[4] = 0, We need to check if a shorter prefix might
                    match. We "fall back" by setting length = lps[length - 1];
                ◈ Pattern: a b a b "c"
                ◈ Substring: "abab"
                ◈ Prefixes: "a", "ab", "aba"
                ◈ Suffixes: "a", "ab", "bab"
                ◈ Result:  The longest match is "a" (length 1).
                ◈ LPS: [0, 0, 1, 2, 0]

    ◉ ====================> Example 2 <=====================

    ptr = "abaac"
    lps = [?, ?, ?, ?]
    i = 1;
    length = 0;

    ◉ Step 1: lsp[0] is always 0.
                ◈ A single character has no prefix and suffix.
                lps = [0, ?, ?, ?]

    ◉ Step 2: i = 1 ('b')
                ◈ Compair ptr[i] == ptr[length], a == b;
                ◈ They don't match. length is already = 0, we can't go back otherwise we will.
                ◈ lps[i] = lps[1] = 0;
                ◈ Pattern: a "b" a a c
                ◈ Substring: "ab"
                ◈ Prefixes: "a"
                ◈ Suffixes: "b"
                ◈ Result: No match. Length is 0.
                ◈ LPS: [0, 0, ?, ?, ?]

    ◉ Step 3: i = 2 ('a')
                ◈ Compair ptr[i] == ptr[length], a == a;
                ◈ They match!
                ◈ Increase length by "1", Set lps[i] to length;
                ◈ Pattern: a b "a" a c
                ◈ Substring: "aba"
                ◈ Prefixes: "a", "ab"
                ◈ Suffixes: "a", "ba"
                ◈ Result:  The longest match is "a" (length 1).
                ◈ LPS: [0, 0, 1, 2, ?]

    ◉ Step 4: i = 3 ('a')
                ◈ Compair ptr[i] == ptr[length], a == b;
                ◈ They don't match. We crucial fallback step, to see whether in prev any
                    prefix/suffix is there. length = lps[length - 1] = 0
                ◈ length = lps[length - 1] = 0;
                ◈ Pattern: a b a "a" c
                ◈ Substring: "abab"
                ◈ Prefixes: "a", "ab", "aba"
                ◈ Suffixes: "a", "ab", "bab"
                ◈ Result:  The longest match is "a" (length 1).
                ◈ LPS: [0, 0, 1, 1, ?]

    ◉ Step 5: i = 4 ('c')
                ◈ Compair ptr[i] == ptr[length], c == b;
                ◈ They don't match. length is already = 0, we can't go back otherwise we will.
                ◈ At there instead of making lps[4] = 0, We need to check if a shorter prefix might
                    match. We "fall back" by setting length = lps[length - 1];
                ◈ Pattern: a b a a "c"
                ◈ Substring: "abab"
                ◈ Prefixes: "a", "ab", "aba", "abaa"
                ◈ Suffixes: "c", "ac", "aac", "baac"
                ◈ Result:  The longest match is "a" (length 1).
                ◈ LPS: [0, 0, 1, 1, 0]

"""

# LPS[0] will always 0

# Constructing LPS

# Let's constructLPS

# Let's perform searching

def build_lps(pattern):
    lps = [0] * len(pattern)
    length, i = 0, 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            i += 1
    return lps

def kmp_search(text, pattern):
    if not pattern:
        return 0
    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        elif j:
            j = lps[j - 1]
        else:
            i += 1
    return -1
