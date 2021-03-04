class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        
      // Method 1:
      for(int i = 0; i < arr.size(); i++){

        	if(arr[i] == 0){
                for(int j = arr.size() - 1; j > i; j--){
                    arr[j] = arr[j - 1];                	
                }
                i++;
        	}
        }
        
        /* ==============================================*/
        // Method 2:
        int nums_zeros = 0;
        int l = arr.size();
        for (int i=0; i<l; i++) {
            if (i > l - nums_zeros - 1) {
                break;
            }
            if (arr[i] == 0) {
                if (i == l - nums_zeros - 1) {
                    arr[l-1]=0;
                    l--;
                    break;
                }
                nums_zeros++;
            }
        }

        int j = l - nums_zeros - 1;
        for (j; j>-1; j--) {
            if (arr[j] == 0) {
                arr[j + nums_zeros] = 0;
                nums_zeros--;
                arr[j + nums_zeros] = 0;
            }else {
                arr[j + nums_zeros] = arr[j];
            }
            
        }
        
    }
};
