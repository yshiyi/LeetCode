#include <algorithm>
class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> heights_org = heights;
        sort(heights.begin(), heights.end());
        int result = 0;
        for (int i=0; i < heights.size(); i++) {
            if (heights_org[i] != heights[i]) {
                result++;
            }
        }
        return result;
    }
};
