import sorting as problem
import utils
import ucs
import time

point_time = time.process_time()
goal_node, n_visits = ucs.uniform_cost_graph_search(problem)
if goal_node is not None:
    print("Solution")
    print("========")
    utils.print_solution(goal_node)
    print("========")
    print("Path cost = %d" % goal_node[2])
    print("Number of Visited States = %d" % n_visits)
else:
    print("No solutions found")()
print("Execution Time = %s seconds" % round(time.process_time() - point_time, 2))