class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        // Method 1:
        bool result = false;
        set<double> s; 
        for (int i=0; i<arr.size(); i++) {
            if (s.find((double)arr[i]/2) != s.end() || s.find((double)arr[i]*2) != s.end()) {
                return result = true;
            }else {
                s.insert((double)arr[i]);
            }
        }
        return result;
      
        
        // Method 2: using count(v.begin(), v.end(), value)
        for(auto i: arr){
            // just take care of exeptions and use count all over :)
            if (i == 0){
                if (count(arr.begin(), arr.end(), i) > 1) 
                    return true;
                else
                    continue;
            }
            if (count(arr.begin(), arr.end(), i*2))
                return true;
        }
        return false;
    }
};
