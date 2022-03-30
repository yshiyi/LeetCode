'''
1229M. Meeting Scheduler

Description:
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration, 
return the earliest time slot that works for both of them and is of duration.
If there is no common time slot that satisfies the requirements, return an empty array.
The format of a time slot is an array of two elements [start, end] 
representing an inclusive time range from start to end.  
It is guaranteed that no two availability slots of the same person intersect with each other. 
That is, for any two time slots [start1, end1] and [start2, end2] of the same person, 
either start1 > end2 or start2 > end1.

Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []

Constraints:
1 <= slots1.length, slots2.length <= 10^4
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 10^9
1 <= duration <= 10^6 
'''

"""
Method: Consider the following two cases:
        1. |----------------|
                 |-----------------|
        2.       |-----------------|
           |----------------|
        If the overlapped period is less than the duration, we move to the next interval.
        Otherwise, we check if the overlapped period is greater than or equal to the duration..
"""
class Solution(object):
    def meetingScheduler(self, slot1, slot2, d):
        slot1.sort()
        slot2.sort()
        i, j = 0, 0
        while i<len(slot1) and j<len(slot2):
            if slot1[i][1] < slot2[j][0]+d:
                i += 1
                continue
            if slot2[j][1] < slot1[i][0]+d:
                j += 1
                continue
            starting = max(slot1[i][0], slot2[j][0])
            ending = min(slot1[i][1], slot2[j][1])
            if starting+d<=ending:
                return [starting, starting+d]
            if slot1[i][1] < slot2[j][1]:
                i += 1
            else:
                j += 1
        return []

sol = Solution()
slot1 = [[10, 50], [60, 120], [140, 210]]
slot2 = [[0, 15], [60, 70]]
duration = 12
print(sol.meetingScheduler(slot1, slot2, duration))
