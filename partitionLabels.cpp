class Solution {
public:
    vector<int> partitionLabels(string s) {
        
        int n = s.length(), p1 = 0, p2 = 0, len = 0;
    
        unordered_map<char, int> umap;

        vector<int> partitions;

        for(int i = 0; i < n; i++)
            umap[s[i]] = i;

        p2 = umap[s[p1]];

        len = p2 + 1;

        while(p2 < n)
        {
            if(p1 == p2) //Check if we have found a partition
            {
                partitions.push_back(len);

                if(p1 + 1 < n)
                {
                    int next = umap[s[p1 + 1]];
                    
                    len = next - p2;

                    p2 = next;
                }
                else
                    break;
            }
            else if(umap[s[p1]] > p2) //Check if there is a greater recent version index than the current recent version index
            {
                int recent = umap[s[p1]];
                
                len += (recent - p2);

                p2 = recent;
            }
            p1++;
        }

        return partitions;
    }
};