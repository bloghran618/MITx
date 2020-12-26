# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

from search import *
APH3 = Graph(edgesdict=[
        {NAME: 'e1', VAL: 6, NODE1:'S', NODE2:'B' },
        {NAME: 'e2', VAL:10, NODE1:'S', NODE2:'A' },
        {NAME: 'e3', VAL:10, NODE1:'A', NODE2:'B' },
        {NAME: 'e4', VAL: 7, NODE1:'B', NODE2:'C' },
        {NAME: 'e5', VAL: 4, NODE1:'A', NODE2:'D' },
        {NAME: 'e6', VAL: 2, NODE1:'C', NODE2:'D' },
        {NAME: 'e7', VAL: 6, NODE1:'C', NODE2:'G' },
        {NAME: 'e8', VAL: 8, NODE1:'G', NODE2:'D' } ],
               heuristic={'G':{"S":0,"A":2,"B":5,"C":6,"D":5}})

def bfs(graph, start, goal):
    visited_dict = {}
    visited_dict[start] = 0
    active = [start]
    this_level = [start]
    preds = {}

    while goal not in this_level:
        this_level, visited_dict, preds = next_level(graph, this_level, visited_dict, preds)

    if goal in visited_dict:
        one_up = goal
        path = [goal]
        while one_up != start:
            one_up = preds[one_up]
            path.append(one_up)
        return list(reversed(path))
    else:
        return []

def next_level(graph, active_nodes, visited_dict, predecessors):
    next_level_nodes = []
    for beg_node in active_nodes:
        for connected_node in graph.get_connected_nodes(beg_node):
            connected_node_length = visited_dict[beg_node] + graph.get_edge(beg_node, connected_node).length
            # print 'length from {} to {} is {}'.format(beg_node, connected_node, connected_node_length)
            if connected_node not in visited_dict:
                # print '{} connected to {}'.format(connected_node, beg_node)
                next_level_nodes.append(connected_node)
                visited_dict[connected_node] = connected_node_length
                predecessors[connected_node] = beg_node
            elif connected_node_length < visited_dict[connected_node]:
                # print 'length {] < {}'.format(connected_node_length, visited_dict[connected_node])
                visited_dict[connected_node] = connected_node_length
                predecessors[connected_node] = beg_node
    # print visited_dict
    # print next_level_nodes
    return (next_level_nodes, visited_dict, predecessors)

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    raise NotImplementedError


## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    raise NotImplementedError

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
