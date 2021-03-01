class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        
        /* Method 1: create two vectors. A_even contains even elements, A_odd contains odd elements
                     Then insert all odd elements into A_even
        */
        vector<int> A_even, A_odd;
        for (int i=0; i<A.size(); i++) {
            if (A[i]%2==0) {
                A_even.push_back(A[i]);
            }else {
                A_odd.push_back(A[i]);
            }
        }
        for (int j=0; j<A_odd.size(); j++) {
            A_even.push_back(A_odd[j]);
        }
        return A_even;
      
        
        /* Method 2: two pointers.
                     The first pointer sweeps through vector.
                     The second pointer points to the beginning position of odd elements.
        */
        int j=0, tmp;
        for (int i=0; i<A.size(); i++) {
            if (A[i]%2==0) {
                swap(A[j], A[i]);
                j++;
            }
        }
        return A;
    }
};
