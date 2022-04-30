class Solution {
public:
    int fib(int n) {
        const double golden_ratio = 1.6180339887498948482;
        
        int res = (pow(golden_ratio, n) - pow((1 - golden_ratio), n)) / sqrt(5);
        
        return res;
    }
    
};





class Solution {
public:
    int fib(int n) {
        
        if(n == 1)
            return 1;
        
        if(n == 0)
            return 0;
        
        return fib(n - 1) + fib(n - 2);
    }
};