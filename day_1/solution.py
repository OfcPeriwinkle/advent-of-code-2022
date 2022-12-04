def main(log_file: str, top_n_elves: int):
    """
    Given a log of calories each elf is holding in log_file, display the total
    number of calories for the top n elves.

    Args:
        log_file: path to the file containing the calories for items each elf is
            holding
        top_n_elves: the number of elves with the highest calorie counts to get
            the sum for

    Displays:
        An int of the number of calories the top n elves are holding
    """

    with open(log_file, 'r', encoding='utf-8') as handle:
        elf_log = handle.read().split('\n')
        log_length = len(elf_log)

    # Create list of tuples (elf_index, elf_calories) from log
    calories_by_elf = []
    elf_index = 0
    total = 0
    for log_index, value in enumerate(elf_log):
        if value != '':
            total += int(value)

        # Handle elf boundary or last elf
        if value == '' or log_index + 1 == log_length:
            calories_by_elf.append((elf_index, total))
            total = 0
            elf_index += 1

    # Sort log info by calories
    sorted_elf_log = sorted(calories_by_elf, key=lambda x: x[1], reverse=True)

    # Get the sum of the calories for the top n elves
    top_calories = 0
    for _, calories in sorted_elf_log[:top_n_elves]:
        top_calories += calories

    print(top_calories)


if __name__ == '__main__':
    main('input.txt', 3)
