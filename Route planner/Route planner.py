import math
from queue import PriorityQueue

#I used the idea in here- https://dbader.org/blog/priority-queues-in-python
#let the initial point be x
#let the destination point be y

@doc module 'shortest_path'

def shortest_path(graph, x, y):
    
    pathQueue = PriorityQueue()
    pathQueue.put(start, 0)
    
    prev = {x: None}
    score = {x: 0}

    while not pathQueue.empty():
        curr = pathQueue.get()

        if curr == y:
            generatePath(prev, x, y)

        for node in graph.roads[curr]:
            updateScore = score[curr] + heuristicMeasure(graph.intersections[curr], graph.intersections[node])
            
            if node not in score or updateScore < score[node]:
                score[node] = updateScore
                totalScore = updateScore + heuristicMeasure(graph.intersections[curr], graph.intersections[node])
                pathQueue.put(node, totalScore)
                prev[node] = curr

    return generatePath(prev, x, y)


#return the distance from x to y i.e., finding the displacement of the distance.

#distance's heuristic search algorithm

def heuristicMeasure(x, y):
    return math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))

@doc module 'generatePath'
def generatePath(prev, x, y):
    curr = goal
    path = [curr]
    while curr != x:
        curr = prev[curr]
        path.append(curr)
    path.reverse()
    return path