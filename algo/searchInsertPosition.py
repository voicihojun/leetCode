# 35. Search Insert Position

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if(nums[i] == target):
                return nums.index(nums[i])
            elif(nums[i] > target):
                if(i == 0):
                    return i
                elif(nums[i-1 < target]):
                    return i
            
        return len(nums)

# Success Details 
# Runtime: 40 ms, faster than 31.35% of Python online submissions for Search Insert Position.
# Memory Usage: 12.2 MB, less than 70.18% of Python online submissions for Search Insert Position.        