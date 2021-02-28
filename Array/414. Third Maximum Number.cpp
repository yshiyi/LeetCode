class Solution {
public:
    int thirdMax(vector<int>& nums) {
        
        // Method: using vector<int>::reverse_iterator rit = nums.rbegin(), rit++ goes from right to left
        if (nums.size() > 2) {
            sort(nums.begin(), nums.end());
            int count = 0;
            for (vector<int>::reverse_iterator it=nums.rbegin(); it!=nums.rend()-1; ++it) {
                if (*it > *(it+1)) {
                    count++;
                }
                if (count == 2) {
                    return *(it+1);
                }
            }
        }
        
        return *max_element(nums.begin(), nums.end());
    }
};
