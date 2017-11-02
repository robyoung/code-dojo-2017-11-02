import random

def pairs(children):
    if len(children) == 1: yield list(children)
    for index, i in enumerate(children):
        for j in children[index+1:]:
            current_pair = (i, j)
            remaining_kids = set(children) - set(current_pair)
            if remaining_kids:
                for pair in pairs(list(remaining_kids)):
                    yield [current_pair] + pair
            else:
                yield [current_pair]

def perform_ops(paired_children):
    pass

def demo():
    for i in pairs([4,5,2,8,6]):
        for j in pairs(i):
            print(j)


def make_n(n=5):
    print(n)
    p = list(pairs([4,5,2,8,6]))
    print(p)
    while len(p[0]) > n:
        p = list(pairs(set(p)))
        print(p)
    return p

if __name__ == "__main__":
    # print(n())
    # print(make_n(2))
    # print(list(pairs([1, 2, 3, 4, 5])))
    demo()
