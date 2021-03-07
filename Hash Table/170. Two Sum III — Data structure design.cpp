/* 170. Two Sum III — Data structure design
        Hash Table
    Description:
    Design and implement a TwoSum class. It should support the following operations: add and find.
    add - Add the number to an internal data structure.
    find - Find if there exists any pair of numbers which sum is equal to the value.
    Example 1:
    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false
    Example 2:
    add(3); add(1); add(2);
    find(3) -> true
    find(6) -> false
*/

//
// Created by Shiyi Yang on 2021-03-07.
//
#include <iostream>
#include <set>
using namespace std;

class TwoSum {
private:
    set<int> s1, s2;
public:
    TwoSum(){};
    void add(int val) {
        s1.insert(val);
    }
    bool find(int val) {
        for (set<int>::iterator it=s1.begin(); it!=s1.end(); ++it) {
            int remain = val - *it;
            if (s2.find(remain) != s2.end()) {
                return true;
            }else {
                s2.insert(remain);
            }
        }
        return false;
    }
};

int main() {
    TwoSum* obj = new TwoSum();
    obj->add(1);
    obj->add(3);
    obj->add(5);
    cout << obj->find(2) << endl;
    cout << obj->find(4) << endl;
    cout << obj->find(7) << endl;
    cout << obj->find(8) << endl;

    return 0;
}
