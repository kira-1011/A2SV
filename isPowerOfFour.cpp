//Without recursion or loops

class Solution {
public:
    bool isPowerOfFour(int n) {
       
        float result = logb(n);
        
        if(result == -1)
            return false;
        
        if(floor(result) == result)
            return true;
        else
            return false;
        
        
    }
    
    float logb(int n){
        
        if(n == 0)
            return -1;
        
        return log2(n) / log2(4);
    }
};


//Using Recursion

class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n == 1)
            return true;
        else if(n % 4 != 0 || n == 0)
            return false;
        else
        {
            n = n / 4;
            return isPowerOfFour(n);
        }
    }
};

//Using loop
class Solution {
public:
    bool isPowerOfFour(int n) {
        while(n != 1){
            if(n % 4 != 0 || n == 0)
                return false;
            else
                n = n / 4;
        }
        
        return true;
    }
};