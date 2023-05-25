class UnionFind:

    def __init__(self, size):
        self.parent = {i : i for i in range(size)}
        self.rank = {i : 0 for i in range(size)}

    def find(self, node):
        
        # Applying path comprehension to optimize quick find
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]
    
    def union(self, node1, node2):
        
        # Union by rank(rank)
        node1_rep = self.find(node1)
        node2_rep = self.find(node2)

        if node1_rep == node2_rep:
            return False

        if self.rank[node1_rep] > self.rank[node2_rep]:
            self.parent[node2_rep] = node1_rep
        
        elif self.rank[node1_rep] < self.rank[node2_rep]:
            self.parent[node1_rep] = node2_rep

        else:
            self.parent[node2_rep] = node1_rep
            self.rank[node1_rep] += 1

        return True
    
    def isConnected(self, email1, email2):
        return self.find(email1) == self.find(email2)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        union_find = UnionFind(len(accounts))
        merged_acc = []
        temp_acc = defaultdict(list)
        owners = dict()

        # connect the accounts that belong to a single person
        for i in range(len(accounts)):
            account = accounts[i]

            for j in range(1, len(account)):

                email = account[j]

                if email not in owners.keys():
                    owners[email] = i

                else:
                    union_find.union(i, owners[email])

        # merge accounts having common emails
        for email, account in owners.items():
            owner_acc = union_find.find(account)
            temp_acc[owner_acc].append(email)

        for key, value in temp_acc.items():

            merged = [accounts[key][0]]

            merged.extend(sorted(value))

            merged_acc.append(merged)
        
        return merged_acc
                


        
