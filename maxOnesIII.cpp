class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        
        int windowStart = 0, windowEnd = 0, zeroes = 0, size = 0, max = 0, n = nums.size();
        
        
        while(windowEnd < n)
        {
            if(nums[windowEnd] == 0) zeroes++;
            
            while(zeroes > k)
            {
                if(nums[windowStart] == 0) zeroes--;
                
                windowStart++;
            }
            
            size = windowEnd - windowStart + 1;
            
            if(size > max) max = size;
            
            windowEnd++;
        }
        
        return max;
    }
};