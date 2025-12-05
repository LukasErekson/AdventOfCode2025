def main(input_path: str = "inputs/05/sample.txt") -> None:
    raw_input: str
    with open(input_path, "r") as f:
        raw_input = f.read()

    database: list[str] = raw_input.splitlines()
    split_line: int = database.index("")
    fresh_ranges: list[range] = [range(int(fr.split("-")[0]), int(fr.split("-")[1]) + 1) for fr in database[:split_line]]
    ingredients: list[int] = list(map(int, database[split_line + 1 :]))

    part1(fresh_ranges, ingredients)
    part2(fresh_ranges)

    return

def part1(fresh_ranges: list[range], ingredients: list[int]) -> None:
    fresh_ingredient_count: int = 0
    for ingredient in ingredients:
        if any(ingredient in fresh_range for fresh_range in fresh_ranges):
            fresh_ingredient_count += 1

    print(f"Part 1: The number of fresh ingredients is {fresh_ingredient_count}")
    return

def part2(fresh_ranges: list[range]) -> None:
    fresh_ranges.sort(key=lambda r: r.start)
    merged_ranges: list[range] = []

    current_range: range = fresh_ranges[0]
    range_index: int = 1

    while range_index < len(fresh_ranges):
        next_range: range = fresh_ranges[range_index]
        while can_merge_ranges(current_range, next_range):
            next_range = fresh_ranges[range_index]
            current_range = range(current_range.start, max(next_range.stop, current_range.stop))
            range_index += 1
            if range_index < len(fresh_ranges):
                next_range = fresh_ranges[range_index]
            else:
                break

        merged_ranges.append(current_range)
        current_range = next_range
        range_index += 1

    fresh_ingredient_count: int = sum([len(r) for r in merged_ranges])

    print(f"Part 2: The total possible fresh ingredients is {fresh_ingredient_count}")

    return

def can_merge_ranges(r1: range, r2: range) -> bool:
    return r2.start in r1 or r2.start == r1.stop

if __name__ == "__main__":
    main()