import sys


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) < 3:
            return 0

        closest_sum = sys.maxsize
        nums.sort()
        print(nums)
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while (j < k):

                total = nums[i] + nums[j] + nums[k]
                distance = abs(target - total)

                if distance < (abs(target - closest_sum)):
                    closest_sum = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                elif total == target:
                    return total

        return closest_sum