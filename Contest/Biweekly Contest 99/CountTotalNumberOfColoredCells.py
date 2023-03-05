# 2579. Count Total Number of Colored Cells

# There exists an infinitely large two-dimensional grid of uncolored unit cells.
# You are given a positive integer n, indicating that you must do the following routine for n minutes:
# 1. At the first minute, color any arbitrary unit cell blue.
# 2. Every minute thereafter, color blue every uncolored cell that touches a blue cell.

# Return the number of colored cells at the end of n minutes.

# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution(object):
    def coloredCells(self, n):
        return 2 * n * (n - 1) + 1