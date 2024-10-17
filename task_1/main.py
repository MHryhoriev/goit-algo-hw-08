import heapq

def min_cost_to_coonect_cables(cable_lengths: list) -> list:

    heapq.heapify(cable_lengths)
    print(f"Initial cable lengths: {cable_lengths}")

    total_cost = 0

    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        cost = first + second
        total_cost += cost

        heapq.heappush(cable_lengths, cost)

        print(f"Connecting cables of length {first} and {second}: cost = {cost}")
        print(f"Current state of the heap: {cable_lengths}")

    return total_cost

def main():
    cable_lengths = [4, 3, 2, 6]
    total_min_cost = min_cost_to_coonect_cables(cable_lengths)
    print(f"\nMinimum cost to connect the cables: {total_min_cost}")

if __name__ == "__main__":
    main()
