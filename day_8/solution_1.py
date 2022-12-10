def is_visible(matrix: list, i: int, j: int) -> bool:
    height = matrix[i][j]

    left_vals = matrix[i][:j]
    if height > max(left_vals):
        return True

    right_vals = matrix[i][j + 1:]
    if height > max(right_vals):
        return True

    up_rows = matrix[:i]
    up_vals = [row[j] for row in up_rows]
    if height > max(up_vals):
        return True

    down_rows = matrix[i + 1:]
    down_vals = [row[j] for row in down_rows]
    if height > max(down_vals):
        return True

    return False


def create_matrix(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as handle:
        data = handle.read().split('\n')

    return [[int(height) for height in row] for row in data]


def solution_1(path: str):
    height_matrix = create_matrix(path)

    num_rows = len(height_matrix)
    num_cols = len(height_matrix[0])

    visible = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if i in (0, num_rows - 1):
                visible += 1
            elif j in (0, num_cols - 1):
                visible += 1
            elif is_visible(height_matrix, i, j):
                visible += 1

    print(visible)

###################################################################################################


def scenic_score(matrix: list, i: int, j: int) -> int:
    height = matrix[i][j]

    left, right, up, down = 0, 0, 0, 0

    left_vals = matrix[i][:j]
    for val in left_vals[::-1]:
        left += 1

        if height <= val:
            break

    right_vals = matrix[i][j + 1:]
    for val in right_vals:
        right += 1

        if height <= val:
            break

    up_rows = matrix[:i]
    up_vals = [row[j] for row in up_rows]
    for val in up_vals[::-1]:
        up += 1

        if height <= val:
            break

    down_rows = matrix[i + 1:]
    down_vals = [row[j] for row in down_rows]
    for val in down_vals:
        down += 1

        if height <= val:
            break

    return left * right * up * down


def solution_2(path: str):
    height_matrix = create_matrix(path)

    num_rows = len(height_matrix)
    num_cols = len(height_matrix[0])

    max_scenic_score = 0
    for i in range(num_rows):
        for j in range(num_cols):
            max_scenic_score = max(
                max_scenic_score, scenic_score(height_matrix, i, j))

    print(max_scenic_score)


if __name__ == '__main__':
    solution_1('day_8/input.txt')
    solution_2('day_8/input.txt')
