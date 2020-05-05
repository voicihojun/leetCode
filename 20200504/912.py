class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # easy way to sort by python functions
        # nums = sorted(nums)
        # return nums

        #selection sort (n^2)
        # for i in range(len(nums)):
        #     min = nums[i]
        #     min_index = i
        #     for j in range(i, len(nums)):
        #         if nums[j] < min:
        #             min = nums[j]
        #             min_index = j
        #     nums[i], nums[min_index] = nums[min_index], nums[i]
        # return nums
        # because of time limit, this sort is not passable for the test.

        #quick sort  (nlogn)
        if(len(nums) <= 1):
            return nums

        pivot = nums[len(nums) // 2]
        less_arr, equal_arr, bigger_arr = [],[],[]

        for i in nums:
            if i < pivot:
                less_arr.append(i)
            elif i == pivot:
                equal_arr.append(i)
            else:
                bigger_arr.append(i)
        return self.sortArray(less_arr) + equal_arr + self.sortArray(bigger_arr)






test = Solution()
print(test.sortArray([5,1,1,2,0,0]))  #[0,0,1,1,2,5]
print(test.sortArray([5,2,3,1]))  #[1,2,3,5]


#
# 912. Sort an Array
# Given an array of integers nums, sort the array in ascending order.
#
# Example 1:
# Input: nums = [5, 2, 3, 1]
# Output: [1, 2, 3, 5]
#
# Example 2:
# Input: nums = [5, 1, 1, 2, 0, 0]
# Output: [0, 0, 1, 1, 2, 5]
#
# Constraints:
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000


