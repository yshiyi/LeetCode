class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        /* Method 1: using count(v.begin(), v.end(), value)
                     This method takes about 952 ms.
        */
        int single_num;
        for (auto i:nums) {
            if (count(nums.begin(), nums.end(), i) == 1) {
                return single_num = i;
            }
        }
        return single_num;
        
        
        /* Method 2: using XOR
                     In c++, XOR is ^;
                     a ^ 0 = a; a ^ a = 0;
                     This method takes only 16 ms.
        */
        int result = 0;
        for (auto i:nums) {
            result = result ^ i;
        }
        return result;
    }
};
