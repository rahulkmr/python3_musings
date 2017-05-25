import collections
thunk = lambda fn, *args, **kwargs: lambda: fn(*args, **kwargs)


def trampoline(bouncer):
    while isinstance(bouncer, collections.Callable):
        bouncer = bouncer()
    return bouncer


def fact(n, accum=1):
    if n <= 1:
        return accum
    else:
        return thunk(fact, n-1, n*accum)

print(trampoline(fact(1000)))
