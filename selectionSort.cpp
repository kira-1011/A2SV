class Solution
{
    public:
    int select(int arr[], int i)
    {
        // code here such that selectionSort() sorts arr[]
        return 0;
    }
     
    void selectionSort(int arr[], int n)
    {
       //code here
       int min = 0;
       
       for(int i = 0; i < n; i++)
       {
           min = i;
           
           for(int j = i + 1; j < n; j++)
           {
               if(arr[min] > arr[j])
                    min = j;
           }
           
           swap(arr[min], arr[i]);
       }
       
    }
};