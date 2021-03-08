class Solution {
public:
    bool isHappy(int n) {
        set<int> s;
        while (true) {
            n = squaredSum(n);
            if (n == 1) {
                return true;
            }
            if (s.find(n) != s.end()) {
                return false;
            }else {
                s.insert(n);
            }
        }
        
    }
    int squaredSum(int n) {
        string str = to_string(n);
        int sum = 0, mod;
        for (int i=0; i< str.size(); i++) {
            mod = n % 10;
            sum += pow(mod, 2);
            n = n / 10;  // n is defined as int, it will be automatically rounded down.
        }
        return sum;
    }
};
