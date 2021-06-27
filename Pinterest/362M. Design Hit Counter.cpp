/*
362M. Design Hit Counter

Description:
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) 
and you may assume that calls are being made to the system in chronological order 
(ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?

Similar Question:
Logger Rate Limiter - Easy
*/

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

/*
Method 1: Using two arrays.
          One is to record the timestamp, and the other is to record the number of hits.
          Take the modulo of the timestamp every time when we call counter.hits().
          If the timestamp saved in times is different from the new one, it means the time has passed by 300s.
          We need to update the values saved in times and hits.
          To obtain the total number of hits within the passed 300s, we only need to iterate over hits().
          Check the difference between current timestamp and times[i].
*/
class Solution{
public:
    vector<int> hits, times;
    Solution(){
        hits.resize(300);
        times.resize(300);
    }
    void hit(int timestamp){
        int index = timestamp%300;
        if(times[index]!=timestamp){
            times[index] = timestamp;
            hits[index] = 1;
        }else{
            ++hits[index];
        }
    }
    int getHits(int timestamp){
        int total=0;
        for(int i=0; i<times.size(); ++i){
            if(timestamp - times[i] < 300){
                total += hits[i];
            }
        }
        return total;
    }
};

/*
Method 2: Using queue.
          Create a queue to save the timestamp. 
          Check the difference between the q.front() and the current timestamp.
          If the difference is greater than or equal to 300s, then we need to pop the q.front().
*/
class Solution2{
public:
    queue<int> q;
    void hit(int i){
        q.push(i);
    }
    int getHits(int i){
        while(i - q.front()>=300){
            q.pop();
        }
        return q.size();
    }
};

int main() {
    Solution *counter = new Solution();
    counter->hit(1);
    counter->hit(2);
    counter->hit(3);
    cout << counter->getHits(4) << endl;
    counter->hit(300);
    cout << counter->getHits(300) << endl;
    cout << counter->getHits(301) << endl;

}
