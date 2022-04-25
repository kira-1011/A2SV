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