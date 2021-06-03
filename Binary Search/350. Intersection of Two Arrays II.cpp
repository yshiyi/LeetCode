/*
Method: This is a solution using binary search method.
        Different from 349. Intersection of Two Arrays, we need to record the appearances of the value as many times as it shows.
        To avoid to save duplicates, we have to remove the value that is saved to the result.
*/
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        sort(nums2.begin(), nums2.end());
        for(auto& val:nums1){
            int pos = binarySearch(nums2, val);
            if(pos!=-1){
                res.push_back(val);
                // vec.erase() takes a position iterator.
                nums2.erase(nums2.begin()+pos);
            }
        }
        return res;
    }
    int binarySearch(vector<int>& nums, int target){
        int left = 0, right = nums.size()-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid]>target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return -1;
    }
};
