class Solution {

public:
    void moveZeroes(vector<int>& nums) {
        
        if(nums.size() <= 1)
            return;
        
        int p1 = 0, p2 = 1, n = nums.size();
        
        while(p2 < n)
        {
            if(nums[p1] == 0 && nums[p2] != 0)
            {
                int temp = nums[p1];
                nums[p1] = nums[p2];
                nums[p2] = temp;
                p1++;
                p2++;
            }
            
            else if(nums[p1] == 0 && nums[p2] == 0)
                p2++;
            else
            {
                p1++;
                p2++;
            }
        }
    }
};