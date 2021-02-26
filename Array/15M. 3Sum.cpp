class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> triplet;
        int r, l, sum;
        
        sort(nums.begin(), nums.end());
        for (int i=0; i<nums.size(); i++) {
            if (i>0 && nums[i]==nums[i-1]) {
                continue;
            }
            r = nums.size() - 1;
            l = i + 1;
            while (l < r) {
                sum = nums[i] + nums[l] + nums[r];
                if (sum > 0) {
                    r--;
                }else if (sum < 0) {
                    l++;
                }else if (sum == 0) {
                    triplet.push_back(nums[i]);
                    triplet.push_back(nums[l]);
                    triplet.push_back(nums[r]);
                    result.push_back(triplet);
                    triplet.clear();
                    l++;
                    while (l<r && nums[l]==nums[l-1]){
                        l++;
                    }
                }
            }
        }
        return result;
    }
};
