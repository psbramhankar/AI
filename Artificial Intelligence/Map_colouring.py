domain = ['R', 'G', 'B']
assigned = {'WA': None, 'NT': None, 'Q': None, 'SA': None, 'NSW': None, 'V': None, 'T': None}
neighbours = {'WA': ['NT', 'SA'], 'NT': ['WA', 'Q', 'SA'], 'Q': ['NT', 'SA', 'NSW'],
              'SA': ['WA', 'NT', 'Q', 'NSW', 'V'], 'NSW': ['Q', 'SA', 'V'],
              'V': ['SA', 'NSW'], 'T': []}


def assignCol():
    for key in assigned.keys():
        print(key)
        i, flag = 0, 0
        current = key
        if assigned[key] == None:
            while i <= (len(domain) - 1):
                assigned[current] = domain[i]

                print('the assigned color for ', current, ' is: ', assigned[current])
                flag = checkConst(current)
                if flag == 1:
                    i = i + 1
                else:
                    break


def checkNbr(key):
    for k, v in neighbours.items():
        if k == key:
            return neighbours[key]


def checkConst(key):
    flag = 0
    nblist = checkNbr(key)
    for value in nblist:
        if assigned[key] == assigned[value]:
            print('constraint violated for: ', key)
            flag = 1
            return flag


assignCol()
print('the map is assigned following colors: ')
print(assigned)

