def compose(f, g):
    def h(x):
        return f(g(x))
    return h

