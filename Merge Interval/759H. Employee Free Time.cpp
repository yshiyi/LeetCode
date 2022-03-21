/*
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
*/

/*
Method: Similar to 56M. Merge Intervals
        We first put all the intervals into a vector, and sort the vector by the start time.
        Then we select the first interval as a reference and iterate over the entire intervals.
        If there is a gap between the end time of the reference interval and the start time of interval[i],
        then it means there is a shared free time, and we need to add this gap into the res.
        If there is not a gap (ref[1]>=interval[i].start), we need to check if we should update the reference.
        Now we need to compare the end time of these two intervals.
        If the end time of the ref is greater than or equal to that of interval[i], then we don't need to update ref.
        Otherwise, we need to replace ref with interval[i].
*/
// Definition for an Interval.
class Interval {
public:
    int start;
    int end;

    Interval() {}

    Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};

class Solution {
private:
    struct cmp{
        bool operator()(Interval &a, Interval &b){
            return a.start < b.start;
        }
    };
public:
    vector<Interval> employeeFreeTime(vector<vector<Interval>>& schedule) {
        vector<Interval> res, v;
        for (auto a : schedule) {
            v.insert(v.end(), a.begin(), a.end());
        }
        sort(v.begin(), v.end(), cmp());
        Interval t = v[0];
        for (Interval i : v) {
            if (t.end < i.start) {
                res.push_back(Interval(t.end, i.start));
                t = i;
            } else {
                t = (t.end < i.end) ? i : t;
            }
        }
        return res;
    }
};
