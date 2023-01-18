# Computes weighted shortest paths.

import numpy as np
import sys

class minheap:
    def __init__(self):
        self.heap = []
        self.heap_len = 0
    
    def extractMin(self):
        Min = self.heap[0]
        self.heap_len -= 1
        self.heap[0] = self.heap[self.heap_len]
        del self.heap[self.heap_len]
        cur = 0
        while (cur*2 + 2 < self.heap_len and self.heap[cur*2 + 2][1] < self.heap[cur][1]) or ( cur*2 + 1 < self.heap_len and self.heap[cur*2 + 1][1] < self.heap[cur][1] ):
            if cur*2 + 2 < self.heap_len and self.heap[cur*2 + 1][1] > self.heap[cur*2 + 2][1]:
                self.heap[cur*2 + 2],self.heap[cur] = self.heap[cur],self.heap[cur*2 + 2]
                cur = cur*2 + 2
            else:
                self.heap[cur*2 + 1],self.heap[cur] = self.heap[cur],self.heap[cur*2 + 1]
                cur = cur*2 + 1
        return Min
        pass
    
    def insert(self,vertex):
        self.heap.append(vertex)
        cur  = self.heap_len
        self.heap_len += 1
        while (cur -1)//2 >= 0 and self.heap[cur][1] < self.heap[(cur -1)//2][1]:
            self.heap[cur], self.heap[(cur -1)//2] = self.heap[(cur -1)//2], self.heap[cur]
            cur = (cur -1)//2


class Vertex:
    def __init__(self, nm):
        self.name = nm    #  Vertex name
        self.adj =  dict()    #  Adjacent vertices
        self.prev = None    #  Previous vertex on shortest path
        self.dist = np.inf    #  Distance of path
        self.status = False

    def Vertex(self, nm):
        self.name = nm
        reset()

    def reset(self):
        self.dist = np.inf
        self.prev = None

class Graph:
    def __init__(self):
        self.vertexMap =  dict()

    def addedge(self, sourceName,  destName, distance):
        v = self.getVertex(sourceName)
        w = self.getVertex(destName)
        v.adj[destName] = [float(distance),True]
        w.adj[sourceName] = [float(distance),True]

    def addEdge(self, sourceName,  destName, distance):
        v = self.getVertex(sourceName)
        w = self.getVertex(destName)
        v.adj[destName] = [float(distance),True]

    def deleteEdge(self, sourceName,  destName):
        v = self.getVertex(sourceName)
        del v.adj[destName]
    
    def vertexUp(self, vertexName):
        v = self.getVertex(vertexName)
        v.status = True
    
    def vertexDown(self, vertexName):
        v = self.getVertex(vertexName)
        v.status = False

    def edgeUp(self, sourceName,  destName):
        v = self.getVertex(sourceName)
        v.adj[destName][1] = True

    def edgeDown(self, sourceName,  destName):
        v = self.getVertex(sourceName)
        v.adj[destName][1] = False

    def printPath(self, destName):
        w = self.vertexMap[destName]
        if w is None:
            print("Destination vertex not found")
        elif np.isinf(w.dist):
            print(destName + " is unreachable")
        else:
            self.printPath_(w)
            print("",round(w.dist,4), end ="")
        print()

 
    def  getVertex(self, vertexName):
        if vertexName not in self.vertexMap:
            v = Vertex(vertexName)
            v.status = True
            self.vertexMap[vertexName] = v
        v = self.vertexMap[vertexName]
        return  v

    def printPath_(self, dest):
        if dest.prev is not None:
            self.printPath_(dest.prev)
            print(" ", end ="")
        print(dest.name, end ="")

    def clearAll(self):
        for v in self.vertexMap.values():
            v.reset()

   
    def unweighted(self, startName):
        self.clearAll()
        start = self.vertexMap[startName]
        if start is None or not start.status:
            print("Start vertex not found")
        q = minheap()
        q.insert([start,0,None])
        while q.heap_len > 0:
            v = q.extractMin()
            if np.isinf(v[0].dist) or v[0].dist > v[1]:
                v[0].dist = v[1]
                v[0].prev = v[2]
                for w in v[0].adj.keys():
                    if self.vertexMap[w].status and v[0].adj[w][1]:
                        q.insert([self.vertexMap[w], v[0].dist + v[0].adj[w][0], v[0]])

    def processRequest(self,startName,destName):
        self.unweighted(startName)
        self.printPath(destName)
    
    def Print(self):
        for vertex in sorted(self.vertexMap.keys()):
            v = self.vertexMap[vertex]
            print(vertex +(''if v.status else ' DOWN'))
            for edge in sorted(v.adj.keys()):
                print("\t"+edge+" "+str(v.adj[edge][0]) +(''if v.adj[edge][1] else ' DOWN'))
    
    def reachable(self):
        for vertex in sorted(self.vertexMap.keys()):
            v = self.vertexMap[vertex]
            if v.status:
                print(vertex)
                visited = set()
                visited.add(vertex)
                q = []
                reachable = []
                for j in sorted(v.adj.keys()):
                    if v.adj[j][1] and self.vertexMap[j].status:
                        q.append(j)
                while len(q) > 0:
                    d = q.pop(0)
                    if d not in visited:
                        reachable.append(d)
                        visited.add(d)
                        d = self.vertexMap[d]
                        for j in sorted(d.adj.keys()):
                            if d.adj[j][1] and self.vertexMap[j].status:
                                q.append(j)
                for r in sorted(reachable):
                    print("\t"+r)

def main():
    g = Graph()
    fin = sys.argv[1]
    with open(fin) as f:
        lines = f.readlines()
    for line in lines:
        line = line.replace("\n","").strip().split(" ")
        if (len(line) != 3):
            print("Skipping ill-formatted line " + line)
            continue
        source = line[0]
        dest = line[1]
        dist = line[2]
        g.addedge(source, dest,dist)
    fin = sys.argv[2]
    with open(fin) as f:
        lines = f.readlines()
    for line in lines:
        args = line.replace("\n","").split(" ")
        if args[0] == "print":
            g.Print()
            print()
        elif args[0] == "path":
            g.processRequest(args[1],args[2])
            print()
        elif args[0] == "edgedown":
            g.edgeDown(args[1],args[2])
        elif args[0] == "vertexdown":
            g.vertexDown(args[1])
        elif args[0] == "reachable":
            g.reachable()
            print()
        elif args[0] == "edgeup":
            g.edgeUp(args[1],args[2])
        elif args[0] == "vertexup":
            g.vertexUp(args[1])
        elif args[0] == "deleteedge":
            g.deleteEdge(args[1],args[2])
        elif args[0] == "addedge":
            g.addEdge(args[1],args[2],args[3])
        elif args[0] == "Quit":
            break

if __name__=="__main__":
    main()
