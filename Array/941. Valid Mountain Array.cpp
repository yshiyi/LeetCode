class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        
        /* Method: There are some things need to notice
                   1. If start from i=1, need to check i<arr.size() in the while loops, 
                      check (i==1||i==arr.size()) in if, and return i==arr.size();
                   2. If statement checks if the peak is at the beginning or at the end. 
        */
        if (arr.size()<3) {
            return false;
        }
        int i=0;
        while (i < arr.size()-1 && arr[i] < arr[i+1]) {
            i++;
        }
        if (i==0 || i==arr.size()-1) {
            return false;
        }
        while (i < arr.size()-1 && arr[i] > arr[i+1]) {
            i++;
        }
        return i==arr.size()-1;
    }
};
