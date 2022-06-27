class Solution {
public:
    int maxCoins(vector<int>& piles) {
        
        
        sort(piles.begin(), piles.end(), greater <int>());
        
        int limit = piles.size() - (piles.size() / 3);
        
        int max = 0;
        
        for(int i = 0; i < limit; i++){
            
            if(i % 2 != 0)
                max += piles[i];
        }
        
        return max;
    }
};