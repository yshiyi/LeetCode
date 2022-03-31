'''
Merge multiple lists

Description:
Given 3/k sorted arrays, merge them into one single array without any duplicates.

Example:
lists = [[1,2,2,3], [-10,-10,0,1], [100,101,103]]
output = [-10,0,1,2,3,100,101,103]
'''

"""
Method: minHeap
        Use three pointers to sweep through the arrays.
        The values are saved in a minHeap.
        Use a set to determine if the value has saved in the output list.
        Time complexity: O(N) N is the total number of values in lists
        Space complexity: O(M) M is the total number of values in the output list.
"""
import heapq
class Solution(object):
    def mergeLists(self, lists):
        minHeap = []
        heapq.heapify(minHeap)
        for index, list in enumerate(lists):
            heapq.heappush(minHeap, (list[0], index, 0))  # val, r, c
        s = set()
        ans = []
        while len(minHeap):
            val, r, c = heapq.heappop(minHeap)
            if val not in s:
                s.add(val)
                ans.append(val)
            if c+1 < len(lists[r]):
                heapq.heappush(minHeap, (lists[r][c+1], r, c+1))
        return ans

sol = Solution()
lists = [[1,2,2,3], [-10,-10,0,1,3,5,7], [100,101,103]]
print(sol.mergeLists(lists))
