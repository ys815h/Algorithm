def solution(s):
    a = []
    s = s.split(" ")
    print(s)
    
    print(len(s))
    for i in range(len(s)):
        if s[i] != '':
            a.append(list(s[i])[0].upper())

            for j in range(1, len(s[i])):
                if j % 2 == 1:
                    a.append(list(s[i])[j].lower())
                else:
                    a.append(list(s[i])[j].upper())
            a.append(' ')
        else:
            a.append(' ')
    
    a.pop()
    return str(''.join(a))