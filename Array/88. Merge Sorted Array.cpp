class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> nums3;
        int i = 0;
        
        // Check if nums1 is empty
        if (nums1.size()>0) {
            while (i < m) {
                nums3.push_back(nums1[i]);
                i++;
            }
        }
      
        // Check if nums2 is empty
        if (n>0) {
            for (int j = 0; j<n; j++) {
                nums3.push_back(nums2[j]);
            }
        }
      
        // Check if nums3 is empty
        if (nums3.size()>0) {
            sort(nums3.begin(), nums3.end());
            nums1 = nums3;
        }
    }
};
