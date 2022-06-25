class Solution {
public:
    void sortColors(vector<int>& nums) {
       
        if(nums.empty()){
            return;
        }
        
        sortClr(nums, 0, nums.size() - 1);
    }
    
private:
    
    vector<int> leftNums;
    vector<int> rightNums;
    
    void mergeColors(vector<int>& nums, int start, int mid, int end){
        
        leftNums.clear();
        rightNums.clear();
        
        
        int left = 0;
        int right = 0;
        int k = start;
        
        int leftLen = mid - start + 1;
        int rightLen = end - mid;
        
        for(int i = 0; i < leftLen; i++)
            leftNums.push_back(nums[start + i]);
        
        for(int j = 0; j < rightLen; j++)
            rightNums.push_back(nums[mid + j + 1]);
        
        while((left < leftLen) && (right < rightLen))
        {
            
            if(leftNums[left] <= rightNums[right])
            {
                nums[k] = leftNums[left];
                left++;
            }
            
            else
            {
                nums[k] = rightNums[right];
                right++;
            }
            
            k++;
        }
        
        while(left < leftLen){
            nums[k] = leftNums[left];
            left++;
            k++;
        }
        
         while(right < rightLen){
            nums[k] = rightNums[right];
            right++;
            k++;
        }
        
    }
    
    void sortClr(vector<int>& nums, int start, int end){
        
        if(start >= end)
            return;
        
        int mid = (start + end) / 2;
        
        sortClr(nums, start, mid);
        
        sortClr(nums, mid + 1, end);
        
        mergeColors(nums, start, mid, end);
    }
};