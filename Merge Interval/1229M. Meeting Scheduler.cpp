/*
1229M. Meeting Scheduler
Description:
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration, 
return the earliest time slot that works for both of them and is of duration duration.
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
*/

/*
Method: As the questions requires the earliest possible time slot, we should sort the two slots first by the start time.
        Using two pointers to iterate over two slots.
        We first compare the start time from slot1 plus the duration to the end time from slot2.
          If the former one is larger, (it means the the slot from slot2 end too early, we should next one)
          then we should move to the next slot in slot2.
        If the start time from slot2 plus the duration is greater then the end time from slot1,
          we should move to the next slot in slot1.
        
        We then determine the overlapped duration by obtaining the max of start time and the min of end time.
        If this duration is equal to or greater than the desired duration, we return this time slot.
        
        Otherwise, we need to compare the end time of two slots.
        Move the one which ends earlier (i.e., smaller).
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    vector<int> meetingScheduler(vector<vector<int>> &s1, vector<vector<int>>& s2, int d){
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());

        int i=0, j=0;
        while(i<s1.size() && j<s2.size()){
            vector<int> v1 = s1[i], v2 = s2[j];
            if(v1[1]<v2[0]+d){++i; continue;}
            if(v2[1]<v1[0]+d){++j; continue;}

            int left = max(v1[0], v2[0]);
            int right = min(v1[1], v2[1]);
            if(left + d <= right){
                return {left, left + d};
            }

            v1[1] > v2[1] ? ++j : ++i;
        }
        return {};
    }
};

int main(){
    vector<vector<int>> slot1 = {{10, 50}, {60, 120}, {140, 210}},
                        slot2 = {{0, 15}, {60, 70}};
    int duration = 5;
    Solution *obj = new Solution();

    vector<int> res = obj->meetingScheduler(slot1, slot2, duration);
    for(auto val:res){
        cout << val << " ";
    }
}
