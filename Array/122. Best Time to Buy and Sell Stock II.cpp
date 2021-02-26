class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, buy = 0, sell = 0;
        int l = prices.size();
        
        // Method 1:
        for (int i=0; i<l-1; i++) {
            while (i<l-1 && prices[i] >= prices[i+1]) {
                i++;
            }
            
            buy = prices[i];
            while (i<l-1 && prices[i] <= prices[i+1]) {
                i++;
            }
            sell = prices[i];
            profit += sell - buy;
        }
      
      
        // Method 2:
        for (int i=0; i<l-1; i++) {
            if (prices[i+1]>prices[i]) {
                profit += prices[i+1] - prices[i];
            }
        }
        
        return profit;
    }
};
