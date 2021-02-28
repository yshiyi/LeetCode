class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        /* Method: using reverse_iterator
        */
        vector<int>::reverse_iterator rit = digits.rbegin();
        for (rit; rit!=digits.rend(); rit++) {
            if (*rit != 9) {
                ++(*rit);
                return digits;
            }else {
                *rit = 0;
            }
        }
        vector<int> res;
        res.resize(digits.size()+1);
        res[0] = 1;
        for (int i=1; i<res.size(); i++) {
            res[i] = digits[i-1];
        }
        return res;
    }
};
