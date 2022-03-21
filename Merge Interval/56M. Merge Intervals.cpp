/*
56M. Merge Intervals
Description:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
 
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Similar Questions:
Insert Interval - Medium
Meeting Rooms - Easy
Meeting Rooms II - Medium
Teemo Attacking - Easy
Add Bold Tag in String - Medium
Range Module - Hard
Employee Free Time - Hard
Partition Labels - Medium
Interval List Intersections - Medium
*/

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Create vector to hold the outputs
        vector<vector<int>> res;
        // Sort the intervals w.r.t the first column
        sort(intervals.begin(), intervals.end());
        // Push the first interval into the res
        res.push_back(intervals[0]);
        
        // Traverse the interval from the second elment
        for(int i=1; i<intervals.size(); ++i){
            // Compare the end time of the last element in res
            // to the start time of intervals[i]
            if(res.back()[1] < intervals[i][0]){
                res.push_back(intervals[i]);
            }else{
                // Update the end time of the last element in res
                res.back()[1] = max(res.back()[1], intervals[i][1]);
            }
        }
        
        return res;
    }
};
