/*
277M. Find the Celebrity

Description:
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. 
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of 
whether A knows B. 
You need to find out the celebrity (or verify there is not one) by asking as few questions as possible 
(in the asymptotic sense).

You are given a helper function bool knows(a, b)which tells you whether A knows B. 
Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. 
Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.


Example 1:
Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. 
graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. 
The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.


Note:
The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 
means person i knows person j while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.

Similar Question:
Find the Town Judge - Easy
*/

/*
Method 1: Brute Force
          Check each person and see if anyone is a celebrity.
          The conditions of being a celebrity is every one knows him and he doesn't know anyone.
          i.e., know(i, j) && !know(j, i)
          
          Time complexity: O(n^2)
          Space complexity: O(1)
*/
/* The knows API is defined for you.
      bool knows(int a, int b); */
class Solution {
private:
    int num_people;
public:
    int findCelebrity(int n) {
        num_people = n;
        for(int i=0; i<n; ++i){
            if(isCelebrity(i)){
                return i;
            }
        }
        return -1;
    }
    
    bool isCelebrity(int i){
        for(int j=0; j<num_people; ++j){
            // Don't check if he knows himself
            if(i==j){continue;}
            if(know(i, j) || !know(j, i)){
                return false;
            }
        }
        return true;
    }
};

/*
Method 2: Logical Deduction
          Suppose knows(A, C) = 1. Then A can't be the celebrity, and C may be the celebrity.
          Hence, we don't need to check the relation between A and other people. This can rule out a lot of redundant search.
          We only need to check if C is the celebrity.
          
          Using this idea, we iterate over all people and narrow down to one single person.
          Finally, we check if this person is the celebrity.
          
          Time complexity: O(n)
          Space complexity: O(1)
*/
class Solution{
private:
    int num_people;
public:
    int findCelebrity(int n){
        num_people = n;
        int celebrity_candidate = 0;
        for(int i=0; i<n; ++i){
            if(knows(celebrity_candidate, i)){
                celebrity_candidate = i;
            }
        }
        if(isCelebrity(celebrity_candidate)){
            return true;
        }
        return false;
    }
    
    bool isCelebrity(int i){
        for(int j=0; j<num_people; ++j){
            if(j==i){continue;}
            if(knows(i, j) || !knows(j, i)){
                return false;
            }
        }
        return true;
    }
}




