"""
1813. Sentence Similarity III

You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

For example,

    s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
    s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

 

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"

Output: false

Explanation:

No single sentence can be inserted inside one of the sentences to make it equal to the other.

Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

 

Constraints:

    1 <= sentence1.length, sentence2.length <= 100
    sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
    The words in sentence1 and sentence2 are separated by a single space.

Solutions: 
"""
from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Step 1: Split sentences into word lists
        words1 = sentence1.split()  # O(m)
        words2 = sentence2.split()  # O(n)
        
        # Ensure words1 is the shorter one (for efficiency)
        if len(words1) > len(words2):
            words1, words2 = words2, words1  # Swap to make words1 the smaller sentence
        
        # Step 2: Use two pointers for matching words
        left, right = 0, 0  # Start from beginning and end

        # Move `left` pointer while words match
        while left < len(words1) and words1[left] == words2[left]:  
            left += 1  # O(min(m, n))

        # Move `right` pointer while words match
        while right < len(words1) and words1[-(right + 1)] == words2[-(right + 1)]:  
            right += 1  # O(min(m, n))

        # Step 3: Check if we have matched all words from the shorter sentence
        return left + right >= len(words1)  # O(1)
