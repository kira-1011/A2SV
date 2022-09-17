class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        
        int n = nums.size(), winStart = 0, winEnd = firstLen - 1;
        int p1 = 0, p2 = 0, sum = 0, sumLeft = 0, sumRight = 0, max  = 0, tempMax = 0;
        
        vector<int> prefix(n , 0);
        
        prefix[0] = nums[0];
        
        for(int i = 1; i < n; i++)
            prefix[i] = prefix[i - 1] + nums[i];
        
        while(winEnd < n)
        {
            
            p1 = winStart - 1;
            p2 = winEnd + 1;
            
            sum = prefix[winEnd];
     
            
            if(winStart != 0)
                sum -= prefix[p1];

            
            //left
            while(p1 - secondLen + 1 >= 0)
            {
                sumLeft = prefix[p1];
                
                if(p1 - secondLen + 1 != 0)
                    sumLeft -=  prefix[abs(p1 - secondLen)];
                
                if(sum + sumLeft > max)
                    max = sum + sumLeft;
                
                p1--;
            }
            
            sumLeft = max;
            
            //right
            while(p2 + secondLen - 1 < n)
            {
                sumRight = prefix[p2 + secondLen - 1];
                
                if(p2 != 0)
                    sumRight -= prefix[p2 - 1];
                
                 if(sum + sumRight > max)
                    max = sum + sumRight;
                
                p2++;
            }
            
            sumRight = max;
            
            max = std::max(sumLeft, sumRight);
            
            winStart++;
            
            winEnd = winStart + (firstLen - 1);

        }
        
        return max;
    }
};