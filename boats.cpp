class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
        int n = people.size(), p1 = 0, p2 = n - 1, sum = 0, boats = 0;
        
        sort(people.begin(), people.end(), greater<int>());
        
        while(p1 <= p2)
        {
            sum = people[p1] + people[p2];
            
            if(sum <= limit)
            {
                boats++;
                p1++;
                p2--;
            }
            else if(sum > limit)
            {
                boats++;
                p1++;
            }
        }
        
        return boats;
       
    }
};