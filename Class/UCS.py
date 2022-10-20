import math
from platform import node


def findMin(frontier):
    minV = math.inf
    node = ''
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node


def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution, graph[goalState].totalCost


class Node:

    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost


def UCS():
    intitalState = 'Baltimore'
    goalState = 'Bakersfield'

    graph = {
        'Chicago': Node('Chicago', None, [('Baltimore', 15), ('Denver', 18),('Dallas', 18),('Atlanta', 14)], 0),
        'Dallas': Node('Dallas', None, [('Chicago', 18), ('Atlanta', 15),('Bakersfield', 25)], 0),
        'Atlanta': Node('Atlanta', None, [('Baltimore', 14), ('Denver', 24),('Dallas', 15),('Chicago', 14)], 0),
        'Baltimore': Node('Baltimore', None, [('Chicago', 15), ('Atlanta', 14)], 0),
        'Bakersfield': Node('Bakersfield', None, [('Denver', 19), ('Dallas', 25)], 0),
        'Denver': Node('Denver', None, [('Chicago', 18), ('Atlanta', 24),('Bakersfield', 19)], 0),
        
    }

    frontier = dict()
    frontier[intitalState] = (None, 0)
    explored = []

    while (len(frontier) != 0):
        currentNode = findMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, intitalState, goalState)

        explored.append(currentNode)
        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost

            if child[0] not in frontier and child[0] not in explored:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent,
                                      graph[child[0]].totalCost)

            elif child[0] in frontier:
                if frontier[child[0]][1] < currentCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]

                else:
                    frontier[child[0]] = (currentNode, currentCost)
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]


print(UCS())
