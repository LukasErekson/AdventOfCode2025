from math import sqrt, prod
from itertools import combinations

Point = tuple[int, int, int]


def main(input_path: str = "inputs/08/sample.txt") -> None:
    input_data: str
    with open(input_path) as f:
        input_data = f.read()

    lines: list[list[int]] = list(
        map(lambda s: s.split(","), input_data.split("\n"))  # ty:ignore[invalid-argument-type]
    )
    points: list[Point] = [(int(x), int(y), int(z)) for x, y, z in lines]

    part1(points)
    part2(points)


def dist(a: Point, b: Point) -> float:
    return sqrt(
        sum([(a_coord - b_coord) ** 2 for a_coord, b_coord in zip(a, b)])
    )


def calculate_distance_list(
    points: list[Point],
) -> list[tuple[float, Point, Point]]:
    return [(dist(a, b), a, b) for a, b in combinations(points, 2)]


def part1(points: list[Point]) -> None:
    distance_list: list[tuple[float, Point, Point]] = calculate_distance_list(
        points
    )
    distance_list.sort(key=lambda dpp: dpp[0])

    circuits: list[set[Point]] = [set([p]) for p in points]
    connections_made: int = 0
    for d in distance_list:
        if connections_made >= 10:
            break
        _, p1, p2 = d
        p1_circuit_idx: int = -1
        p2_circuit_idx: int = -1
        for i, circuit in enumerate(circuits):
            if p1 in circuit:
                p1_circuit_idx = i
            if p2 in circuit:
                p2_circuit_idx = i
        p1_circuit: set[Point] = (
            set() if p2_circuit_idx == -1 else circuits[p1_circuit_idx]
        )
        p2_circuit: set[Point] = (
            set() if p2_circuit_idx == -1 else circuits[p2_circuit_idx]
        )

        if p1_circuit_idx == p2_circuit_idx:
            if p1_circuit_idx == -1:
                circuits.append(set([p1, p2]))
            connections_made += 1
            continue

        if p1_circuit_idx != -1:
            p1_circuit = circuits.pop(circuits.index(p1_circuit))
        if p2_circuit_idx != -1:
            p2_circuit = circuits.pop(circuits.index(p2_circuit))

        new_circuit: set[Point] = p1_circuit.union(p2_circuit)
        circuits.append(new_circuit)
        connections_made += 1

    circuit_lengths: list[int] = [len(c) for c in circuits]
    circuit_lengths.sort()
    print(
        f"After the first {connections_made} connections, we have {len(circuits)} circuits."
    )
    print(
        f"The top 3 circuit lengths are {circuit_lengths[-1]}, {circuit_lengths[-2]}, and {circuit_lengths[-3]}. Multiplying those together, we have {prod(circuit_lengths[-3:])}"
    )

    return


def part2(points: list[Point]) -> None:
    distance_list: list[tuple[float, Point, Point]] = calculate_distance_list(
        points
    )
    distance_list.sort(key=lambda dpp: dpp[0])

    circuits: list[set[Point]] = [set([p]) for p in points]
    for d in distance_list:
        if len(circuits) == 1:
            break
        _, p1, p2 = d
        p1_circuit_idx: int = -1
        p2_circuit_idx: int = -1
        for i, circuit in enumerate(circuits):
            if p1 in circuit:
                p1_circuit_idx = i
            if p2 in circuit:
                p2_circuit_idx = i
        p1_circuit: set[Point] = (
            set() if p2_circuit_idx == -1 else circuits[p1_circuit_idx]
        )
        p2_circuit: set[Point] = (
            set() if p2_circuit_idx == -1 else circuits[p2_circuit_idx]
        )

        if p1_circuit_idx == p2_circuit_idx:
            if p1_circuit_idx == -1:
                circuits.append(set([p1, p2]))
            continue

        if p1_circuit_idx != -1:
            p1_circuit = circuits.pop(circuits.index(p1_circuit))
        if p2_circuit_idx != -1:
            p2_circuit = circuits.pop(circuits.index(p2_circuit))

        new_circuit: set[Point] = p1_circuit.union(p2_circuit)
        circuits.append(new_circuit)

    print(
        f"The last two points to connect all of them into one circuit are {p1} and {p2}."
    )
    print(f"The product of their X coordinates is {p1[0] * p2[0]}.")

    return


if __name__ == "__main__":
    main()
