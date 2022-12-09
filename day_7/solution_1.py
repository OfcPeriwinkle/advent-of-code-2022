from __future__ import annotations


class Tree:
    def __init__(self, name: str, size: int, is_dir: bool):
        self.parent = None
        self.children = {}
        self.name = name
        self.directory = is_dir
        self.size = size
        self.total_size = size

    def get_total_size(self) -> int:
        self.total_size = self.size

        if len(self.children) == 0:
            return self.total_size

        for child in self.children.values():
            self.total_size += child.get_total_size()

        return self.total_size

    def total_dir_under_size(self, size: int):
        total_under_size = 0

        if self.directory and self.total_size < size:
            total_under_size = self.total_size

        if len(self.children) == 0:
            return total_under_size

        for child in self.children.values():
            total_under_size += child.total_dir_under_size(size)

        return total_under_size

    def has_child(self, name: str) -> bool:
        if name in self.children:
            return True

        return False

    def add_child(self, child: Tree):
        child.parent = self
        self.children[child.name] = child


def change_directory(argument: str, node: Tree) -> Tree:
    if argument == '/':
        # TODO: 
        return node

    if argument == '..':
        return node.parent

    return node.children[argument]


def solution_1(log_path: str):
    with open(log_path, 'r', encoding='utf-8') as handle:
        log = handle.read().split('\n')

    root = Tree('/', 0, True)
    cur_node = root

    for i, entry in enumerate(log):
        split_entry = entry.split(' ')

        if split_entry[0] == '$' and split_entry[1] == 'cd':
            cur_node = change_directory(split_entry[2], cur_node)
        elif split_entry[0] == '$' and split_entry[1] == 'ls':
            # Don't need to do anything for ls
            pass
        elif split_entry[0] == 'dir':
            new_child = Tree(split_entry[1], 0, True)
            cur_node.add_child(new_child)
        else:
            new_child = Tree(split_entry[1], int(split_entry[0]), False)
            cur_node.add_child(new_child)

    print(root.get_total_size())
    print(root.total_dir_under_size(100000))


if __name__ == '__main__':
    solution_1('day_7/input.txt')
