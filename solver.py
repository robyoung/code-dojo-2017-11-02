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

if __name__ == "__main__":
    for i in pairs([4,5,2,8,6]):
        for j in pairs(i):
            print(j)
