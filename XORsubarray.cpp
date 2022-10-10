class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        
        int n = arr.size(), m = queries.size();
       
        vector<int> answers;
        
        vector<int> prefix(n , 0);
        
        prefix[0] = arr[0];
        
        for(int i = 1; i < n; i++)
            prefix[i] = prefix[i - 1] ^ arr[i];
        
        for(int i = 0, answer = 0; i < m; i++)
        {
            answer = prefix[queries[i][1]];
            
            if(queries[i][0]) answer ^= prefix[queries[i][0] - 1];
            
            answers.push_back(answer);
        }
        
        return answers;
    }
};