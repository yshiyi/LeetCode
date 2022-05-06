"""
986. Interval List Intersections

Description:
You are given two lists of closed intervals, firstList and secondList, 
where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or 
represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 
Constraints
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1
"""

"""
Method: Merge intervals
        Merge two lists, and sort the new list.
        Note, the tricky part is how to determine the value of ref.
        |----------|
              |-----------|
        This is the standard case. The start of the overlap interval is max(list[i-1][0], list[i][0]), end of it is min(ref, list[i][1]).
        The new ref is list[i][1]. ref = max(ref, list[i][1]). NOT!!!! ref = list[i][1]
        Consider this case
        |---------------------------------------|
          |----------| |------------|
        In this case, ref = max(ref, list[i][1])
        
"""
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        newList = firstList + secondList
        newList.sort()
        ref = newList[0][1]
        ans = []
        for i in range(1, len(newList)):
            if newList[i][0]<=ref:
                ans.append([max(newList[i-1][0], newList[i][0]), min(ref, newList[i][1])])
            ref = max(ref, newList[i][1])
        return ans
