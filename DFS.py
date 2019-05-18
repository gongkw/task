graph ={"A":["B","C","D"],
       "B":["C","D"],
       "C":["D","E","A"],
      "D":["A","B","C"],
      "E":["A","B","C","D","E"]       
}

def DFS(graph, s):
    stack=[]
    seen=set()
    seen.add(s)
    stack.append(s)
    parent={s:None}
    while (len(stack) > 0):
        vertex = stack.pop()
        for node in graph[vertex]:
            if node not in seen:
                stack.append(node)
                seen.add(node)
                parent[node] = vertex
        # print vertex
    return parent

parent=DFS(graph,"E")
v="B"

while v != None:
    print v
    v= parent[v]
            

