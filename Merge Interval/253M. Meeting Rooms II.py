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

'''
Method: We can't use the merge interval method.
        For instance, [[0, 8],[5, 10],[9, 20]].
        If we try to merge the above intervals, we will have three distinct intervals in the end.
        The correct result, however, should be 2.

        Therefore, we need to use the priority queue to solve this question.
        We sort the intervals according to the starting time first.
        Use a priority queue to save the ending time.
        If the starting time of the new meeting is greater than or equal to the top of the queue, 
        we don't need to open a new meeting room. 
        We can just pop the top of the queue and push the new ending time.
        On the contrary, we need to open a new meeting room and just push the new ending time.
'''
# Merge the overlapped intervals and return the number of intervals left
import heapq
class Solution(object):
    def meetingRooms(self, intervals):
        if len(intervals)<2:
            return len(intervals)
        intervals.sort()
        meeting_rooms = []
        heapq.heapify(meeting_rooms)
        heapq.heappush(meeting_rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if meeting_rooms[0]<=intervals[i][0]:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, intervals[i][1])
        return len(meeting_rooms)

sol = Solution()
inter1 = [[0, 8],[5, 10],[9, 20]]
inter2 = [[7,10],[2,4]]
inter3 = [[1,3],[2,6],[8,10],[15,18]]
inter4 = [[0, 30],[5, 10],[15, 20]]
inter5 = [[8,12],[10,20],[11,30],[1,10],[2,7],[3,19]]
print(sol.meetingRooms(inter1))  # 2
print(sol.meetingRooms(inter2))  # 1
print(sol.meetingRooms(inter3))  # 2
print(sol.meetingRooms(inter4))  # 2
print(sol.meetingRooms(inter5))  # 4
