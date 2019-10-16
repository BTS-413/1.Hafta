def dikucgenmi(a,b,hipoten):
    if a**2 + b**2 == hipoten**2:
        return "Bu ucgen reis"
    else:
        return "hipotens bile bunu ucgen yapamaz"
a = int(input("Birinci kenar: "))
b = int(input("Ikinci kenar : "))
c = int(input("Ucuncu kenar: "))

print(dikucgenmi(a,b,c))
