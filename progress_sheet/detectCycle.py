from typing import List

class Solution:
    
    def hasCycle(self, v, adj, color, parent):
        
        if color[v] == 1:
            return True
        
        if color[v] == 2:
            return False
        
        color[v] = 1
        
        for next_v in adj[v]:
            
            if next_v == parent:
                continue
            
            if self.hasCycle(next_v, adj, color, v):
                return True
        
        color[v] = 2
        
        return False
        
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    color = [0] * V
		
		for i in range(V):
		    
	        if self.hasCycle(i, adj, color, -1):
	            return True
		  
		return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
