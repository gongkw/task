import heapq

# graph ={"A":{"B":5},{"C",1},
#        "B":{"A":5},{"C":2},{"D":1},
#        "C":{"A":1},{"B":2},{"D":4},{"E":8},
#       "D":{"B":1},{"C":4},{"E":3},{"F":6},
#       "E":{"C":8},{"D":3},
#       "F" :{"D":6},
# }

def diksjia(graph, s):
    pqueue=[]
    heapq.heappush(pqueue,(0,s))
    seen=set()
    parent={s:None}
    distance={s:0}

    while (len(queue) > 0):
        pair = pqueue.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for node in nodes:
            if node not in seen:
                if dist + graph[vertex][node] < distance[node]:
                    pqueue.heappush(pqueue,(dist + graph[vertex][node], node))
                    parent[node] =vertex
                    distance[node] =  dist + graph[vertex][node]
        
        print vertex
    return parent

parent = BFS(graph,"E")

# v="B"

# while v != None:
#     print v
#     v = parent[v]

            

