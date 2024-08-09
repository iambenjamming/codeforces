l = list(input())

a = l.index(".")

if l[a-1]!="9":
    if int(l[a+1]) >= 5:
        l[a-1] = int(l[a-1]) + 1
    for i in l:
        if i != ".":
            print(i,end="")
        else:
            break
else:
    print("GOTO Vasilisa.")
