from itertools import combinations, permutations

Point = tuple[int, int]


def main(input_path: str = "inputs/09/sample.txt") -> None:
    input_data: str
    with open(input_path) as f:
        input_data = f.read()

    red_tile_coordinates: list[Point] = parse_input(input_data)

    part1(red_tile_coordinates)
    part2()


def parse_input(input_data: str) -> list[Point]:
    return [tuple(map(int, s.split(","))) for s in input_data.split("\n")]  # ty:ignore[invalid-return-type]


def compute_area(a: Point, b: Point) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def part1(coordinates: list[Point]) -> None:
    area_to_coords: dict[int, list[tuple[Point, Point]]] = {}
    for a, b in combinations(coordinates, 2):
        area: int = compute_area(a, b)
        if area in area_to_coords:
            area_to_coords[area].append((a, b))
            continue
        area_to_coords[area] = [(a, b)]

    max_area: int = max(area_to_coords.keys())

    print(
        f"The max area is {max_area} with possible points of {area_to_coords[max_area]}"
    )
    return


def part2() -> None:
    return


if __name__ == "__main__":
    main()
