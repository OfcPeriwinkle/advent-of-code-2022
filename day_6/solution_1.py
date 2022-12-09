def solution(path: str, marker_len: int):
    with open(path, 'r', encoding='utf-8') as handle:
        data = handle.read()

    i = 0
    j = 1
    buf = []
    while len(buf) < marker_len:
        if len(buf) == 0:
            buf.append(data[i])

        if data[j] in buf:
            # Collision
            buf_collision_index = buf.index(data[j])
            i = i + buf_collision_index + 1
            buf = buf[buf_collision_index + 1:]

        buf.append(data[j])
        j += 1

    print(j)

if __name__ == '__main__':
    solution('day_6/input.txt', 4)
    solution('day_6/input.txt', 14)
