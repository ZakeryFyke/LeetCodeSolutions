'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
'''

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        points = [p1] + [p2] + [p3] + [p4]

        point_set = [list(x) for x in set(tuple(x) for x in points)]

        if len(point_set) < 4:
            return False

        distances = []

        for i in range(0, len(points)):
            first_point = points[i]

            for j in range(i + 1, len(points)):
                second_point = points[j]

                distance = self.get_distance(first_point, second_point)

                distances.append(distance)

        # For this to be a square, there must be 4 matching lengths
        start = len(distances)
        set_len = len(set(list(distances)))

        if start - set_len >= 4:
            return True

        return False

    def get_distance(self, first, second):
        distance = ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** (1 / 2)
        return distance