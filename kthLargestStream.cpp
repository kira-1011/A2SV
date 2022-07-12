class KthLargest {
private:
    
    vector<int> nums;
    int k;
    
    static bool comp(const long& a,const long& b){ 
        return a>b; 
    }
    
public:
    KthLargest(int k, vector<int>& nums) {
        
        this -> nums = nums;
        
        this -> k = k;
        
        make_heap(this -> nums.begin(), this -> nums.end(), comp);
        
    }
    
    int add(int val) 
    {   
        nums.push_back(val);
        
        push_heap(nums.begin(), nums.end(), comp);
        
        while(nums.size() != k)
        {
            pop_heap(nums.begin(), nums.end(), comp);
            
            nums.pop_back();
        }
        
        return nums.front();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */