class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int result = 0;
        int l = nums.size();
        string s;
        for (int i=0; i<l; i++) {
            s = to_string(nums[i]);
            if (s.size()%2 == 0) {
                result++;
            }
        }
        return result;
    }
};
