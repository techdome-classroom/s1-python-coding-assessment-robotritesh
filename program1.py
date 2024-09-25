class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 'W':
                return
            
            
            grid[r][c] = 'W'
            
            
            dfs(r - 1, c)  
            dfs(r + 1, c)  
            dfs(r, c - 1)  
            dfs(r, c + 1)  
        
        
        num_islands = 0
        
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'L':
                    
                    dfs(r, c)
                    num_islands += 1  
        
        return num_islands

