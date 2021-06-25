/*
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
*/

/*
Method: The basic idea is to use a priority queue to save the end time of each meeting.
        The top element in the priority queue is the smallest value. It means the first end meeting.
        If the start time of the new meeting is greater than or equal to the top value in the priority queue,
        in other words, the top meeting has ended before the new meeting, 
        then we can pop the top meeting.
        Eventually, the size of the priority queue is the total number of meeting rooms we need.
*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution{
private:
    struct cmp{
        bool operator()(int &i1, int &i2){
            return i1 > i2;
        }
    };
public:
    int minMeetingRoom(vector<vector<int>>& intervals){
        // If the number of meetings is less than 2, return intervals.size()
        if(intervals.size()<2){
            return intervals.size();
        }

        // Sort intervals by the start time
        sort(intervals.begin(), intervals.end());

        // Create a priority queue to hold the end time of each meeting
        priority_queue<int, vector<int>, cmp> q;
        q.push(intervals[0][1]);

        // Iterate over remaining intervals
        for(int i=1; i<intervals.size(); ++i){
            if(q.top()<=intervals[i][0]){
                // We only pop out the top one when the new meeting starts after the top meeting.
                // It means we don't need to open a new meeting room
                q.pop();
            }
            // We need to push all the meetings into the queue
            q.push(intervals[i][1]);
        }
        return q.size();
    }
};

int main(){
    vector<vector<int>> intervals1{{8, 12}, {10, 20}, {11, 30}, {1, 10}, {2, 7}, {3, 19}},
    intervals2{{0, 30}, {5, 10}, {15, 20}};

    Solution *obj = new Solution();
    cout << obj->minMeetingRoom(intervals1) << endl;
    cout << obj->minMeetingRoom(intervals2) << endl;

    delete obj;
}
