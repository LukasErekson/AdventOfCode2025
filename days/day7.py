from pprint import pprint

__memoize_cache: dict = {}

def memoize(f):
    """Memoize implementation as a function decorator.
    For a given function, if the args and kwargs are present as a key
    to the dictionary, then return the cached value. Otherwise, add it
    to the cached value.

    Parameters
    ----------
        f (function) : The function to call.

    Returns
    -------
        The value of the function called with the given parameters.
    """
    def wrap(*args, **kwargs):
        cache_key: tuple = (f, *args, *kwargs)
        if cache_key not in __memoize_cache:
            __memoize_cache[cache_key] = f(*args, *kwargs)
        return __memoize_cache[cache_key]
    return wrap


def main(input_path: str = "inputs/07/sample.txt") -> None:
    input_data: str
    with open(input_path) as f:
        input_data = f.read()

    tachyon_grid: list[str] = input_data.split("\n")
    start_pos: tuple[int, int] = (0, tachyon_grid[0].index("S"))

    part1(tachyon_grid, start_pos)
    part2(tachyon_grid, start_pos)

def part1(tachyon_grid: list[str], start_pos: tuple[int, int]) -> None:
    times_split: int = 0

    current_beam_positions: set[tuple[int, int]] = {start_pos}
    for line in tachyon_grid[1:]:
        beams_to_update: set[tuple[int, int]] = set(current_beam_positions)
        for beam_pos in beams_to_update:
            current_beam_positions.remove(beam_pos)
            next_pos: tuple[int, int] = (beam_pos[0] + 1, beam_pos[1])
            if line[next_pos[1]] == '^':
                times_split += 1
                current_beam_positions.add((next_pos[0], next_pos[1] - 1))
                current_beam_positions.add((next_pos[0], next_pos[1] + 1))
            else:
                current_beam_positions.add(next_pos)

    print(f"The number of times the beam split is {times_split}")

    return

def part2(tachyon_grid: list[str], start_pos: tuple[int, int]) -> None:
    timeline_count: int = tachyon_particle_recursive(tuple(tachyon_grid), start_pos)

    print(f"The number of timelines is {timeline_count}")
    return

@memoize
def tachyon_particle_recursive(tachyon_gird: tuple[str, ...], current_pos: tuple[int, int]) -> int:
    next_pos: tuple[int, int] = (current_pos[0] + 1, current_pos[1])

    if next_pos[0] >= len(tachyon_gird):
        return 1

    if tachyon_gird[next_pos[0]][next_pos[1]] == '^':
        left: int = 0 if next_pos[1] - 1 < 0 else tachyon_particle_recursive(tachyon_gird, (next_pos[0], next_pos[1] - 1))
        right: int = 0 if next_pos[1] + 1 >= len(tachyon_gird[next_pos[1]]) else tachyon_particle_recursive(tachyon_gird, (next_pos[0], next_pos[1] + 1))
        return left + right

    return tachyon_particle_recursive(tachyon_gird, next_pos)

if __name__ == "__main__":
    main()