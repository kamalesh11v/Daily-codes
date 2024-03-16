from collections import deque

# Define the capacities of the jugs and the target amount of water
jug1_capacity = 5
jug2_capacity = 3
target_amount = 4

# Define state representation
class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

# Define possible actions
def fill_jug1(state):
    return State(jug1=jug1_capacity, jug2=state.jug2)

def fill_jug2(state):
    return State(jug1=state.jug1, jug2=jug2_capacity)

def empty_jug1(state):
    return State(jug1=0, jug2=state.jug2)

def empty_jug2(state):
    return State(jug1=state.jug1, jug2=0)

def pour_jug1_to_jug2(state):
    amount_to_pour = min(state.jug1, jug2_capacity - state.jug2)
    return State(jug1=state.jug1 - amount_to_pour, jug2=state.jug2 + amount_to_pour)

def pour_jug2_to_jug1(state):
    amount_to_pour = min(state.jug2, jug1_capacity - state.jug1)
    return State(jug1=state.jug1 + amount_to_pour, jug2=state.jug2 - amount_to_pour)

# Define the search algorithm
def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        state, path = queue.popleft()

        if state.jug1 == target_amount or state.jug2 == target_amount:
            return path

        if state in visited:
            continue

        visited.add(state)

        for action in [fill_jug1, fill_jug2, empty_jug1, empty_jug2, pour_jug1_to_jug2, pour_jug2_to_jug1]:
            next_state = action(state)
            if next_state not in visited:
                queue.append((next_state, path + [action]))

# Function to print capacities of jugs
def print_capacities(step, jug1, jug2):
    print(f"Step {step}: Jug1({jug1}/{jug1_capacity}), Jug2({jug2}/{jug2_capacity})")

# Initial state where both jugs are empty
start_state = State(jug1=0, jug2=0)

# Solve the problem
solution = bfs(start_state)

# Print the solution with capacities after each step
if solution:
    print("Solution Found:")
    jug1, jug2 = 0, 0
    print_capacities(0, jug1, jug2)
    for i, action in enumerate(solution):
        result = action(State(jug1, jug2))
        jug1, jug2 = result.jug1, result.jug2
        print_capacities(i+1, jug1, jug2)
else:
    print("No solution found.")
