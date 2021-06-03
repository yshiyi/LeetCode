// This is a solution using binary search.
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s;
        sort(nums2.begin(), nums2.end());
        for(auto& val:nums1){
            if(binarySearch(nums2, val)){
                s.insert(val);
            }
        }
        return vector<int> (s.begin(), s.end());
    }
    bool binarySearch(vector<int>& nums, int target){
        int left = 0, right = nums.size()-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid]==target){
                return true;
            }
            if(nums[mid]>target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return false;
    }
};
