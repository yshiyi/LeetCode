class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size()==0){return 0;}
        if (s.size()==1){return 1;}
        int res = 0;
        int right = 0, left = 0, match = 0;
        unordered_map<char, int> window;
        while (right < s.size()){
            char c = s[right];
            window[c]++;
            
            while(window[c] > 1) {
                char d = s[left];
                window[d]--;
                left++;
            }
            
            right++;
            res = max(right-left, res);
        }
        return res;
    }
};
