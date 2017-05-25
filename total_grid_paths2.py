#!/usr/bin/env python
from collections import defaultdict


def gen_neighour(start, end):
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, 1], [-1, -1], [1, 1], [1, -1]]

    def neighours(current):
        return ((current[0] + d[0], current[1] + d[1]) for d in directions
                if (start[0] <= (current[0] + d[0]) <= end[0]) and (start[1] <= (current[1] + d[1]) <= end[1]))
    return neighours


def count_all_paths(start, end):
    neighours = gen_neighour(start, end)
    path_count = 0
    queue = [start]
    prev = defaultdict(set)
    while queue:
        node = queue.pop()
        if node[0] == end[0] and node[1] == end[1]:
            path_count += 1
            continue
        for neighour in neighours(node):
            if not is_prev(neighour, node, prev):
                prev[neighour].add(node)
                queue.append(neighour)
    return path_count


def is_prev(neighbour, node, prev):
    parents = prev.get(node)
    if not parents:
        return False
    elif neighbour == node or neighbour in parents:
        return True
    else:
        return any(is_prev(neighbour, p, prev) for p in parents)


print(count_all_paths((1, 1), (3, 3)))
