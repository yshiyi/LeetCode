class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        
        /* Method 1: using set_difference, it works. But exceeds time limit.
        */
        if (nums.size() < 2) {
            return nums;
        }
        vector<int> v;
        for (int i=1; i<nums.size()+1; i++) {
            v.push_back(i);
        }
        vector<int> v_Result;
        v_Result.resize(min(nums.size(), v.size()));
        sort(nums.begin(), nums.end());
        vector<int>::iterator it = set_difference(v.begin(), v.end(), nums.begin(), nums.end(), v_Result.begin());
        
        // This is the method to remove 0s in the intersection or difference
        if (it != v_Result.end()) {
            while (it != v_Result.end()) {
                v_Result.erase(it);
            }
        }
        return v_Result;
        
        
        /* Method 2: use elements in nums as index indicator, and then increase the corresponding elements in res.
                     e.g. [4,3,2,7,8,2,3,1] -> res = [0 1 2 2 1 0 0 1 1]
                     Finally, save the index numbers which contain zero
        */
        vector <int> res;
        res.assign(nums.size()+1,0);
        for (int i = 0; i < nums.size();i++){
            res[nums[i]]++;
        }
        
        nums.erase(nums.begin(),nums.end());
        
        for (int i = 1; i < res.size();i++){
            if (res[i] == 0){
                nums.push_back(i);
            }
        }
        return nums;
    }
};
