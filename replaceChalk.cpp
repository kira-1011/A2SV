class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        
        int n = chalk.size(), replace = 0;
        
        vector<long> chalkSum (n , 0);
        
        chalkSum[0] = chalk[0];
        
        for(int i = 1; i < n; i++)
            chalkSum[i] = chalkSum[i - 1] + chalk[i];
        
        k = k % chalkSum[n - 1];
        
        for(int i = 0; i < n; i++)
        {
            if(k < chalkSum[i]){
                replace = i;
                break;
            }
        }
        
        return replace;
        
    }
};
