import math
import heapq

def find_distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def shortest_path(M,start,goal):
	# length of Map
	length = len(M.roads)
    
	# Initialise all the explored intersections to False
	explored = [ False for _ in range(length)]
    #Initialise heuristic value to 0 for all intersections
	h_values = [0]*length
    
    #Find heuristic value for each intersection
	for index in range(length):
		h_values[index] = find_distance( M.intersections[index][0],  M.intersections[index][1],
			M.intersections[goal][0], M.intersections[goal][1])

	frontier_heap = [(0, [start])]

	while len(frontier_heap) > 0:
		total_cost, path = heapq.heappop(frontier_heap)
		curr_intersection = path[-1]
        # Path Cost of current intersection without heuristic value
		total_path_cost = total_cost - h_values[curr_intersection]

        # If cuurent intersection is the final goal
		if goal == curr_intersection:
			return path

		for intersection in M.roads[curr_intersection]:

            # If neghbour intersection is not explored yet
			if(explored[intersection] is False):
                
				path_cost = find_distance(M.intersections[curr_intersection][0], M.intersections[curr_intersection][1],
					M.intersections[intersection][0], M.intersections[intersection][1])

				# total cost(f) =  g(total path cost) + h(heuristic distance)
				f_cost = total_path_cost + path_cost + h_values[intersection]
                # Create copy of path list
				curr_path = list(path)
				curr_path.append(intersection)
				heapq.heappush(frontier_heap, (f_cost, curr_path))

		explored[curr_intersection] = True
	
	return None