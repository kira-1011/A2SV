class Solution {
public:
    int hIndex(vector<int>& citations) {
        
        int n = citations.size(), hIndex = 0;
        
        sort(citations.begin(), citations.end(), greater<>());
        
        for(int i = 1; i <= n; i++)
        {
            if(citations[i - 1] >= i)
                hIndex++;
            else
                break;
        }
        
        return hIndex;
    
    }
};