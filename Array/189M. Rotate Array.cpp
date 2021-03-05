class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
        // Method 1: using reverse(nums.begin(), nums.end())
        k %= nums.size();
        vector<int>::iterator it = nums.begin();
        for (int i=0; i<k; i++) {
            it++;
        }
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), it);
        reverse(it, nums.end());
        
        
        /* Method 2: Create an extra vector
                     Elements will be moved to (i+k)%nums.size() position.
        */
        k %= nums.size();
        vector<int> nums2;
        int l = nums.size();
        nums2.resize(l);
        for (int i=0; i<l; i++) {
            nums2[(i+k)%l] = nums[i];
        }
        nums.clear();
        for (auto v:nums2) {
            nums.push_back(v);
        }
    }
};
