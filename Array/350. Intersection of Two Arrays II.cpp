class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        result.resize(min(nums1.size(), nums2.size()));
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        
        vector<int>::iterator it = set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), result.begin());
        
        /* Note: it points to the position next to the last intersected element.
                 If it is pointing to result.end(), there must be zeros. We need to remove those zeros.
        */
        if (it != result.end()) {
            while(it!= result.end()) {
                result.erase(it);
            }
        }
        return result;
    }
};
