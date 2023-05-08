class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        possible_recipes = []

        # build a graph that shows the ingredients needed to make a recipe
        graph = defaultdict(list)
        incoming_edges = defaultdict(int)

        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):

                graph[ingredients[i][j]].append(recipes[i])
                incoming_edges[recipes[i]] += 1
        
        # apply khan's algorithm to check the recipes we can make using topological sorting

        # start with the ingeredients we have initially
        queue = deque(supplies)

        while queue:
            
            ingredient = queue.popleft()

            if ingredient in recipes:
                possible_recipes.append(ingredient)

            for neghibour in graph[ingredient]:

                incoming_edges[neghibour] -= 1

                if incoming_edges[neghibour] == 0:
                    queue.append(neghibour)
        
        return possible_recipes
