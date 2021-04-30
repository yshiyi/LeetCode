/* 
This is a recursive solution.
We first create a vector to store the values and assign 1 to the first and the last position.
We then inquire the values in the previous row.
Finally, construct the current row based on the values from the previous row.
*/
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex+1);
        res[0] = 1;
        if(rowIndex==0){
            return res;
        }
        res[rowIndex] = 1;
        vector<int> preRow = getRow(rowIndex-1);
        for(int i=1; i<rowIndex; i++){
            res[i] = preRow[i-1] + preRow[i];
        }
        return res;
      }
};
