"""
921. Minimum Add to Make Parentheses Valid
Medium
Topics
Companies

A parentheses string is valid if and only if:

    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1

Example 2:

Input: s = "((("
Output: 3

 

Constraints:

    1 <= s.length <= 1000
    s[i] is either '(' or ')'.



Solution:
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0  # Tracks unmatched '('
        close_count = 0  # Tracks unmatched ')'
        
        # Iterate through the string
        for char in s:  # O(n) time
            if char == '(':  
                open_count += 1  # Increment count for unmatched '('
            else:  # If char == ')'
                if open_count > 0:
                    open_count -= 1  # Match with an existing '('
                else:
                    close_count += 1  # No matching '(', so this ')' is extra
        
        # Total insertions required
        return open_count + close_count  # O(1) operation
