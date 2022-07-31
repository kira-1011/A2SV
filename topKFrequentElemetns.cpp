class Solution {

public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        int n = nums.size();

        unordered_map<int, int> freqMap;
         
        vector<vector<int>> countBucket (n + 1, vector<int>(0));

        vector<int> answer;
        
        int max = 0, j = 0;
        
        if(n == 1)
        {
            answer.push_back(1);
            return answer;
        }
        
        for(auto i : nums)
            freqMap[i]++;
        
        for(auto i : freqMap)
            countBucket[i.second].push_back(i.first);
        
        for(auto i : freqMap)
        {
            if(max < i.second)
                max = i.second;
        }
        
        j = max;
        
        while(answer.size() != k)
        {
            int i = countBucket[j].size() - 1;
            
            while(!(countBucket[j].empty()))
            {
                answer.push_back(countBucket[j][i]);
                countBucket[j].pop_back();
                i--;
            }
            
            j--;
        }        
        
        return answer;
    }
};