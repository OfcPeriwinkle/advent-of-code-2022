import re


DIGIT_REGEX = re.compile(r'\d+')
CARGO_REGEX = re.compile(r'[A-Z]')


def stacks_and_procedure(path: str):
    with open(path, 'r', encoding='utf-8') as handle:
        positions, procedures = handle.read().split('\n\n')

    # Process cargo stacks
    cargo_rows = positions.split('\n')

    # Create translation table for string index the cargo is found to label provided by the elves
    index_to_label = {
        match.start(): int(match[0])
        for match in DIGIT_REGEX.finditer(cargo_rows[-1])}

    # Load up cargo stacks
    stacks = {label: [] for label in index_to_label.values()}
    for row in cargo_rows[-2::-1]:
        for cargo in CARGO_REGEX.finditer(row):
            stacks[index_to_label[cargo.start()]].append(cargo[0])

    # Process procedures
    move_orders = []
    for procedure in procedures.split('\n'):
        move_orders.append([int(val)
                           for val in DIGIT_REGEX.findall(procedure)])

    return stacks, move_orders


def solution(rearrangement_procedure: str, new_crane: bool = False):
    stacks, procedure = stacks_and_procedure(rearrangement_procedure)

    # Move cargo around
    for quantity, origin, destination in procedure:
        cargo_being_moved = []
        for _ in range(quantity):
            cargo_being_moved.append(stacks[origin].pop())

        if new_crane:
            cargo_being_moved.reverse()

        stacks[destination].extend(cargo_being_moved)

    # Display results
    print(''.join(stack[-1] for stack in stacks.values()))


if __name__ == '__main__':
    solution('day_5/input.txt')
    solution('day_5/input.txt', True)
