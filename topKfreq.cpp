class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int, int> myMap;
        unordered_multimap<int, int> myMap2;
        
        unordered_map<int, int> :: iterator itr;
        
        for(auto i : nums)
            myMap.insert(make_pair(i, 0));
            
        for(auto key : nums)
        {
            itr = myMap.find(key);
            itr -> second ++;
        }
        
        for(auto i : myMap)
            myMap2.insert(make_pair(i.second, i.first));

        
        vector<int> freq;
        
        for(auto i : myMap)
            freq.push_back(i.second);
        
        
        
        make_heap(freq.begin(), freq.end());
        
        vector<int> answer;
        
        for(int i = 0; i < k; i++)
        {
            itr = myMap2.find(freq.front());
            
            answer.push_back(itr -> second);
            
            myMap2.erase(itr);
            
            pop_heap(freq.begin(), freq.end());
            
            freq.pop_back();
        }
        
        return answer;
    }
};