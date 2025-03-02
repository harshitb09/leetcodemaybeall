"""
2491. Divide Players Into Teams of Equal Skill
Medium
Topics
Companies
Hint

You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

Example 2:

Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.

Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.

 

Constraints:

    2 <= skill.length <= 105
    skill.length is even.
    1 <= skill[i] <= 1000

Solution:
"""
from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array (O(n log n))
        skill.sort()  

        # Step 2: Initialize two pointers
        left, right = 0, len(skill) - 1  # O(1) space
        target = skill[left] + skill[right]  # Expected sum of each team (O(1))
        total_chemistry = 0  # Variable to store the sum of chemistry (O(1))

        # Step 3: Use two-pointer approach to form teams (O(n))
        while left < right:
            # If the current pair doesn't match the expected sum, return -1
            if skill[left] + skill[right] != target:
                return -1  # O(1)

            # Calculate chemistry and accumulate the result
            total_chemistry += skill[left] * skill[right]  # O(1)

            # Move the pointers inward
            left += 1  # O(1)
            right -= 1  # O(1)

        # Step 4: Return the total chemistry sum (O(1))
        return total_chemistry
