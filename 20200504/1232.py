class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y1-y0) * (x-x1) != (y-y1) * (x1-x0):
                return False

        return True

test = Solution()
print(test.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))  #True
print(test.checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))  #False

# comment
# if the number of list is less than 3, we don't calculate another thing. just return True.
# if not, we need to calculate the angle. it means that diff_y / diff_x.
# but diff_x is possibly 0. and it causes error message.
# y1-y0 / x1-x0 = y-y1 / x-x1 equals to :  (y1-y0) * (x-x1) = (y-y1) * (x1-x0)
# so instead of division, i used multiplication for comparison of angle.


# 1232. Check If It Is a Straight Line
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
#
# Example 1
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
#
# Example 2
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
# Constraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.