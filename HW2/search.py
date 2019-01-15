# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # implement the depth first search algorithm with Stack
    # initialize the search tree using the initial state of problem
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    visited = []

    while not stack.isEmpty():
        # pop the top element in the stack
        state, actions = stack.pop()

        # if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(state):
            return actions

        # expand current node and push the successors in the stack
        if state not in visited:
            visited.append(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    stack.push((successor, actions + [action]))

    return False
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    # initialize the search tree using the initial state of problem
    queue = util.Queue()
    queue.push((problem.getStartState(), []))
    visited = []

    while not queue.isEmpty():
        # choose a leaf node for expansion
        state, actions = queue.pop()

        # if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(state):
            return actions

        # expand the node and add the resulting nodes to the search tree
        if state not in visited:
            visited.append(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    queue.push((successor, actions + [action]))
    return False

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # implement the uniform cost search algorithm with PriorityQueue
    # initialize the initial state
    # p_queue = util.PriorityQueue()
    # state = problem.getStartState()
    # path_cost = 0
    # p_queue.push((state, []), path_cost)
    # visited = []

    # print('=== Searching... ===')
    # while not p_queue.isEmpty():
    #     # choose the lowest cost node in the priority queue
    #     state, actions = p_queue.pop()

    #     # if the node contains a goal state then return the corresponding solution
    #     if problem.isGoalState(state):
    #         print('=== Find solution! ===')
    #         return actions

    #     # expand the node
    #     if state not in visited:
    #         # add current node in the visited[] array
    #         visited.append(state)
    #         for successor, action, stepCost in problem.getSuccessors(state):
    #             # if this successor has not been visited or is not in the priority queue, then insert this successor
    #             # if the successor is in the priority queue and has a higher path cost, then replace it
    #             # use the update function provided by priority queue
    #             p_queue.update((successor, actions + [action]), stepCost)

    # return False
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    #implement the a star algorithm
    # the initial state
    start_state = problem.getStartState()
    open_list = [] # contains lists [state, g_value, h_value, actions]
    close_list = []
    g_cost = 0

    # add the starting state into the open list
    open_list.append([start_state, 0, heuristic(start_state, problem), []])

    # h_value: heuristic function value
    # g_value: the cost taken for moving from starting state to current state
    # f_value = h_value + g_value
    while len(open_list):
        # find the element with min f_value in open list
        cur = open_list[0]
        min_f_value = cur[1] + cur[2]
        for temp in open_list:
            f_value = temp[1] + temp[2]
            if f_value < min_f_value:
                cur = temp
                min_f_value = f_value

        # check whether it is the goal state or not
        if problem.isGoalState(cur[0]):
            return cur[3] # return actions

        # move current state from open list to close list
        open_list.remove(cur)
        close_list.append(cur)

        g_value = cur[1]
        actions = cur[3]

        for successor, action, step_cost in problem.getSuccessors(cur[0]):
            # if the successor is in close list, then ignore it
            is_exist = False
            for temp in close_list:
                if temp[0] == successor:
                    is_exist = True
                    break
            if is_exist == False:
                # check whether open list contains successor and record the index
                index = -1
                for i in range(len(open_list)):
                    if open_list[i][0] == successor:
                        index = i
                        break
                # if it is not in the open list, add it into open list
                temp = [successor, g_value + step_cost, heuristic(successor, problem), actions + [action]]
                if index == -1:
                    open_list.append(temp)
                # if it is in the open list, check whether it is a better path by comparing with g_value
                # keep the better one in open list
                else:
                    if temp[1] < open_list[index][1]:
                        open_list[index] = temp

    return False
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
