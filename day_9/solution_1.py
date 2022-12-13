def calc_positions(h_pos: tuple, t_pos: tuple, direction: str):
    if direction == 'R':
        new_h_pos = (h_pos[0] + 1, h_pos[1])
    elif direction == 'L':
        new_h_pos = (h_pos[0] - 1, h_pos[1])
    elif direction == 'U':
        new_h_pos = (h_pos[0], h_pos[1] + 1)
    else:
        new_h_pos = (h_pos[0], h_pos[1] - 1)

    delta_t_pos = (t_pos[0] - new_h_pos[0], t_pos[1] - new_h_pos[1])

    if 0 not in delta_t_pos and (delta_t_pos[0] in (-2, 2) or delta_t_pos[1] in (-2, 2)):
        # diagonal move
        new_t_pos = h_pos
    elif delta_t_pos[0] in (-2, 2):
        # row move
        new_t_pos = (h_pos[0], t_pos[1])
    elif delta_t_pos[1] in (-2, 2):
        # col move
        new_t_pos = (t_pos[0], h_pos[1])
    else:
        new_t_pos = t_pos

    return new_h_pos, new_t_pos


def solution(path: str):
    with open(path, 'r', encoding='utf-8') as handle:
        moves = handle.read().split('\n')


    h_pos = (0, 0)
    t_pos = (0, 0)
    visited_cells = {t_pos: True}

    for move in moves:
        direction, times = move.split(' ')

        for _ in range(int(times)):
            h_pos, t_pos = calc_positions(h_pos, t_pos, direction)
            visited_cells[t_pos] = True

    print(len(visited_cells))


if __name__ == '__main__':
    solution('day_9/input.txt')
