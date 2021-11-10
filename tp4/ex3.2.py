demo = {1: 'a', 2: 'b', 3: 'c'}


def echange(demo):
    return {y: x for x, y in demo.items()}


print(echange(demo))
