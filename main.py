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
        print(node)
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


if __name__ == "__main__":
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D', 'E'],
             'C': ['E', 'F', 'G'],
             'D': ['E'],
             'E': [],
             'F': ['H'],
             'G': [],
             'H': []}
    #depth_first_travel(graph,'A')
    print('---')
    breath_first_travel(graph, 'A')

    #print(depth_first_search(graph, "A", "E"))
