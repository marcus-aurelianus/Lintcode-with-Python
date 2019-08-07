class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def totalNQueens(self, n):
        result=[0]
        visited = {
            'col': set(),
            'sum': set(),
            'diff': set(),
        }
        self.dfs(n, [], visited, result)
        return result[0]
        
    def dfs(self, n, permutation, visited, boards):
        if n == len(permutation):
            boards[0]+=1
            return
        
        row = len(permutation)
        for col in range(n):
            if not self.is_valid(permutation, visited, col):
                continue
            permutation.append(col)
            visited['col'].add(col)
            visited['sum'].add(row + col)
            visited['diff'].add(row - col)
            self.dfs(n, permutation, visited, boards)
            visited['col'].remove(col)
            visited['sum'].remove(row + col)
            visited['diff'].remove(row - col)
            permutation.pop()

    # O(1)
    def is_valid(self, permutation, visited, col):
        row = len(permutation)
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if row - col in visited['diff']:
            return False
        return True
        
sol=Solution()
print(sol.totalNQueens(7))
