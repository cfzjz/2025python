import copy


def use_copy():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


def use_deep_copy():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(f'c--{c}')
    print(f'd--{d}')
    print(id(c[0]),id(c[1]))
    print(id(d[0]),id(d[1]))


if __name__ == '__main__':
    use_copy()
    use_deep_copy()
