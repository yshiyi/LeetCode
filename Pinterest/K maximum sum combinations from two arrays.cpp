
/*
K maximum sum combinations from two arrays
Difficulty Level : Hard

Description:
Given two equally sized arrays (A, B) and N (size of both arrays).
A sum combination is made by adding one element from array A and another element of array B. 
Display the maximum K valid sum combinations from all the possible sum combinations.

Example 1:
Input :  A[] : {3, 2}
         B[] : {1, 4}
         K : 2 [Number of maximum sum
               combinations to be printed]
Output : 7    // (A : 3) + (B : 4)
         6    // (A : 2) + (B : 4)

Example 2:
Input :  A[] : {4, 2, 5, 1}
         B[] : {8, 0, 3, 5}
         K : 3
Output : 13   // (A : 5) + (B : 8)
         12   // (A : 4) + (B :  8)
         10   // (A : 2) + (B : 8)
*/

/*
Method: Brute Force. Using priority queue.
        Iterate over two arrays, and save the sum into the priority queue.
        Maintain the size of the queue as k.
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
    vector<int> KMaxCombinations(vector<int> vec1, vector<int> vec2, int k){
        sort(vec1.begin(), vec1.end(), cmp());
        sort(vec2.begin(), vec2.end(), cmp());
        vector<int> res;
        priority_queue<int, vector<int>, cmp> q;
        for(int i=0; i<vec1.size(); ++i){
            for(int j=0; j<vec2.size(); ++j){
                int sum = vec1[i] + vec2[j];
                q.push(sum);
                if(q.size()>k){
                    q.pop();
                }
            }
        }
        while(q.size()){
            res.push_back(q.top());
            q.pop();
        }
        return res;
    }
};

int main(){
    vector<int> vec1 = {4, 2, 5, 1};
    vector<int> vec2 = {8, 0, 7, 3};
    int k = 16;

    Solution *obj = new Solution();
    vector<int> res = obj->KMaxCombinations(vec1, vec2, k);
    for(auto val:res){
        cout << val << " ";
    }cout << endl;
}
