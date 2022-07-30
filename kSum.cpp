class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
      
        int operations = 0;
        
        unordered_map<int,int> myMap; // num , count
        
        for(auto i : nums)
            myMap[i]++;
        
        for(auto num : nums)
        {
            if(myMap[num] > 0)
            {
                myMap[num] --;
                
                if(myMap[k - num] > 0)
                {
                    myMap[k - num]--;
                    
                    operations++;
                }
            }
        }
        
        
       
        return operations;
    }
};