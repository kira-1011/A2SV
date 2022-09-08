class Solution {
private:
    static bool comp(vector<int>& a, vector<int>& b)
    {
        return a[1] > b[1];
    }
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        vector<vector<int>> heap;
        
        unordered_map<int ,int> umap;
        
        int n = nums.size();
        
        make_heap(heap.begin(), heap.end(), comp);
        
        for(int i = 0; i < n; i++)
            umap[nums[i]]++;
        
        auto i = umap.begin();
        n = k;
        
        while(n > 0)
        { 
            heap.push_back({i -> first, i -> second});
            push_heap(heap.begin(), heap.end(), comp);
            i++;
            n--;
        }
        
        while(i != umap.end())
        {
           if(i -> second > heap.front()[1])
            {
                pop_heap(heap.begin(), heap.end(), comp);
                heap.pop_back();
                heap.push_back({i -> first, i -> second});
                push_heap(heap.begin(), heap.end(), comp);
            }
            
            i++;
        }
        
        vector<int> frequentElements;
        
        for(int i = 0; i < k; i++)
           frequentElements.push_back(heap[i][0]);
        
 

        return frequentElements;
    }
};