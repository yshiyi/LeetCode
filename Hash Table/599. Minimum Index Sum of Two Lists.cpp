class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        map<string, int> m;
        for(int i=0; i<list1.size(); ++i){
            m[list1[i]] = i;
        }
        int sum_min = INT_MAX;
        vector<string> res;
        for(int j=0; j<list2.size(); ++j){
            if(m.find(list2[j])!=m.end()){
                int sum = j + m[list2[j]];
                if(sum < sum_min){
                    sum_min = sum;
                    res.clear();
                    res.push_back(list2[j]);
                }else if(sum==sum_min){
                    res.push_back(list2[j]);
                }
            }
        }
        return res;
    }
};
