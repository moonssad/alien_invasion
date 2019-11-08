def graph_gen():
    hash = {}
    hash['start'] = {}
    hash['start']['a'] = 6
    hash['start']['b'] = 2
    hash['a'] = {}
    hash['a']['end'] = 1
    hash['b'] = {}
    hash['b']['a'] = 3
    hash['b']['end'] = 5
    hash['end'] = {}
    return hash


# 保存源点到各个可直达的顶点的最短距离
def coast_gen():
    inifity = float('inf')  # 正负无穷
    coasts = {}
    coasts['a'] = 6
    coasts['b'] = 2
    coasts['end'] = inifity
    return coasts

# 保存路径
def parent_gen():
    parent = {}
    parent['a'] = 'start'
    parent['b'] = 'start'
    parent['end'] = None
    return parent

# 寻找最低消耗节点
def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_node = None
    for key in costs.keys():
        if key not in processed and lowest_cost > costs[key]:
                lowest_cost = costs[key]
                lowest_node = key
    print(lowest_node)
    return lowest_node


def Dijkstra(graph, costs, relation):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                relation[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return relation


def output(realtion):
    begin = relation['end']
    str_ = 'end--'
    while begin is not None:
        for key, value in relation.items():
            if key == begin:
                str_ += begin + '__'
                begin = value
                break
        else:
            begin = None
    print(str_ + 'start')


relation = Dijkstra(graph_gen(), coast_gen(), parent_gen())
output(relation)

