baduk = []

for i in range(0,19) :
    baduk.append([ ])
    for j in range(0,19):
        baduk[i].append(0)

for i in range(0,19) :
    for j in range(0,19) :
        print(baduk[i][j], end = " ")
    print("\n")
