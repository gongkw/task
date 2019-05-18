graph ={"A":{"B":5},{"C",1},
       "B":{"A":5},{"C":2},{"D":1},
       "C":{"A":1},{"B":2},{"D":4},{"E":8},
      "D":{"B":1},{"C":4},{"E":3},{"F":6},
      "E":{"C":8},{"D":3},
      "F" :{"D":6}   
}


import heapq
def diksjia(graph,s):
    pqueue=[]
    heapq.heappush(pqueue,(0,s))
    seen=set()
    parents={s:None}
    distance={s:0}

    while pqueue:
        pair = pqueue.heappop(pqueue)
        vertex=pair[1]
        distance=pair[0]
        nodes = graph[s].keys()
        for node in nodes:
            if node in seen:
                pass
            else:
                if dist + graph[vertex][node] < distance[node]
