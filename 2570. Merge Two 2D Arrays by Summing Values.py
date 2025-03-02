from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Create an array to store the sum of values for IDs (1 to 1000)
        values = [0] * 1001  # Index represents ID, value represents sum
        
        # Boolean array to track which IDs are present in either nums1 or nums2
        present = [False] * 1001  # Index represents ID, True means ID exists in at least one array

        # Process nums1: Add values and mark IDs as present
        for id_, val in nums1:
            values[id_] += val  # Add the value to the corresponding ID index
            present[id_] = True  # Mark this ID as present

        # Process nums2: Add values and mark IDs as present
        for id_, val in nums2:
            values[id_] += val  # Add the value to the corresponding ID index
            present[id_] = True  # Mark this ID as present

        # Construct the result array by iterating over all possible IDs (1 to 1000)
        return [[id_, values[id_]] for id_ in range(1001) if present[id_]]  # Include only IDs that exist
