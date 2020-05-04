
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) == 1):
            return True

        for i in range(len(nums)):
            temp = nums[i]
            del nums[i]
            print(nums)

            # is_sorted = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

            # print("nums : ", nums)
            # print("nums.sort : ", sorted(nums))
            is_sorted = (nums == sorted(nums))

            if (is_sorted):
                return True

            nums.insert(i, temp)

        return False


test = Solution()
print(test.checkPossibility([3,4,2,3])) #False
print(test.checkPossibility([1])) #True
print(test.checkPossibility([1,2,4,5,3])) #True

# MY COMMENT
# this code passed all the tests except the last one which have huge amount of element.
# for passing the last one, i need to use another access way to solve this problem.

# 665. Non-decreasing Array
# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
#
# Example 1:
# Input: nums = [4, 2, 3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non - decreasing array.
#
# Example 2:
# Input: nums = [4, 2, 1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.
