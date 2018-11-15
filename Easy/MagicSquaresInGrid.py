'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
'''


class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row = 0
        count = 0

        while row < len(grid) - 2:
            col = 0

            while col < len(grid[0]) - 2:

                square = self.get_square(row, col, grid)
                col += 1

                if self.is_magic(square):
                    count += 1

            row += 1

        return count

    def is_magic(self, square):

        target_sum = sum(square[0])
        for row in square:
            if sum(row) != target_sum:
                return False

            if any(x > 9 or x < 1 for x in row):
                return False

        # Transpose list to check columns
        t_list = list(map(list, zip(*square)))

        print(t_list)

        for row in t_list:
            if sum(row) != target_sum:
                return False

        # Check diagnols <- is that how you spell that? probably not
        if sum([square[0][0], square[1][1], square[2][2]]) != target_sum:
            return False
        if sum([square[2][0], square[1][1], square[0][2]]) != target_sum:
            return False

        return True

    def get_square(self, row, column, grid):

        row_1 = grid[row][column:column + 3]
        row_2 = grid[row + 1][column:column + 3]
        row_3 = grid[row + 2][column:column + 3]

        return [row_1, row_2, row_3]

