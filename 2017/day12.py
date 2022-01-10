import os
import re


def digital_plumber_1(puzzle_data):
    village_graph = {}
    for line in puzzle_data:
        data = re.findall(r'\d+', line)
        prog_id = int(data[0])
        prog_connections = list(map(int, data[1:]))
        village_graph[prog_id] = prog_connections
    groups = [[0]]
    for entry in village_graph:
        if search_in_groups(groups, entry):
            continue
        found = False
        for i in range(len(groups)):
            new_elements = new_path_for_group(village_graph, groups[i], entry)
            if not new_elements is None:
                found = True
                groups[i].extend(new_elements)
                break
        if not found:
            groups.append([entry])
    print(len(groups))
    print(len(groups[0]))


def search_in_groups(groups, entry):
    for group in groups:
        if entry in group:
            return True
    return False


def new_path_for_group(graph, group, entry):
    for element in group:
        path = find_path(graph, entry, element)
        if not path is None:
            new_elements = list(set(path) - set(group))
            return new_elements
    return None


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def get_puzzle_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/' + 'day12.txt', 'r') as file:
        puzzle_data = file.readlines()
    return puzzle_data


def main():
    puzzle_data = get_puzzle_input()
    digital_plumber_1(puzzle_data)


if __name__ == '__main__':
    main()
