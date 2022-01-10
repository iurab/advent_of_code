def get_input():
    tree = list(map(int, open('input').read().split()))
    return tree


def sum_metadata(tree):
    n_children = tree.pop(0)
    n_metadata = tree.pop(0)
    return sum(sum_metadata(tree) for _ in range(n_children)) + sum(
        tree.pop(0) for _ in range(n_metadata))


def root_val(tree):
    n_children = tree.pop(0)
    n_ref = tree.pop(0)
    children = [root_val(tree) for _ in range(n_children)]
    refs = [tree.pop(0) for _ in range(n_ref)]
    if n_children == 0:
        return sum(refs)
    return sum(
        children[i - 1] for i in refs if i - 1 in range(n_children))


if __name__ == "__main__":
    sum_value = sum_metadata(get_input())
    print(sum_value)
    value = root_val(get_input())
    print(value)