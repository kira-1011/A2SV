//Using Recursion

class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n == 1)
            return true;
        else if(n % 3 != 0 || n == 0)
            return false;
        else
        {
            n = n / 3;
            return isPowerOfThree(n);
        }
            
    }
};

//Using loop

class Solution {
public:
    bool isPowerOfThree(int n) {
      
        while(n != 1){
            if(n % 3 != 0 || n == 0)
                return false;
            else
                n = n / 3;
        }
        
        return true;
            
    }
};