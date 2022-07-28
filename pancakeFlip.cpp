class Solution {

private:
    
    void swap(int *a, int *b)
    {
        int temp = *a;
        *a = *b;
        *b = temp;
    }
    
    void flip(vector<int> &arr, int end)
    {
        int p1 = 0, p2 = end;
        
        while(p1 < p2)
        {
            swap(&arr[p1], &arr[p2]);
            p1++;
            p2--;
        }
    }
    
    int findMax(vector<int> &arr, int i)
    {
        int max = i;
        
        for(int j = 0; j < i; j++)
        {
            if(arr[max] < arr[j])
                max = j;
        }
        
        return max;
    }

public:
    vector<int> pancakeSort(vector<int>& arr) {
        
        int n = arr.size();
        
        vector<int> kValues;
        
        int max = 0;
        
        if(n == 1)
            return kValues;
        
        for(int i = n - 1; i >= 0; i--)
        {
            max = i;
            
            //Find max value from 0 to i
            max = findMax(arr, i);
            
            //It means the number is in its correct place
            if(max == i)
                continue;
            
            kValues.push_back(max + 1);
            
            kValues.push_back(i + 1);
            
            flip(arr, max);
            
            flip(arr, i);
        }
        
        return kValues;
        
    }
};