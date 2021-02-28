class Solution {
public:
    int thirdMax(vector<int>& nums) {
        
        /* Method: using vector<int>::reverse_iterator rit = nums.rbegin(), rit++ goes from right to left
                   Note: 1. We can't access to nums.rend(), so we terminate the loop at the second element
                         2. Using *(it+1) to access next element. Using *(it++), it will automatically increase by 1.
                         3. Return next element when count == 2
        */
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
