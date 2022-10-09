class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        
        int p1 = 0, p2 = 0, n = nums.size(), maxSize = 0, zeroes = 0;
        
        if(!(nums[p2])) zeroes++;
        
        while(p2 < n)
        {
            while(zeroes > 1 && p1 < p2)
            {
                if(!(nums[p1])) zeroes --;
                p1++;
            }
            
            if(maxSize < p2 - p1 + 1) maxSize = p2 - p1 + 1;
            
            p2++;
            
            if((p2 < n) && !(nums[p2])) zeroes++;
        }
        
        if(!zeroes) return n - 1;
        
        return (maxSize - 1);
    }
};