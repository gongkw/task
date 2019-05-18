
def count(array):
    memo=[None]*(len(array)+1)
    print num_count(array,len(array),memo)
    print memo



def num_count(array,num_lookat,memo):


    if num_lookat == 0:
        return 1

    s = len(array) - num_lookat
    if array[s] == '0':
        return 0
    if memo[num_lookat] != None:
        return memo[s]
    
    result = num_count(array,num_lookat-1,memo)

    if num_lookat >=2 and int(array[s:s+2]) <=26:
        result += num_count(array,num_lookat-2,memo)

    memo[num_lookat]=result
    return result


count("12") 