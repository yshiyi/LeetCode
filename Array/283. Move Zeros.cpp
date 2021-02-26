class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        if (nums.size() < 1) {return;}
        int i = 0, j = 0, temp;
        for (i; i<nums.size(); i++) {
            if (nums[i] != 0) {
                temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                j++;
            }
        }
    }
};
