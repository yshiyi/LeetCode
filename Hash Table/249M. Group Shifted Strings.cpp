/*
Description:
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd".
We can keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz" or "adg -> beh -> cfi ..."
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
Example:
given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
*/
//
// Created by Shiyi Yang on 2021-03-11.
//
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> m;
        for (auto str:strings) {
            m[convertString(str)].push_back(str);
        }
        unordered_map<string, vector<string>>::iterator it=m.begin();
        while (it!=m.end()) {
            cout << (*it).first << endl;
            res.push_back(it->second);
            it++;
        }
        return res;
    }

    string convertString(string str) {
        vector<int> v;
        string res;
        int num1, num2;
        /*
        for (int i=0; i<str.size(); ++i) {
            num1 = (int)str[i] - 97;
            v.push_back(num1);
        }
        for (int i=0; i<v.size(); ++i) {
            num2 = v[i] - v[0];
            if (num2 < 0) {
                num2 +=  26;
            }
            res.insert(i, to_string(num2));
        }
        */
        
        int num0 = (int)str[0] - 97;
        for (int i=0; i<str.size(); ++i) {
            num1 = (int)str[i] - 97 - num0;
            if (num1 < 0) {
                num1 += 26;
            }
            res.insert(i, to_string(num1));
        }
      
        return res;
    }
};

void print_vector(vector<vector<string>> v){
    cout << "[";
    for(int i = 0; i<v.size(); i++){
        cout << "[";
        for(int j = 0; j <v[i].size(); j++){
            cout << v[i][j] << ", ";
        }
        cout << "], ";
    }
    cout << "]"<<endl;
}

int main() {
    Solution* obj = new Solution();
    vector<string> vec = {"abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"};
    print_vector(obj->groupStrings(vec));  //[[a, z, ], [acef, ], [az, ba, ], [abc, bcd, xyz, ], ]

    return 0;
}
