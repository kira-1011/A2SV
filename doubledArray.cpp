class Solution {

public:
    vector<int> findOriginalArray(vector<int>& changed) {
        
        int n = changed.size();
        
        // cout << n << endl;
        
        vector<int> original;
        vector<int> empty;
        
        if(n == 1)
            return original;
        
        if(n % 2 != 0)
            return original;
        
        unordered_map <int, int> myMap;
        
        sort(changed.begin(), changed.end());
        
        for(auto i : changed)
            myMap[i]++;
        
        
        
        for(auto element : changed)
        {
            if(myMap[element] > 0)
            {
                myMap[element]--;
                
                if(myMap[element * 2] > 0)
                {
                    myMap[element * 2]--;
                    
                    original.push_back(element);
                }
            }
        }
        
        if(original.size() == (n / 2))
            return original;
       
        return empty;
    }
};