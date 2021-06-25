/*
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
*/

/*
 * Method:
 * Similar to 56M. Merge Intervals
 * The approach to this question is to check if there is any overlapping between each vector.
 *
 * */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution{
public:
    bool checkMeetingTime(vector<vector<int>> &intervals){
        if(intervals.size()<2){return true;}
        // Sort the intervals w.r.t. the first column first
        sort(intervals.begin(), intervals.end());
        // Traverse the intervals from the second element
        for(int i=1; i<intervals.size(); ++i){
            if(intervals[i-1][1] > intervals[i][0]){
                return false;
            }
        }
        return true;
    }
};

int main(){
    vector<vector<int>> intervals1{{0,30},{5,10},{15,20}}, intervals2{{7, 10}, {2, 4}};
    Solution *obj = new Solution();

    cout << obj->checkMeetingTime(intervals1) << endl;
    cout << obj->checkMeetingTime(intervals2) << endl;
}


