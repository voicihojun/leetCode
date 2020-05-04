class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        result = [i for i in A if i % 2 == 0]
        result2 = [i for i in A if i % 2 == 1]

        result.extend(result2)

        return result

test = Solution()

print(test.sortArrayByParity([3,1,2,4])) #[2,4,3,1] or [4,2,3,1] or ...


# 905. Sort Array By Parity
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
# Input: [3, 1, 2, 4]
# Output: [2, 4, 3, 1]
# The outputs[4, 2, 3, 1], [2, 4, 1, 3], and [4, 2, 1, 3] would also be accepted.
#
# Note:
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000