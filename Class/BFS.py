class Node:
    def __init__(self,state,parent,action):
        self.state=state
        self.parent=parent
        self.action=action

def actionSequence(graph,goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while(currentParent!=None):
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return  solution

def BFS():
    initialState = 'Baltimore'
    goalState = 'Bakersfield'

    graph = {
        'Baltimore': Node('Baltimore', None, ['Chicago', 'Atlanta']),
        'Denver': Node('Denver', None, ['Chicago', 'Atlanta','Bakersfield']),
        'Dallas': Node('Dallas', None, ['Chicago', 'Atlanta','Bakersfield']),
        'Atlanta': Node('Atlanta', None, ['Baltimore', 'Denver', 'Dallas', 'Chicago']),
        'Chicago':Node('Chicago', None, ['Baltimore', 'Denver', 'Dallas', 'Atlanta']),
        'Bakersfield': Node('Bakersfield', None, ['Denver', 'Dallas']), 
    }

    frontier =[initialState]
    explored =[]

    while(len(frontier)!=0):
        currentNode = frontier.pop()

        explored.append(currentNode)

        for child in graph[currentNode].action:
            if child not in frontier and child not in explored:
                graph[child].parent=currentNode

                if graph[child].state == goalState:
                    return actionSequence(graph, goalState)

                frontier.append(child)

print(BFS())
