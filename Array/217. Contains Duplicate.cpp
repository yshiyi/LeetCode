class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        // Method 1: Using a set and check if the element is in the set
        set<int> s;
        int l = nums.size();
        for (auto val:nums) {
            if (s.find(val) != s.end()) {
                return true;
            }else {
                s.insert(val);
            }
        }
        return false;
        
        
        // Method 2: using a set. Save all the elements form nums to s, and compare the size.
        for (auto val:nums) {
            s.insert(val);
        }
        return !(s.size()==l);
        
    }
};
