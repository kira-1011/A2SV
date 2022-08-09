class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        
        unordered_map<int, int> map;
        
        int size = 0, max = 0;
        
        for(int windowStart = 0, windowEnd = 0, n = fruits.size(); windowEnd < n; windowEnd++)
        {
            map[fruits[windowEnd]]++;
            
            while(map.size() > 2)
            {
                map[fruits[windowStart]]--;
                
                if(map[fruits[windowStart]] == 0)  map.erase(fruits[windowStart]);
                
                windowStart++;
            }
            
            size = windowEnd - windowStart + 1;
            
            if(size > max) max = size;
        }
        
        return max;
    }
};