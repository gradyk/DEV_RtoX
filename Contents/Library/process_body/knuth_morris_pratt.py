#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# Python program for KMP Algorithm
# https://www.geeksforgeeks.org/python-program-for-kmp-algorithm-for-pattern-searching-2/
# This code was contributed by Bhavya Jain


def kmp_search(pattern, text):
    m_length = len(pattern)
    n_length = len(text)

    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * m_length
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    compute_lps_array(pattern=pattern, m_length=m_length, lps=lps)

    i = 0  # index for txt[]
    while i < n_length:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m_length:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < n_length and pattern[j] != text[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def compute_lps_array(pattern, m_length, lps):
    length = 0  # length of the previous longest prefix suffix

    lps[0] = 0  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < m_length:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if length != 0:
                length = lps[length - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


if __name__ == '__main__':
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    kmp_search(pattern=pat, text=txt)
