from itertools import product

def solution(word):
    check = ['A', 'E', 'I', 'O', 'U']
    li= []
    for i in range(1,6):
        li2 = list(product(check, repeat=i))
        li3= []
        for elem in li2:
            li3.append("".join(elem))

        li= li+ li3
        #print(li)
    
    li.sort()
    
    return li.index(word)+1