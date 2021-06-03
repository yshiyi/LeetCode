/*
Method: Using Hashtable
        Traverse nums1, record the values and their appearances.
        Then sweep through nums2. 
        If the value is in the map and its value is greater than 0, then save it to res and reduce its value in map by 1.
*/
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> m;
        vector<int> res;
        for (auto a : nums1) ++m[a];
        for (auto a : nums2) {
            if (m[a] > 0){
                res.push_back(a);
                m[a]--;
            }
        }
        return res;
    }
};
