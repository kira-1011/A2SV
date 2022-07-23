class Solution {
    
public:
    
    double myPow(double x, int n) {
        
        if(n == 0)
            return 1;
        
        if(x == 1)
            return 1;
           
        
        if(n == 1)
             return x;
        
        if(n == -1)
            return (1 / x);
           
        
        double y = myPow(x, n / 2);
        
        double z = 1;
        
        if(n % 2 != 0)
        {
            if(n < 0)
                z = (1 / x);
            
            else
                z = x;
        }
        else
            z = 1;
        
          
        y = y * y * z;
        
        return y;
    }
};