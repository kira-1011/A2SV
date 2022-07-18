class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        unordered_map<int, int> hashMap;
        unordered_map<int, int> :: iterator itr;
        vector<int> monotonicStack;
        vector<int> answer;
        
        for(int i = 0, n = nums2.size(); i < n;  i++)
            hashMap.insert(make_pair(nums2[i], i));
        
        int i = 0;
        
        itr = hashMap.find(nums1[i]);
        
        int j = itr -> second;
        
        int n = nums1.size();
        
        int n2 = nums2.size();
        
        monotonicStack.push_back(nums2[j]);
        
        j++;
        
        while(i < n)
        {
            if(j >= n2)
            {
                answer.push_back(-1);
                i++;
                
                if(i >= n)
                    break;
                
                itr = hashMap.find(nums1[i]);
                j = itr -> second;
                monotonicStack.push_back(nums2[j]);
                j++;
            }
            
            else if(nums2[j] > monotonicStack.back())
            {
                int popped = monotonicStack.back();
                
                monotonicStack.pop_back();
                
                if(popped == nums1[i])
                {
                    answer.push_back(nums2[j]);
                    i++;
                    
                    if(i >= n)
                        break;
                    
                    itr = hashMap.find(nums1[i]);
                    j = itr -> second;
                    monotonicStack.push_back(nums2[j]);
                    j++;
                }
            }
            else
            {
                monotonicStack.push_back(nums2[j]);
                j++;
            }
        }
        
        return answer;
    }
};