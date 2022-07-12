class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        
        
        make_heap(stones.begin(), stones.end());
        
        int y, x;
        
        while (stones.size() > 1)
        {
            y = 0;
            
            if(stones.size() == 2)
                x = 1;
            
            else
                (stones[2 * y + 1] >= stones[2 * y + 2])? x = 2 * y + 1 :  x = 2 * y + 2;
            
            
            int num1 = stones[y];
            
            int num2 = stones[x];
           
            pop_heap(stones.begin(), stones.end());
            
            stones.pop_back();

            pop_heap(stones.begin(), stones.end());
            
            stones.pop_back();
            
            if(num1 != num2)
            {
                stones.push_back(num1 - num2);
                push_heap(stones.begin(), stones.end());
            }
            
        }
        
        if(stones.size())
            return stones[0];
        
        return 0;
        
 
    }
};