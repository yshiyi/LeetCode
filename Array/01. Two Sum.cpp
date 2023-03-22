class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        int l = nums.size();
        map<int, int>::iterator it;
        vector<int> result;
        for (int i=0; i<l; i++) {
            cout << i << endl;
            it = m.find(target - nums[i]);
            if(it==m.end()) {
                m.insert(make_pair(nums[i], i));
            }else {
                result.push_back(i);
                // result.push_back(m[target-nums[i]]);
                result.push_back((*it).second);
                break;
            }
        }
        return result;
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Length
        int l = nums.size();
        unordered_map<int, int> m;
        vector<int> result;
        int i = 0;
        for (auto val:nums){
            if (m.find(target-val)==m.end()){
                m[val] = i;
            }else{
                result.push_back(i);
                result.push_back(m[target-val]);
            }
            i++;
        }
        return result;
    }
};
