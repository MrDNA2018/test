def constraint():
    return True


def bound():
    return True


def perm_backtracking(depth, lst):
    size = len(lst)

    if depth == size:
        print(lst)
    else:
        for i in range(depth, size):
            if constraint() and bound():
                lst[depth], lst[i] = lst[i], lst[depth]
                perm_backtracking(depth + 1, lst)
                lst[depth], lst[i] = lst[i], lst[depth]