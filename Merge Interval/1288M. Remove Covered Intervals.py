"""
1288M. Remove Covered Intervals.py

Description:
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), 
remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
Return the number of remaining intervals.

 
Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:
Input: intervals = [[1,4],[2,3]]
Output: 1
 

Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 105
All the given intervals are unique.
"""

"""
Method: There are two cases that we need to consider:
        1. |-------------|
              |--------|
        2. |-------------|
           |-----------------|
"""
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        ref = intervals[0]
        ans = 0
        for i in range(1, len(intervals)):
            if ref[0]<=intervals[i][0] and ref[1]>=intervals[i][1]:
                ans += 1
            elif ref[0]==intervals[i][0] and ref[1]<=intervals[i][1]:
                ans += 1
                ref = intervals[i]
            else:
                ref = intervals[i]
        return len(intervals) - ans

