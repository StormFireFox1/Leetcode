from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lower_lefts = [-1] + [0] * (len(heights) - 1)
        lower_rights = [0] * (len(heights) - 1) + [len(heights)]

        for i in range(1, len(heights)):
            minNeighbor = i - 1

            while minNeighbor >= 0 and heights[minNeighbor] >= heights[i]:
                minNeighbor = lower_lefts[minNeighbor]
            lower_lefts[i] = minNeighbor

        for i in range(len(heights) - 2, -1, -1):
            minNeighbor = i + 1
            while minNeighbor < len(heights) and heights[minNeighbor] >= heights[i]:
                minNeighbor = lower_rights[minNeighbor]
            lower_rights[i] = minNeighbor

        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i] * (lower_rights[i] - lower_lefts[i] - 1))
        return maxArea
