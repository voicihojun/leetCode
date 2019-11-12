
# 88. Merge Sorted Array

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.


# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        for m in range(m, len(nums1)):
            nums1[m] = nums2[i]
            i += 1
        print(nums1.sort())


# Success
# Details 
# Runtime: 20 ms, faster than 86.38% of Python online submissions for Merge Sorted Array.
# Memory Usage: 11.9 MB, less than 5.13% of Python online submissions for Merge Sorted Array