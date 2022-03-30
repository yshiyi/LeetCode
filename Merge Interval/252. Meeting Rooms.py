'''
252. Meeting Rooms

Description:
Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

Similar Questions
Merge Intervals - Medium
Meeting Rooms II - Medium
'''

'''
Method: Similar to Merge Intervals
        Determine if there is an overlap.
        Time complexity: O(NlogN) due to the sort
'''
class Solution(object):
    def meetingRooms(self, intervals):
        if len(intervals)<2:
            return True
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True

sol = Solution()
intervals = [[0,30],[5,10],[15,20]]  # Fale
intervals2 = [[7,10], [2,4]]  # True
print(sol.meetingRooms(intervals2))
