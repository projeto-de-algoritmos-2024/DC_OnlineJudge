from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        transformed = [nums1[i] - nums2[i] for i in range(n)]
        sorted_list = SortedList()
        count = 0
        
        def custom_bisect_right(sorted_list, value):
            low, high = 0, len(sorted_list)
            while low < high:
                mid = (low + high) // 2
                if sorted_list[mid] <= value:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        for value in transformed:
            # Count number of elements in sorted_list that are <= value + diff
            count += custom_bisect_right(sorted_list, value + diff)
            # Add the current value to the sorted list
            sorted_list.add(value)
        
        return count