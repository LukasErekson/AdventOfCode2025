
from typing import Generator, Tuple

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
    fresh_ingredients: set[int] = set()

    for fresh_range in fresh_ranges:
        fresh_ingredients.update(set(fresh_range))

    print(f"Part 2: The total possible fresh ingredients is {len(fresh_ingredients)}")

    return

if __name__ == "__main__":
    main()