from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns

        # trivial cases
        if m == 1: # single row
            return matrix[0]
        elif n == 1: # single column
            result = []
            for i in range(m):
                result.append(matrix[i][0])
            return result

        visited = [[False] * n for _ in range(m)] # keeps track of it a cell has been visited
        result = []
        i = 0
        j = 0
        # If we cannot go in a certain direction, then we're done
        while True:
            # Go all the way right until we either reach the boundary or reach a visited cell
            while j < n and not visited[i][j]:
                result.append(matrix[i][j])
                visited[i][j] = True
                j += 1
            j -= 1
            i += 1
            if visited[i][j]:
                break

            # Go all the way down until we either reach the boundary or reach a visited cell
            while i < m and not visited[i][j]:
                result.append(matrix[i][j])
                visited[i][j] = True
                i += 1
            i -= 1
            j -= 1
            if visited[i][j]:
                break

            # Go all the way left until we either reach the boundary or reach a visited cell
            while j >= 0 and not visited[i][j]:
                result.append(matrix[i][j])
                visited[i][j] = True
                j -= 1
            j += 1
            i -= 1
            if visited[i][j]:
                break

            # Go all the way up until we either reach the boundary or reach a visited cell
            while i >= 0 and not visited[i][j]:
                result.append(matrix[i][j])
                visited[i][j] = True
                i -= 1
            i += 1
            j += 1
            if visited[i][j]:
                break
                
        return result