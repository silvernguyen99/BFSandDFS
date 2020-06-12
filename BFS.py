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

    # function to be implemented
    def BFS(self, s, filepath):
        '''
        TODO: print the vertices in the order of traversal 
        '''

        #explored is a dictionary to help find a value in O(1)
        explored = {}
        #FiFo queue
        frontier = []
        # explored the first element
        frontier.append(s)
        explored[s] = True

        #open filepath to write
        f = open(filepath,"w")
        while frontier:

            #dequeue the frontier and write the vertex to the filpath
            s = frontier.pop(0)
            f.write(str(s) + " ")
            # go to all successors of s
            # check if any successors is not explored 
            # then add it to explored
            for vertex in self.graph[s]:
                if not explored.get(vertex):
                    frontier.append(vertex)
                    explored[vertex] = True

        #close filepath
        f.close()

    #hàm này phục vụ cho việc test
    #def printPraph(self):
        #print(self.graph)


# Driver code
# Create a graph given in the above diagram
g = Graph()

# Read from input file
f = open("test4.txt", "r")
for line in f:
    u, v = [int(it) for it in line.strip().split(' ')]
    g.addEdge(u,v)
f.close()

#g.printPraph()
g.BFS(0,"output.txt")
