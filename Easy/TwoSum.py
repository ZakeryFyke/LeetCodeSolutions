'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        number_dict = dict()

        for i in range(0, len(nums)):
            # (Number, Index)
            if nums[i] in number_dict:
                number_dict[nums[i]] = number_dict[nums[i]] + [i]
            else:
                number_dict[nums[i]] = [i]

        for i in range(0, len(nums)):

            complement = target - nums[i]

            if complement in number_dict:

                # If there is more than 1, return the 2nd index
                if len(number_dict[complement]) > 1:
                    j = number_dict[complement][1]
                else:
                    # Make sure it's not reusing the same number
                    if complement == nums[i]:
                        continue

                    j = number_dict[complement][0]

                break

        return [i, j]