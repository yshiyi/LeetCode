/*
84H. Largest Rectangle in Histogram
Array, Stack

Description:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104

Similar Questions:
Maximal Rectangle - Hard
Maximum Score of a Good Subarray - Hard
*/

/*
Method 1: Brute force
          The basic idea is to go through the whole array and to find a local vertex.
          Once find a local vertex, we go back to the starting point from this position step by step.
          On each step, we determine the minimum value and the area of the rectangle that minimum value can span.
          Save the maximum area on each step as well.
          The time complexity of this approach can go up to O(n^2). Sure, it will exceed the time limit.
*/
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0;
        for(int i=0; i<heights.size(); i++){
            if(i+1<heights.size() && heights[i]<=heights[i+1]){
                continue;
            }
            int minH = INT_MAX;
            for(int j=i; j>=0; j--){
                minH = min(minH, heights[j]);
                int area = minH*(i-j+1);
                res = max(res, area);
            }
        }
        return res;
    }
};

/*
Method 2: Using Stack
          The technique is called monotonous stack in which we save the elements in monotonous sequence.
          In this problem, the area of the rectangle depends on the smallest integer.
          Hence, the values saved in the stack should be monotonically increasing.
          The basic procedure is:
          1. We save the values into a stack.
          2. When we encounter a value that is smaller than the previous one (i.e., the top one in the stack),
             we pop out the top value can calculate the area of the rectangle it can construct.
          3. Then we check out the new top value. If it is still smaller than the current value, we repeat step 2.
             We save the current value to the stack until there are no values greater than it.
*/
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0;
        // This stack saves the index of values instead of the values themself.
        stack<int> s;
        // Insert an extra 0 at the end of the array so that we can easily check the last value in the array.
        heights.push_back(0);
        for(int i=0; i<heights.size(); i++){
            // If we encounter a value that is smaller than the top value in the stack, 
            // we start to calculate the area of rectangle.
            while(!s.empty() && heights[s.top()] >= heights[i]){
                // We first save and pop out the top index.
                int cur = s.top(); s.pop();
                /* This part is tricky.
                   If the stack becomes empty, it means the current index contains the smallest value in the array so far.
                   Hence, the length of the area of the rectangle that it can construct is just the current index i.
                   If the stack is not empty, the length is i - s.top() - 1.
                   Note, the new top index must be the index right before cur. 
                   Imagine a sequence [1,3,2,4,7], 1 and 3 are processed when we get to 2. 
                */
                int length = s.empty() ? i : (i - s.top() - 1);
                int area = heights[cur] * length;
                res = max(res, area);
            }
            s.push(i);
        }
        return res;
    }
};
