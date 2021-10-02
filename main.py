def show():
    print("Hello")


def depth_first_travel(graph, node, visited=set()):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            depth_first_travel(graph, neighbor, visited)


def depth_first_search(graph, node, key, visited=set(), path=[]) -> list:
    if node == key:
        path.append(node)
        return path

    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            (depth_first_search(graph, neighbor, key, visited, path))
            if path:
                path.append(node)
                return path


def breath_first_travel(graph, node, visited=set(), visit_queue=[]):
    if not visited:
        print(node)
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visit_queue:
                print(neighbor)
                visit_queue.append(neighbor)

    if visit_queue:
        breath_first_travel(graph, visit_queue.pop(0), visited, visit_queue)


def breath_first_search(graph, node, key, found=False, visited=set(), visit_queue=[]):
    if node == key:
        found = True
        return found

    # visited block
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visit_queue:
                print(neighbor)
                visit_queue.append(neighbor)

    # check all nodes are visited,
    # should put this after "visited block" because visit_queue empty when first function call
    if not visit_queue:
        return False
    return breath_first_search(graph, visit_queue.pop(0), key, found, visited, visit_queue)


if __name__ == "__main__":
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D', 'E'],
             'C': ['E', 'F', 'G'],
             'D': ['E'],
             'E': [],
             'F': ['H'],
             'G': [],
             'H': []}

    print(breath_first_search(graph, 'A', 'H'))
