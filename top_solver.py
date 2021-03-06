import random
nums = [5, 7, 8, 25, 100]
operators = ['-', '+', '*', '/']

tree = ('-', [
    6,
    (
        '*',
        [3, 9],
    ),
])


def make_tree(numbers, target):
    numbers = numbers.copy()
    node = numbers.pop()
    while numbers:
        node = ('+', (node, numbers.pop()))
    return node


def slightly_less_naive(numbers, target):
    numbers = numbers.copy()
    operators = '+ - * /'.split()
    node = numbers.pop()
    while numbers:
        node = (random.choice(operators), (node, numbers.pop()))
    return node


def walk_tree(tree):
    if isinstance(tree, int):
        return tree
    op, children = tree
    return '({} {} {})'.format(
        walk_tree(children[0]),
        op,
        walk_tree(children[1]),
    )


def solve(numbers, target, solver):
    solution = solver(numbers, target)
    return walk_tree(solution)


if __name__ == '__main__':
    answer = walk_tree(make_tree(nums))

    print(answer)
    print(eval(answer))
