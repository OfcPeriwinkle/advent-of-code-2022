WEIGHTS = {chr(val): val - (ord('a') - 1) for val in range(ord('a'), ord('z') + 1)}
WEIGHTS.update({chr(val): val - (ord('A') - 1) + 26 for val in range(ord('A'), ord('Z') + 1)})


def get_rucksacks(path: str):
    with open(path, 'r', encoding='utf-8') as handle:
        return handle.read().split('\n')


def solution_1(rucksacks_path: str):
    rucksacks = get_rucksacks(rucksacks_path)

    total = 0
    for rucksack in rucksacks:
        items_per_compartment = len(rucksack) // 2
        first_compartment = rucksack[:items_per_compartment]
        second_compartment = rucksack[items_per_compartment:]

        shared_item = ''.join(set(first_compartment).intersection(second_compartment))
        total += WEIGHTS[shared_item]

    print(total)


def grouper(source_iterable: list, group_size: int):
    for i in range(0, len(source_iterable), group_size):
        yield source_iterable[i:i + group_size]


def solution_2(rucksacks_path: str):
    rucksacks = get_rucksacks(rucksacks_path)

    total = 0
    for rucksack_group in grouper(rucksacks, 3):
        badge = ''.join(
            set(rucksack_group[0]).intersection(rucksack_group[1]).intersection(rucksack_group[2]))

        total += WEIGHTS[badge]

    print(total)

if __name__ == '__main__':
    solution_1('day_3/input.txt')
    solution_2('day_3/input.txt')
