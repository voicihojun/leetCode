class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result += nums[i]

        return result

test = Solution()
test.arrayPairSum([1,4,3,2]) #4

# to minimize the result, we need to sort the array at first.
# and then add all the even index of this array.

# 561. Array Partition I
#
# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
# Input: [1,4,3,2]
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
#
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].