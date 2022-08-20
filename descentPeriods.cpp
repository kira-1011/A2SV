class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        
        vector<int> stack;
        long long n = prices.size(), descentPeriods = 0, m = 0;
        
        if(n == 1)
            return 1;
        
        stack.push_back(prices[0]);
        
        for(int i = 1; i < n; i++)
        {
            if(stack.back() - prices[i] == 1)
                stack.push_back(prices[i]);
            else
            {
                m = stack.size();
                
                descentPeriods += ((m * (m + 1)) / 2);
                
                while(!stack.empty())
                    stack.pop_back();
                
                stack.push_back(prices[i]);
            }
        }
        
        
        if(!stack.empty())
        {
            m = stack.size();

            descentPeriods += ((m * (m + 1)) / 2);
        }
        
        return descentPeriods;
        
    }
};