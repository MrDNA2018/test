# 1、单点按照距离递增辐射出去；
# 2、辐射到的点会被放进优先级队列，距离远的点可能会先放到队列里；
# 3、距离近的，可能会后放进队列，但是肯定会先出去；
# 4、每一个放进优先级队列的点，需要记录：自己，自己的前继节点，自己到起点的距离，会被用到的。
import heapq
import numpy as np


def dijkstra(graph, start):
    pqueue = []
    heapq.heappush(pqueue, (0.0, start))

    visit = set()
    parent = {start: None}
    distance = {vertex: np.Inf for vertex in graph}
    distance[start] = 0.0

    while pqueue:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        visit.add(vertex)

        edges = graph[vertex]
        for v in edges:
            if v not in visit:
                if dist + graph[vertex][v] < distance[v]:
                    heapq.heappush(pqueue, (dist + graph[vertex][v], v))
                    distance[v] = dist + graph[vertex][v]
                    parent[v] = vertex

    return parent, distance
#%%
def dijkstra2(graph, start):
    vnum = len(graph)
    pqueue = []
    heapq.heappush(pqueue, (0.0, None, start))
    paths = {vertex: None for vertex in graph}
    count = 0

    while count < vnum and pqueue:
        pair = heapq.heappop(pqueue)
        distance = pair[0]
        parent = pair[1]
        vertex = pair[2]
        if paths[vertex]:
            continue
        paths[vertex] = (parent, distance)
        edges = graph[vertex]
        for v in edges:
            if paths[v] is None:
                heapq.heappush(pqueue, (distance + graph[vertex][v], vertex, v))
        count += 1
    return paths
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
i,j=dijkstra(g,'A')