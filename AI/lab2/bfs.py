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
        print '------------------------------'
        print 'visited: {}'.format(visited_dict)
        print '------------------------------'

    if goal in visited_dict:
        one_up = goal
        path = [goal]
        while one_up != start:
            one_up = preds[one_up]
            path.append(one_up)
        print path
        return path
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

# next_level(APH3, active_nodes, visited_dict)
bfs(APH3, 'S', 'G')
