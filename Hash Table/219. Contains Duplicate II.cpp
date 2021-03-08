class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // Note: set the initial value of min_dis 
        //       as allowed maximum value of k
        int min_dis = pow(10, 5), dis;
        map<int, int> m;
        map<int, int>::iterator it;
        for (unsigned int i=0; i<nums.size(); ++i) {
            it = m.find(nums[i]);
            if (it == m.end()) {
                m.insert(make_pair(nums[i], i));
            }else {
                dis = i - (it)->second;
                if (dis <= min_dis) {
                    min_dis = dis;
                    m[nums[i]] = i;
                }else {
                    continue;
                }
            }
        }
        
        if (min_dis <= k) {
            return true;
        }else {
            return false;
        }
    }
};
