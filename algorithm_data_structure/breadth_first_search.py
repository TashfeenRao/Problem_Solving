from collections import deque

graph = {
        "alice": ["mick", "jonathan","tash"],
        "tash": ["manan", "jonathan"]
}
data = {"manan": "mango seller"}
def breadth_first_search(name):
    search_queue = deque()
    if name not in graph:
        return False
    search_queue += [name]
    search_queue += graph[name]
    already_visited = []
    
    while search_queue:
        node = search_queue.popleft()
        if node not in already_visited:
            if check_if_mango_seller(node):
                print("you have found mango seller")
                return True
            else:
                already_visited.append(node)
                if node in graph:
                    search_queue += graph[node]
    return False
        
    
def check_if_mango_seller(name):
    print(name)
    if name not in data:
        return False
    return data[name] == 'mango seller'

print(breadth_first_search("alice"))