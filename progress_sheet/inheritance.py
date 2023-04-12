class ThroneInheritance:

    def __init__(self, kingName: str):

        self.inheritance = defaultdict(list)

        self.dead = defaultdict(str)

        self.kingName = kingName

        self.dead[kingName] = 'G'
    
    def dfs(self, curr_child, order):

        # append only if it's alive
        if self.dead[curr_child] == 'G':
            order.append(curr_child)

        for child in self.inheritance[curr_child]:
            self.dfs(child, order)

    def birth(self, parentName: str, childName: str) -> None:

        # G is for alive and R is for dead
        self.inheritance[parentName].append(childName)
        self.dead[childName] = 'G'

    def death(self, name: str) -> None:
        self.dead[name] = 'R'

    def getInheritanceOrder(self) -> List[str]:
        
        # apply dfs to get the order
        order = []

        self.dfs(self.kingName, order)

        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
