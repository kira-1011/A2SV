class Solution {
private:
    int indexOf(vector<int> nums, int num){
        auto it = find(nums.begin(), nums.end(), num);
        
        if (it != nums.end()) 
        {
            int index = it - nums.begin();
            return index;
        }
        
        return -1;
        
    }
    
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> nextGreaterElements;
        bool found = false;
        
        for(int i = 0, n = nums1.size(), index; i < n; i++){
            index = indexOf(nums2,nums1[i]);
            found = false;
            for(int j = index + 1, n = nums2.size(); j < n; j++ ){
                 if(nums2[index] < nums2[j]){
                     nextGreaterElements.push_back(nums2[j]);
                     found = true;
                     break;
                 }
            }
            
            if(!found)
                nextGreaterElements.push_back(-1);
            
        }
        
        return nextGreaterElements;
        
    }
};
