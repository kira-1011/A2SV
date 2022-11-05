class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        
        int n = security.size();

        vector<int> decreasingSum(n, 0);

        vector<int> increasingSum(n, 0);

        vector<int> goodDays;

        for(int i = 1; i < n; i++)
            if(security[i - 1] >= security[i]) decreasingSum[i] = (decreasingSum[i - 1] + 1);

        for(int j = n - 2; j > 0; j--)
            if(security[j + 1] >= security[j]) increasingSum[j] = (increasingSum[j + 1] + 1); 

        for(int i = time; i < n; i++)
            if(decreasingSum[i] >= time && increasingSum[i] >= time) goodDays.push_back(i);

        return goodDays;

    }
};