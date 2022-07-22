class Solution {
public:
    string removeKdigits(string num, int k) {
        
        int n = num.length();
        
        vector<char> monotonicStack;
        
        int kDigits = 0;
        
        if(n == 1)
            return "0";
        
        if(k == n)
            return "0";
        
        
        int i;
        
        for(i = 0; i < n; i++)
        {

           while(monotonicStack.size() != 0 && num[i] < monotonicStack.back() && kDigits < k)
           {
                monotonicStack.pop_back();
                kDigits++;
           }
            
            monotonicStack.push_back(num[i]);
            
        }
        
        while(kDigits < k)
        {
            monotonicStack.pop_back();
            kDigits++;
        }
                                                                                                                                                                               
        string s(monotonicStack.begin(), monotonicStack.end());
        
        
         while(s[0] == '0' && s.length() != 1)
            s.erase(0, 1);
        
        return s;
    }
};  