class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        // Method 1: two pointers
        if (nums.size()<1) {
            return nums.size();
        }
        
        vector<int>::iterator it = nums.begin()+1;
        int i = 1, l = nums.size();
        while (i < l) {
            if (nums[i] == nums[i-1]) {
                nums.erase(it);
                l--;
            }else {
                i++;
                it++;
            }
        }
        return nums.size();
        
        
        // Method 2: two pointers, move the distinct element front
        if(nums.size()<=1) return nums.size();
        int j = 1;
        for(int i=1;i<nums.size();i++){
            if(nums[i]!=nums[i-1]) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
        
    }
};
