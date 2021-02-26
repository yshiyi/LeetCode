class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int l = arr.size();
        int max = arr[l-1], temp = -1, t;
        for (int i=l-1; i>-1; i--) {
            // if (i == l-1) {
            //     arr[i] = -1;
            // }else {
            //     temp = arr[i];
            //     arr[i] = max;
            //     if (temp > max) {
            //         max = temp;
            //     }
            // }
            t = arr[i];
            arr[i] = temp;
            temp = std::max(temp, t);
        }
        return arr;
    }
};
