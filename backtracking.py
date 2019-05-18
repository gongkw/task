tmp=[]
def permute(list, s, tmp):
    if list == 1:
        return s
    else:
        for y in permute(1, s,tmp):
            for x in permute(list - 1, s,tmp):
                tmp.append(y+x)
        return tmp
        
print(permute(1, ["a","b","c"],tmp))
print(permute(2, ["a","b","c"],tmp))