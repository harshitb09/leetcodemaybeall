"""
962. Maximum Width Ramp
Solved
Medium
Topics
Companies

A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.

 

Constraints:

    2 <= nums.length <= 5 * 104
    0 <= nums[i] <= 5 * 104


Solution:
"""
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []  # Monotonic decreasing stack (stores indices)
        max_width = 0  # Stores the maximum ramp width
        
        # Step 1: Build decreasing monotonic stack (O(n))
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)  # Push index if it's a new potential start
        
        # Step 2: Find maximum width using two-pointer approach (O(n))
        for j in range(len(nums) - 1, -1, -1):  # Iterate from right to left
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())  # Update max width
        
        return max_width  # Return maximum found ramp width
