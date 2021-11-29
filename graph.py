from queue import PriorityQueue


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def dijkstra(self, start):
        visited = []
        max_value = 10 ** 6
        distance = {k: max_value for k in self.vertList.keys()}
        distance[start] = 0
        distance_copy = {key: value for key, value in distance.items()}

        while self.vertList[start].connectedTo:
            visited.append(start)
            for vert in self.vertList[start].connectedTo.keys():
                vert = vert.getId()
                if vert not in visited:
                    if self.vertList[start].getWeight(self.vertList[vert]) + distance[start] < distance[vert] \
                            or max_value + distance[start] < distance[vert]:
                        distance[vert] = self.vertList[start].getWeight(
                            self.vertList[vert]) + distance[start]

            distance_copy = {key: value for key,
                             value in distance.items() if key not in visited}
            if distance_copy:
                start = min(distance_copy, key=distance.get)
        return distance, visited
