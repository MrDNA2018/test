import heapq


def kruskal2(graph):
    vnum = len(graph)
    pqueue = []
    for head in graph:
        for tail in graph[head].keys():
            heapq.heappush(pqueue, (graph[head][tail], head, tail))

    reps = {vertex: vertex for vertex in graph}
    mst = {vertex: None for vertex in graph}
    count = 0

    while count < vnum and pqueue:
        pair = heapq.heappop(pqueue)
        weight = pair[0]
        head = pair[1]
        tail = pair[2]

        if reps[head] == reps[tail]:
            continue

        mst[tail] = (head, weight)

        for v in graph:
            if reps[v] == reps[tail]:
                reps[v] = reps[head]
        count += 1
    return mst
#%%
 #%%
g = {'A':{'B':1,'C':2},
     'B':{'A':1,'C':3,'D':4},
     'C':{'A':2,'B':3,'D':5,'E':6},
     'D':{'B':4,'C':5,'E':7,'F':8},
     'E':{'C':6,'D':7,'G':9},
     'F':{'D':8},
     'G':{'E':9}
    }


