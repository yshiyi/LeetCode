/* Method 1: Using hash table
             The key is the element in nums, and the value is the index of the element in nums.
             We find out the minimum distance between two duplicate elements.
             In the end, we check if the minimum distance is less than k.
*/
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // Note: set the initial value of min_dis 
        //       as allowed maximum value of k
        int min_dis = INT_MAX;
        map<int, int> m;
        map<int, int>::iterator it;
        for (unsigned int i=0; i<nums.size(); ++i) {
            it = m.find(nums[i]);
            if (it == m.end()) {
                //m.insert(make_pair(nums[i], i));
                m[nums[i]] = i;
            }else {
                int dis = i - (it)->second;
                if (dis <= min_dis) {
                    min_dis = dis;
                    m[nums[i]] = i;
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


/* Method 2: Sliding Window
*/
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> m;
        int right = 0, left = 0;
        while(right < nums.size()){
            int val = nums[right];
            if(m.find(val)==m.end()){
                m[val] = right;
            }else if(right - m[val] <= k){
                return true;
            }
            right++;
            
            if(right - left > k){
                m.erase(nums[left]);
                left++;
            }
        }
        return false;
    }
};
