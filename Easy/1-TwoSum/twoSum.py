from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      indices = {}
      # for each item, save the index in a hashtable
      for i, num in enumerate(nums):
          indices[num] = i
      for i, num in enumerate(nums):
          # get the complement
          complement = target - num;
          # if it exists in array and is not the same element
          if complement in indices and indices[complement] != i:
              return [i, indices[complement]]
