from collections import defaultdict

# define graph
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    #recursive to go to the most left
    def DFSrecur(self,v,explored,filepath):
        #add to explored dictionary then print
        explored[v] = True
        f = open(filepath,"a")
        f.write(str(v) + " ")
        f.close()
        
        for vertex in self.graph[v]:
            if not explored.get(vertex):
                self.DFSrecur(vertex,explored,filepath)

    # function to be implemented
    def DFS(self, s, filepath):
        '''
        TODO: print the vertices in the order of traversal 
        '''
        #explored is a dictionary to help find a value in O(1)
        explored = {}
        
        self.DFSrecur(s,explored,filepath)

                
# Driver code
# Create a graph given in the above diagram
g = Graph()

# Read from input file
f = open("input.txt", "r")
for line in f:
    u, v = [int(it) for it in line.strip().split(' ')]
    g.addEdge(u,v)
f.close()

g.DFS(0,"output.txt")


#nguồn tham khảo : https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/