import the4

with open("cases.txt", 'r') as c:
    v = 0
    t = 0
    ll = c.readlines()
    Descriptions = []
    for l in ll:
        if l.startswith("["):
            Descriptions = eval(l.strip('\n'))
            continue
        t += 1
        l = l.strip('\n').split('|')
        result = the4.inheritance(Descriptions + [l[0]])
        if result == eval(l[1]):
            v += 1
        else:
            print(result)
    print(f"All cases tested. \n{v}/{t} is correct")
