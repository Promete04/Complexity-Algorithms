import heapq

def find_fastest_routes(computers, cables, main_server):
    # Create the graph from the list of computers and cables
    graph = {computer: [] for computer in computers}
    for cable in cables:
        computer1, computer2, transmission_time = cable
        graph[computer1].append((computer2, transmission_time))
        graph[computer2].append((computer1, transmission_time))

    # Initialize the priority queue with the main server and a transmission time of 0
    pq = [(0, main_server)]
    # Initialize the transmission times dictionary with infinity for all computers
    t_transmision = {computer: float('inf') for computer in computers}
    # Set the transmission time for the main server to 0
    t_transmision[main_server] = 0
    # Initialize the visited set to keep track of processed computers
    visited = set()

    while pq:
        # Get the computer with the smallest transmission time from the priority queue
        # Used a heap to simplify the process of getting the smallest transmission time, could be done with a regular list and min function
        current_transmission_time, current_computer = heapq.heappop(pq)

        # If the current computer has already been visited, skip it
        if current_computer in visited:
            continue

        # Mark the current computer as visited
        visited.add(current_computer)

        # Iterate over the neighbors of the current computer
        for neighbor, delay in graph[current_computer]:
            # Calculate the new transmission time to the neighbor
            new_transmission_time = current_transmission_time + delay

            # If the new transmission time is smaller, update it
            if new_transmission_time < t_transmision[neighbor]:
                t_transmision[neighbor] = new_transmission_time
                # Push the neighbor and its transmission time to the priority queue
                heapq.heappush(pq, (new_transmission_time, neighbor))

    # Return the dictionary of transmission times from the main server to all other computers
    return t_transmision

# Example usage
computers = ['A', 'B', 'C', 'D']
cables = [
    ('A', 'B', 5),
    ('A', 'C', 1),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
]
main_server = 'A'
t_transmision = find_fastest_routes(computers, cables, main_server)
print(f"Fastest routes from {main_server}: {t_transmision}")