class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        int i = 0, j = 1, n = temperatures.size();

        vector<int> answer (n , 0);

        vector<vector<int>> monotonicStack;
        
        vector<int> nextGrt;
        
        int nextGrtIdx = -1;

        for(int i = n - 1; i >= 0; i--)
        {

            while(monotonicStack.size() != 0 && temperatures[i] >= monotonicStack.back()[0])
                monotonicStack.pop_back();            
            
            nextGrtIdx = (monotonicStack.size() == 0)?  -1 : monotonicStack.back()[1];
            
            nextGrt = {temperatures[i], i};
            
            monotonicStack.push_back(nextGrt);
            
            nextGrt.pop_back();

            answer[i] = (nextGrtIdx != -1)?  (nextGrtIdx - i) : 0;
        }
        
        return answer;
    }
};