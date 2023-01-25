graph = {
    'Start' : ['d','e', 'p'],
    'd' : ['b', 'c', 'e'],
    'e' : ['r', 'h'],
    'p' : ['q'],
    'b' : ['a'],
    'c' : ['a'],
    'r': ['f'],
    'h': ['p', 'q'],
    'q': [],
    'a': [],
    'f': ['c', 'Goal'],
    'Goal': []
}

def dfs(node):
    visited = [node]
    queue = [node]

    while queue:
        node = queue.pop(0)
        print (node, end = " ")

        not_visited_neighbours = [n for n in graph[node] if n not in visited]
        visited.extend(not_visited_neighbours)
        queue = not_visited_neighbours + queue
    print()

dfs('Start')
