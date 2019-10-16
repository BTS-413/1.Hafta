def ucgen(a,b,hipotenus):
    if a**2 + b**2 ==hipotenus**2:
        return "bu bir üçgendir"
    else:
        return "bu bir üçgen değildir"

print(ucgen(3,4,5))
