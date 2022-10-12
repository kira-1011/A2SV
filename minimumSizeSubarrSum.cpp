class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        
        int p1 = 0, p2 = 0, n = nums.size(), sum = 0, minSize = INT_MAX;
        
        for(int i = 1; i < n; i++)
            nums[i] += nums[i - 1];
        
        while(p2 < n)
        {
            sum = nums[p2];
            
            if(p1) sum -= nums[p1 - 1];
            
            if(sum >= target)
            {
                if(minSize > (p2 - p1 + 1)) minSize = p2 - p1 + 1;
                
                p1++;
            }
            else
                p2++;
        }
        
        if(minSize == INT_MAX) return 0;
        
        return minSize;
    }
};