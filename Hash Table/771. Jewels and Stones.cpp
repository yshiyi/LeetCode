class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int res = 0;
        for(auto& c:stones){
            if(jewels.find(c)!=-1){
                res++;
            }
        }
        return res;
    }
};
