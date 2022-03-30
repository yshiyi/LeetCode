'''
759H. Employee Free Time

Description:
We are given a list schedule of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
Return the list of finite intervals representing common, positive-length free time for all employees, 
also in sorted order.
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. 
For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  
Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

Constraints:
1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8

Hints
Take all the intervals and do an "events" (or "line sweep") approach - an event of (x, OPEN) 
increases the number of active intervals, while (x, CLOSE) decreases it. 
Processing in sorted order from left to right, if the number of active intervals is zero, 
then you crossed a region of common free time.

Similar Questions:
Merge Intervals - Medium
Interval List Intersections - Medium
'''

"""
Method: Determine if there is an unoverlapped period.
        Put all intervals into one single list.
        Sweep through the whole list and put all the gaps into ans.
        Set the ending time of the first interval as a ref, and compare to the next starting time.
        If overlapped, check if we need to update ref (update if ref < interval[1]).
"""
class Solution(object):
    def employeeFreeTime(self, schedules):
        intervals = []
        for schedule in schedules:
            intervals += schedule
        intervals.sort()
        ref = intervals[0][1]
        ans = []
        for interval in intervals:
            if ref < interval[0]:
                ans.append([ref, interval[0]])
                ref = interval[1]
            else:
                ref = max(ref, interval[1])
        return ans

sol = Solution()
schedules = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
print(sol.employeeFreeTime(schedules))
