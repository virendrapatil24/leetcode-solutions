class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_cook = {supply: True for supply in supplies}
        recipes_graph = {}
        for i in range(len(recipes)):
            recipes_graph[recipes[i]] = ingredients[i]
    
        def dfs(recipe):
            if recipe in can_cook:
                return can_cook[recipe]
            if recipe not in recipes_graph:
                return False
            
            can_cook[recipe] = False
            for ingredient in recipes_graph[recipe]:
                if not dfs(ingredient):
                    return False
            
            can_cook[recipe] = True
            return True

        return [recipe for recipe in recipes if dfs(recipe)]
        
