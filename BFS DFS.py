class Solution:
    def bfsOfGraph(self, V, adj):
           queue = [0]
           visited = [0]     
           while queue:
               popVertex = queue.pop(0)
               for neighbour in adj[popVertex]:
                   if neighbour not in visited:
                       queue.append(neighbour)
                       visited.append(neighbour)
           return visited

      
    def dfsOfGraph(self, V, adj):
        ans=[]
        visited=dict()
        def dfs(node):
            visited[node]=1
            ans.append(node)
            for node in adj[node]:
                if node not in visited:
                    dfs(node) 
        dfs(0)
        return ans
