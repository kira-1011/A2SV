class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int windowStart = 0, windowEnd = 0, n = s.length(), max = 0, size = 0;
        
        unordered_map<char, int> map;
        
        for(windowEnd = 0; windowEnd < n; windowEnd++)
        {
            map[s[windowEnd]]++;
            
            while(map[s[windowEnd]] > 1){
                
                map[s[windowStart]]--;
                
                windowStart++;
            }
            
            size = windowEnd - windowStart + 1;
            
            if(size > max) max = size;
        }
        
        return max;
        
    }
};