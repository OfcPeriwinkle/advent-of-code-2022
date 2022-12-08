from typing import List, Tuple


def get_ranges(start: str, end: str):
    return set(range(int(start), int(end) + 1))


def get_assignments(path: str) -> List[Tuple[set]]:
    with open(path, 'r', encoding='utf-8') as handle:
        lines = handle.read().split('\n')

    split_assignments = [line.split(',') for line in lines]

    return [
        (get_ranges(*pair[0].split('-')), get_ranges(*pair[1].split('-')))
        for pair in split_assignments
    ]


def solution_1(assignments_path: str):
    assignment_range_pairs = get_assignments(assignments_path)

    fully_contained_assignments = 0
    for pair in assignment_range_pairs:
        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
            fully_contained_assignments += 1

    print(fully_contained_assignments)


def solution_2(assignments_path: str):
    assignment_range_pairs = get_assignments(assignments_path)

    overlapping_assignments = 0
    for pair in assignment_range_pairs:
        if len(pair[0].intersection(pair[1])) > 0:
            overlapping_assignments += 1

    print(overlapping_assignments)


if __name__ == '__main__':
    solution_1('day_4/input.txt')
    solution_2('day_4/input.txt')
