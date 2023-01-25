graph = {
    'Start' : [('d', 3),('e', 9), ('p', 1)],
    'd' : [('b', 1), ('c', 8), ('e', 2)],
    'e' : [('r', 2), ('h', 8)],
    'p' : [('q', 15)],
    'b' : [('a', 2)],
    'c' : [('a', 2)],
    'r': [('f', 1)],
    'h': [('p', 4), ('q', 4)],
    'q': [],
    'a': [],
    'f': [('c', 3), ('Goal', 2)],
    'Goal': []
}


def ucs(node, goal):
    queue = [(node, 0)]

    while queue:
        node, cost = queue.pop(0)
        print(node, cost)
        if(node == goal):
            break

        for nn, cc in graph[node]:
            queue.append((nn, cc + cost))
            queue.sort(key = lambda x: x[-1]) 

ucs('Start', 'Goal')
