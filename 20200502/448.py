class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        set_nums = set(nums)
        every_number = {i for i in range(1, len(nums) + 1)}
        result = list(every_number - set_nums)

        return result

test = Solution()
print(test.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  #[5,6]
print(test.findDisappearedNumbers([]))  #[]

# by using a for loop, there exists time limit exceeded. it means, for lots of data, that it's not good way to handle it.
# by using a set character, i can handle this problem. I learned one thing. ^^


# 448. Find All Numbers Disappeared in an Array
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [5,6]
