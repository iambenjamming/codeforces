t = int(input())

for _ in range(t):

    password = input()
    ans = []
    inserted = False

    ans.append(password[0])

    if len(password) == 1:
        if password[0] != 'z':
            new = chr(ord(password[0]) + 1)
            ans.append(new)
            inserted = True
                
        elif password[0] == 'z':
            new = chr(ord(password[0]) - 1)
            ans.append(new)
            inserted = True
    
    for i in range(1, len(password)):
        
        if password[i] == password[i-1] and inserted == False:
            if password[i-1] != 'z':
                new = chr(ord(password[i]) + 1)
                ans.append(new)
                inserted = True
                
            elif password[i-1] == 'z':
                new = chr(ord(password[i]) - 1)
                ans.append(new)
                inserted = True
            ans.append(password[i])
            
        else:
            ans.append(password[i])

    if inserted == False:
        if password[-1] != 'z':
            new = chr(ord(password[-1]) + 1)
            ans.append(new)
            inserted = True
                
        elif password[-1] == 'z':
            new = chr(ord(password[-1]) - 1)
            ans.append(new)
            inserted = True

    print(''.join(ans))
