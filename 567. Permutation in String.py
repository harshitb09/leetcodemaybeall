"""
567. Permutation in String
Medium
Topics
Companies
Hint

Given two strings s1 and s2, return true if s2 contains a

of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

 

Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, it's impossible to find a permutation
        if len(s1) > len(s2):  
            return False  # O(1)

        # Frequency count arrays for characters in 'a' to 'z' (26 letters)
        s1_count = [0] * 26  # Stores character frequencies for s1 (O(1) space)
        s2_count = [0] * 26  # Stores character frequencies for the current window in s2 (O(1) space)

        # Initialize frequency maps for s1 and the first window in s2
        for i in range(len(s1)):  # O(k), where k = len(s1)
            s1_count[ord(s1[i]) - ord('a')] += 1  # Convert character to index and increment count
            s2_count[ord(s2[i]) - ord('a')] += 1  # Initialize first window in s2

        # Check if the initial window is a permutation of s1
        if s1_count == s2_count:  # O(26) = O(1) comparison
            return True

        # Sliding window technique: shift the window right one character at a time
        for i in range(len(s1), len(s2)):  # O(n - k), where n = len(s2), k = len(s1)
            # Include the new character into the window
            s2_count[ord(s2[i]) - ord('a')] += 1  # O(1)

            # Remove the leftmost character from the window
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1  # O(1)

            # Check if the updated window is a permutation of s1
            if s1_count == s2_count:  # O(26) = O(1) comparison
                return True

        # If no matching window found, return False
        return False  # O(1)
