from sortedcontainers import SortedList

class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        numsDiff = [nums1[i] - nums2[i] for i in range(n)]
        return self.CountPairs(numsDiff, 0, n - 1, diff)
    
    def CountPairs(self, nums, left, right, diff):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = self.CountPairs(nums, left, mid, diff) + self.CountPairs(nums, mid + 1, right, diff)
        
        j = mid + 1
        l = SortedList()
        
        for i in range(mid, left - 1, -1):
            while j <= right and nums[j] <= nums[i] + diff:
                l.add(nums[j])
                j += 1
            count += len(l) - l.bisect_right(nums[i] + diff)
        
        nums[left:right + 1] = sorted(nums[left:right + 1])
        return count
