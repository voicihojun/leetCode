class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        from collections import Counter

        A_dict = Counter(A)

        for a in set(A):
            if A_dict[a] > 1:
                return a


test = Solution()
print(test.repeatedNTimes([1,2,3,3])) #3
print(test.repeatedNTimes([5,1,5,2,5,3,5,4])) #5

# my comment
# I learned Counter and dict for the previous problem. and I used to solve it.


# 961. N-Repeated Element in Size 2N Array
# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
# Return the element repeated N times.
#
# Example 1:
# Input: [1, 2, 3, 3]
# Output: 3
#
# Example 2:
# Input: [2, 1, 2, 5, 3, 2]
# Output: 2
#
# Example 3:
# Input: [5, 1, 5, 2, 5, 3, 5, 4]
# Output: 5
#
# Note:
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length is even
