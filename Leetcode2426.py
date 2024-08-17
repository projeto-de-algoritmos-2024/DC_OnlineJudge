from sortedcontainers import SortedList

class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        nums_diff = [nums1[i] - nums2[i] for i in range(n)]
        return self.CountPairs(nums_diff, 0, n - 1, diff)
    
    def CountPairs(self, nums, left, right, diff):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = self.CountPairs(nums, left, mid, diff) + self.CountPairs(nums, mid + 1, right, diff)
        
        j = mid + 1
        sorted_list = SortedList()
        
        # Count pairs using the SortedList
        for i in range(mid, left - 1, -1):
            while j <= right and nums[j] <= nums[i] + diff:
                sorted_list.add(nums[j])
                j += 1
            count += len(sorted_list) - sorted_list.bisect_right(nums[i] + diff)
        
        # Merge the two halves
        nums[left:right + 1] = sorted(nums[left:right + 1])
        return count
