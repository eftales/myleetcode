def t():
    n1 = "n1"
    print(n1)
    def tt():
        nonlocal n1
        n1 = "n11"
    tt()
    print(n1)

t()

