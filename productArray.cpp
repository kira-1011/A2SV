class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) 
    {
        int n = nums.size();
        vector<int> prefixProduct (n, 1);
        vector<int> suffixProduct (n ,1);
        vector<int> answer;
        
        prefixProduct[0] = nums[0];
        suffixProduct[n - 1] = 1;
        
        for(int i = 1; i < n; i++)
            prefixProduct[i] = prefixProduct[i - 1] * nums[i];
        
        for(int i = n - 2; i >= 0; i--)
            suffixProduct[i] = suffixProduct[i + 1] * nums[i + 1];
        
        for(int i = 0, left = 1, right = 1; i < n; i++)
        {
            if(i == 0)
                left = 1;
            else
                left = prefixProduct[i - 1];
            
            right = suffixProduct[i];
            
            answer.push_back(left * right);
            
        }
        return answer;
    }
};