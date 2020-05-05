def fib_sequence(n):
    def fib_rec(n):
        if n == 0 or n == 1:
            return n
        return fib_rec(n - 1) + fib_rec(n - 2)

    list = []
    for i in range(n):
        list += [fib_rec(i)]

    return list
#%%
def fib_top_down_(n):
    list = [-1]*(n)
    list[0] = 0
    list[1] = 1
    def fib_top_down(n):
        if list[n] == -1:
            list[n] = fib_top_down(n-1)+fib_top_down(n-2)
        return list[n]
    fib_top_down(n-1)
    return list
#%%
# %%
def fib_botton_up_(n):
    list = [0, 1]
    for i in range(2, n):
        list.append(list[i - 1] + list[i - 2])

    return list
