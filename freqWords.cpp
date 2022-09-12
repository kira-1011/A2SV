class Solution {
private:
    
    static bool comp(vector<string>& a, vector<string>& b)
    {
        if(stoi(a[1]) == stoi(b[1]))
        {
            return (a[0].compare(b[0]) < 0);
        }
        
        return stoi(a[1]) > stoi(b[1]);
    }
    
    static bool comp1(vector<string>& a, vector<string>& b)
    {
        if(stoi(a[1]) == stoi(b[1]))
        {
            return (a[0].compare(b[0]) > 0);
        }
        
        return stoi(a[1]) < stoi(b[1]);
    }

public:
    
    vector<string> topKFrequent(vector<string>& words, int k) {
        
        vector<vector<string>> heap;
        
        unordered_map<string ,int> umap;
        
        int n = words.size(), j = 0;
        
        make_heap(heap.begin(), heap.end(), comp);
        
        for(int i = 0; i < n; i++)
            umap[words[i]]++;

        
        auto i = umap.begin();
        
        while(heap.size() != k)
        { 
            heap.push_back({i -> first, to_string(i -> second)});
            push_heap(heap.begin(), heap.end(), comp);
            
            i++;
        }
        
        
        while(i != umap.end())
        {
            
           if(i -> second > stoi(heap.front()[1]))
            {
                pop_heap(heap.begin(), heap.end(), comp);
                heap.pop_back();
                heap.push_back({i -> first, to_string(i -> second)});
                push_heap(heap.begin(), heap.end(), comp);
            }
            
            else if(i -> second == stoi(heap.front()[1]))
            {
                bool lexographicOrder = ((i -> first).compare(heap.front()[0])) < 0;
         
                if(lexographicOrder)
                {
                    pop_heap(heap.begin(), heap.end(), comp);
                    heap.pop_back();
                    heap.push_back({i -> first, to_string(i -> second)});
                    push_heap(heap.begin(), heap.end(), comp);
                }
            }
            
            i++;
        }
        
        sort(heap.begin(), heap.end(), comp1);
        
        vector<string> frequentElements;
        
        for(int i = 0; i < k; i++)
        {
            frequentElements.push_back(heap.back()[0]);
            heap.pop_back();
        }
        

        return frequentElements;
    }
};