class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        m = len(nums2)
        l = SortedList()
        count = 0

        for i in range(n):
            for j in range(m)
                current = nums1[i] - nums1[j]
                current_diff = nums2[i] - nums2[j] + diff
                if current <= current_diff
                    count += 1
        return count