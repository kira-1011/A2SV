class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        
        
        make_heap(stones.begin(), stones.end());
        
        int y,x;
        
        while (stones.size() > 1)
        {
            y = stones[0];
            
            if(stones.size() >= 3)
            {
                if(stones[1] < stones[2])
                {
                     x = stones[2];
                }
                else
                {
                     x = stones[1];
                } 
            }
            else
            {
                 x = stones[1]; 
            }
          
            

            cout << "y : " << y << " x : " << x << endl;

            pop_heap(stones.begin(), stones.end());
            stones.pop_back();
            pop_heap(stones.begin(), stones.end()); 
            stones.pop_back(); 

            if(x != y)
            {
                stones.push_back(y - x);
                push_heap(stones.begin(), stones.end());
            }   
        }
        
        if(stones.size())
            return stones[0];
        
        return 0;
        
 
    }
};