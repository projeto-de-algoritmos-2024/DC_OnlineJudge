from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            left_sum = helper(left, mid)
            right_sum = helper(mid + 1, right)
            
            left_max, right_max = float('-inf'), float('-inf')
            temp_sum = 0

            for i in range(mid, left - 1, -1):
                temp_sum += nums[i]
                left_max = max(left_max, temp_sum)

            temp_sum = 0
            for i in range(mid + 1, right + 1):
                temp_sum += nums[i]
                right_max = max(right_max, temp_sum)

            cross_sum = left_max + right_max

            return max(left_sum, right_sum, cross_sum)

        return helper(0, len(nums) - 1)