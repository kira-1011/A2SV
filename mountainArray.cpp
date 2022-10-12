class Solution {
public:
    int longestMountain(vector<int>& arr) {
        
        int i = 1, left = i, right = i, n = arr.size(), max = 0;
        
        if(n < 3)
            return 0;
        
        if(arr[i - 1] < arr[i])
            left = 0;
        
        while(right < n - 1 && (arr[right + 1] < arr[right])) right++;
        
        while(i < n)
        {   
            if(arr[i - 1] >= arr[i]) left = i;
            
            if(right < i) right = i;
            
            while(right < n - 1 && arr[right + 1] < arr[right]) right++;
            
            if((left != i && right != i) && (max < (right - left + 1))) max = right - left + 1;
            
            i++;
        }
        
        return max;
    }
};