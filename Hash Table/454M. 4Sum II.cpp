class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        map<int, int> m;
        int res = 0;
        for(auto& val1:A){
            for(auto& val2:B){
                m[val1+val2]++;
            }
        }
        
        for(auto& val3:C){
            for(auto& val4:D){
                int sum = val3 + val4;
                if(m.find(-sum)!=m.end()){
                    res += m[-sum];
                }
            }
        }
        return res;
    }
};
