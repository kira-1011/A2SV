class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        
        int n = nums.size();
        
        if(n == 0)
            return 0;
        
        if(n == 1)
        {
            if(nums[0] == k)
                return 1;

            return 0;
        }

        unordered_map<int, int> hashPrefixSum;
        
        unordered_map<int, int> :: iterator itr;

        int subArray = 0;

        int sum = 0;
        
        for(int i = 0; i < n; i++)
        {
            sum = sum + nums[i];
            
            if(sum == k)
                subArray++;
            
            if(hashPrefixSum.find(sum - k) != hashPrefixSum.end())
                    subArray += hashPrefixSum[sum - k];
            
            
            hashPrefixSum[sum]++;
        }
        
        return subArray;
       
    }
};