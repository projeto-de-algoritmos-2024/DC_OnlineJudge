from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        max_val = max(instructions)
        tree = [0] * (2 * max_val + 2)
        mod = 10**9 + 7
        
        def update(index, value):
            while index < len(tree):
                tree[index] += value
                index += index & -index
        
        def query(index):
            total = 0
            while index > 0:
                total += tree[index]
                index -= index & -index
            return total
        
        cost = 0
        for i, num in enumerate(instructions):
            left_cost = query(num - 1)
            right_cost = i - query(num)
            cost += min(left_cost, right_cost)
            update(num, 1)
        
        return cost % mod