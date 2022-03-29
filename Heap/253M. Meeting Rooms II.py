'''
253M. Meeting Rooms II

Description:
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.
Example 1:
Input: 
[[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:
Input: [[7,10],[2,4]]
Output: 1
Similar Questions:
Merge Intervals - Medium
Meeting Rooms - Easy
Minimum Number of Arrows to Burst Balloons - Medium
Car Pooling - Medium
'''

# Solution:
import heapq

class Solution:
    def minMeetingRoom(self, intervals):
        if len(intervals) < 2:
            return 1
        intervals.sort()
        q = []
        heapq.heapify(q)
        heapq.heappush(q, intervals[0][1])
        for interval in intervals:
            if q[0] <= interval[0]:
                heapq.heappop(q)
            heapq.heappush(q, interval[1])
        return len(q)

sol = Solution()
intervals = [[8,12],[10,20],[11,30],[1,10],[2,7],[3,19]]
print(sol.minMeetingRoom(intervals))  # 4
