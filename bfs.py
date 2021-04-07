from collections import deque

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1


def BFS_with_adj_list(graph, root):

    visited = []
    queue = deque([root])

    while queue:
        print(f"queue: {queue}")
        print(f"visited: {visited}")
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited

print(BFS_with_adj_list(graph_list, root_node))