from typing import Generator, Tuple

def main(input_path: str = "inputs/04/input.txt") -> None:
    raw_input: str
    with open(input_path, "r") as f:
        raw_input = f.read()

    paper_map: list[str] = raw_input.split("\n")
    total_rows: int = len(paper_map)
    total_cols: int = len(paper_map[0])

    part1(paper_map)
    part2(paper_map)

    return

def part1(paper_map: list[str]) -> None:
    total_rows: int = len(paper_map)
    total_cols: int = len(paper_map[0])
    accessible_rolls: int = 0

    for row in range(total_rows):
        for col in range(total_cols):
            if paper_map[row][col] == '@':
                neighbors: int = 0
                for pulse_row, pulse_col in pulse_indices(row, col, total_rows, total_cols):
                    if paper_map[pulse_row][pulse_col] == '@':
                        neighbors += 1
                    if neighbors == 4:
                        break
                if neighbors < 4:
                    accessible_rolls += 1
    print(f"Part 1: The number of accessible rolls is {accessible_rolls}")
    return

def part2(paper_map: list[str]) -> None:
    total_rows: int = len(paper_map)
    total_cols: int = len(paper_map[0])
    removable_rolls: int = 0
    new_removable_rolls: int = -1

    while new_removable_rolls != 0:
        new_removable_rolls = 0
        for row in range(total_rows):
            for col in range(total_cols):
                if paper_map[row][col] == '@':
                    neighbors: int = 0
                    for pulse_row, pulse_col in pulse_indices(row, col, total_rows, total_cols):
                        if paper_map[pulse_row][pulse_col] == '@':
                            neighbors += 1
                        if neighbors == 4:
                            break
                    if neighbors < 4:
                        removable_rolls+= 1
                        new_removable_rolls += 1
                        paper_map[row] = paper_map[row][:col] + '.' + paper_map[row][col + 1:]
    print(f"Part 2: The number of removable rolls is {removable_rolls}")
    return

def pulse_indices(row: int, col: int, total_rows: int, total_cols: int) -> Generator[tuple[int, int], None, None]:
    pulse = list[(int, int)]
    # Above
    if (row - 1) >= 0:
        yield (row - 1, col)
    # Below
    if (row + 1) < total_rows:
        yield (row + 1, col)
    # Left
    if (col - 1) >= 0:
        yield (row, col - 1)
    # Right
    if (col + 1) < total_cols:
        yield (row, col + 1)
    # Upper Left
    if (row - 1) >= 0 and (col - 1) >= 0:
        yield (row - 1, col - 1)
    # Upper Right
    if (row - 1) >= 0 and (col + 1) < total_cols:
        yield (row - 1, col + 1)
    # Lower Left
    if (row + 1) < total_rows and (col - 1) >= 0:
        yield (row + 1, col - 1)
    # Lower Right
    if (row + 1) < total_rows and (col + 1) < total_cols:
        yield (row + 1, col + 1)

if __name__ == "__main__":
    main()