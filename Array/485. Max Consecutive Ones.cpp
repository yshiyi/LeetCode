class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int counter = 0, max_ones = 0;
        for (int i=0; i<nums.size(); i++) {
            if (nums[i]==1) {
                counter++;
            }else {
                if (counter > max_ones){
                    max_ones = counter;
                }
                counter = 0;
            }
        }
      
        /* Note: if nums ends with 1, we don't compared counter with max_ones in the loop
                 Therefore, we need to return max(counter, max_ones)
        */
        return max(max_ones, counter);
    }
};
