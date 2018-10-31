'''

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?

Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


class Solution:
    def threeSum(self, nums):
        results = []
        nums.sort()

        for i in range(0, len(nums) - 2):

            # Ignore duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while (left < right):
                # All up all 3
                total = nums[i] + nums[left] + nums[right]

                # Increment pointers if not == 0
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
