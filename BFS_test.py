graph ={"A":["B","C","D"],
       "B":["C","D"],
       "C":["D","E","A"],
      "D":["A","B","C"],
      "E":["A","B","C","D","E"]       
}


def BFS(graph, s):
    seen=set()
    parents={s:None}
    queue=[]
    seen.add(s)
    queue.append(s)
    while queue:
        print queue
        vertex = queue.pop(0)
        for node in graph[vertex]:
            if node in seen:
                pass
            else:
                queue.append(node)
                parents[node] =vertex
                seen.add(node)
        
            print vertex, parents[vertex]
    print parents
BFS(graph,"A")

