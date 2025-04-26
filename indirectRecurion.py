def funcA(n):
    if n>0:
     print("A:", n)
    funcB(n-1)

    def funcB(n):
        if n>0:
            print("B:",n)
            funcA(n-1)
