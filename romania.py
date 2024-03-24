# Define the Romania map graph as an adjacency list
romania_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

# Function to perform Iterative Deepening Depth-First Search (IDDFS)
def iddfs(graph, start, goal):
    depth = 0
    while True:
        result = dfs(graph, start, goal, depth)
        if result is not None:
            return result
        depth += 1

# Function to perform Depth-First Search (DFS)
def dfs(graph, node, goal, depth):
    if depth == 0 and node == goal:
        return [node]
    if depth > 0:
        if node == goal:
            return [node]
        for neighbor in graph[node]:
            result = dfs(graph, neighbor, goal, depth - 1)
            if result is not None:
                return [node] + result
    return None

# Main function
def main():
    start_city = 'Arad'
    goal_city = 'Bucharest'
    result = iddfs(romania_map, start_city, goal_city)
    if result is not None:
        print("Path found from", start_city, "to", goal_city, ":")
        print(" -> ".join(result))
    else:
        print("Path not found from", start_city, "to", goal_city)

if __name__ == "__main__":
    main()
