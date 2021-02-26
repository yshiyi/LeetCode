class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.size() < 1) {return nums.size();}
      
        // Method 1: two pointers, pointer j points to the distinct elements and pointer i sweeps through nums
        int i = 0, j = 0;
        for (i; i<nums.size();i++) {
            if(nums[i]!= val) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
        
        
        // Method 2: move the last element to front and remove the last element.
        int i=0, l=nums.size();
        vector<int>::iterator it = nums.end();
        while (i<l) {
            if (nums[i] == val) {
                nums[i] = nums[l-1];
                nums.erase(it-1);
                it--;
                l--;
            }else{
                i++;
            }
        }
        return l;
        
        
        
        
    }
};
