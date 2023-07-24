def find_lowest_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
            lowest_cost = cost

    return lowest_cost_node


def dijkstra():
    node = find_lowest_node(costs)                      #finding the lowest cost node

    while node is not None:                             #while there is a lowest cost node
        cost = costs[node]                              #taking the current cost of travelling to the node
        neighbors = graph[node]                         #taking neighbors of the current node

        for neighbor in neighbors.keys():               #looping through neighbors.keys to check the cost of travelling with current path
            new_cost = cost + neighbors[neighbor]       #new_cost = current_cost_of_path + cost_to_this_node

            if new_cost < costs[neighbor]:              #if new_cost is smaller than the current cost we have to change the cost in the costs dictionary and change it to new_cost, also we have to change the parent of the current neighbor because we found a faster way, we change it to the node
                costs[neighbor] = new_cost              #changing cost in the costs dictionary
                parents[neighbor] = node                #changing the parent of the neighbor to node
        
        processed.append(node)                          #appending already checked node
        node = find_lowest_node(costs)                  #looking for next lowest node

    return costs["meta"] 

def way(last_point):
    way_from_start_to_meta = [last_point]
    CHANGE = True

    while CHANGE:                                       #until there is a change in the list
        CHANGE = False        
        for x in parents:                               #looping  throught keys of the parents hash table
            if way_from_start_to_meta[-1] == x:         #if key x is equals to last element added to list append new value from this key x to the list
                way_from_start_to_meta.append(parents[x])
                CHANGE = True
        
    return way_from_start_to_meta[::-1]                 #return reversed list 

        
        

processed = []                                          #list with already checked nodes

#implementation the graph
graph = {}                                              #main graph

graph["start"] = {}
graph["start"]["B"] = 5                                 #way from start to B costs 5
graph["start"]["C"] = 2                                 #way from start to C costs 2

graph["B"] = {} 
graph["B"]["C"] = 1                                     #way from B to C costs 1
graph["B"]["meta"] = 3                                  #way from B to meta costs 3

graph["C"] = {}
graph["C"]["meta"] = 4                                  #way from C to meta costs 5

graph["meta"] = {}                                      #node "meta" is last so there is no more nodes

#costs only from start to another node
costs = {}
costs["B"] = 1                                          #from start to B, cost = 1
costs["C"] = 2                                          #from start to C, cost = 2
costs["meta"] = float("inf")                            #unknown at the begginning, so declaring infinity

#parents of the all nodes key = child, value = parent
parents = {}
parents["B"] = "start"                                  #at the begginning the parent of the B is start
parents["C"] = "start"                                  #at the begginning the parent of the C is start
parents["meta"] = None                                  #at the begginning the parent of the meta is unknown

print("The cost of the fastest way: ", dijkstra())              #main function dijkstra algorithm
print("The fastest way from start to meta: ", way("meta"))      #finding the whole path from start to meta
print("The fastest way from start to B: ", way("B"))            #finding the whole path from start to B  
print("The fastest way from start to C: ", way("C"))            #finding the whole path from start to C

