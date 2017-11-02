from problem_generator import generate_target, generate_numbers
from top_solver import make_tree, solve


def play():
    numbers = generate_numbers(2)
    target = generate_target()
    solution = solve(numbers, target, make_tree)
    n = eval(solution)
    print('Problem: Make {} with {}'.format(target, ', '.join(map(str, numbers))))
    print('Solution: {} = {}'.format(solution, n))


if __name__ == '__main__':
    play()
