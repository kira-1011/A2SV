class Solution {
public:
    int minPairSum(vector<int>& nums) {
        
        sort(nums.begin(), nums.end()); //nlogn
        
        int n = nums.size(), p1 = 0, p2 = n - 1, sum = 0, maxPairSum = 0;
        
        
        while(p1 < p2)
        {   
            sum = nums[p1] + nums[p2];
            
            if(sum > maxPairSum)
                maxPairSum = sum;
            
            p1++;
            p2--;
        }
        
        return maxPairSum;
    }
};