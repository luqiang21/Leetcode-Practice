"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Assume that the total area is never beyond the maximum possible value of int.


"""
from tools import timing

class Solution:
    @timing
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C-A) * (D-B)
        area2 = (H-F) * (G-E)
        highest_start_x = max(A, E)
        highest_start_y = max(B, F)
        lowest_end_x = min(C, G)
        lowest_end_y = min(D, H)

        if highest_start_x >= lowest_end_x or highest_start_y >= lowest_end_y:
            return area1 + area2

        return area1 + area2 - (lowest_end_x - highest_start_x) * (lowest_end_y - highest_start_y)

A, B, C, D, E, F, G, H = -3, 0, 3, 4, 0, -1, 9, 2
assert Solution().computeArea(A, B, C, D, E, F, G, H) == 45
