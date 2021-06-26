/*
359. Logger Rate Limiter
Hash Table

Description:
Design a logger system that receive stream of messages along with its timestamps,
each message should be printed if and only if it is not printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.

Example:
Logger logger = new Logger();
// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true;
// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;
// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;
// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;
// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;
// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
*/
//
// Created by Shiyi Yang on 2021-03-21.
//
#include<iostream>
#include<map>
#include<algorithm>
using namespace std;

class Solution{
public:
    map<string, int> myMap_;
    bool shouldPrintMessage(string& message, int timestamp){
        if(myMap_.count(message) && timestamp-myMap_[message] < 10){
            return false;
        }else{
            myMap_[message] = timestamp;
            return true;
        }
    }
};

class Solution1{
public:
    static bool shouldPrintMessage(string& message, int timestamp){
        if(myMap_.find(message)==myMap_.end() || timestamp - myMap_[message] >= 10){
            myMap_[message] = timestamp;
            return true;
        }else{
            return false;
        }
    }
    typedef map<string, int> myMap;
    static  myMap myMap_;
};
Solution::myMap Solution::myMap_;

class Solution3{
public:
    bool shouldPrintMessage(string& message, int timestamp){
        if(myMap_.find(message)==myMap_.end() || timestamp - myMap_[message] >= 10){
            myMap_[message] = timestamp;
            return true;
        }else{
            return false;
        }
    }
    map<string, int> myMap_;
};

int main() {
    Solution* obj = new Solution;
    Solution obj1;
    string str1 = "foo", str2 = "bar";

    /*cout << obj->shouldPrintMessage(str1, 1) << endl;
    cout << obj1.shouldPrintMessage(str2, 2) << endl;
    cout << obj->shouldPrintMessage(str1, 3) << endl;
    cout << obj1.shouldPrintMessage(str2, 8) << endl;
    cout << obj->shouldPrintMessage(str1, 10) << endl;
    cout << obj->shouldPrintMessage(str1, 11) << endl;

    for(auto& key:obj->myMap_){
        cout << key.first << " " << key.second << endl;
    }*/

    cout << obj->shouldPrintMessage(str1, 1) << endl;
    cout << obj->shouldPrintMessage(str2, 2) << endl;
    cout << obj->shouldPrintMessage(str1, 3) << endl;
    cout << obj->shouldPrintMessage(str2, 8) << endl;
    cout << obj->shouldPrintMessage(str1, 10) << endl;
    cout << obj->shouldPrintMessage(str1, 11) << endl;
    

    return 0;
}

