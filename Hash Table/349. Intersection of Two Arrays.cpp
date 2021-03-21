class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        
        /* Method 1: Using set_intersection. It returns a pointer which points to the end of intersection.
                     Note: Initialize v with size of min(nums1.size(), nums2.size()).
                           Resize v by using v.resize(it - v.begin()).
        */
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> v, res;
        v.resize(min(nums1.size(), nums2.size()));
        vector<int>::iterator it = set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), v.begin());
        v.resize(it-v.begin());
        
        set<int> s;
        for(auto& val:v){
            s.insert(val);
        }
        for(auto& val:s){
            res.push_back(val);
        }
        return res;
        
        
        /* Method 2: Using hashset.
                     Save all elements from nums1 to a set.
                     Then sweep nums2. If the element is in the set, then save it to res.
                     Note: We also need to remove the non-unqiue elements from set to prevent the duplication.
        */
        set<int> s;
        vector<int> res;
        for(auto& val:nums1){
            s.insert(val);
        }
        for(auto& val:nums2){
            if(s.find(val)!=s.end()){
                res.push_back(val);
                s.erase(val);
            }
        }
        return res;
    }
};
