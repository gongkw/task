


def count( array,total):
    memo={}
    print pd(array,total,len(array)-1,memo)

    print memo



def pd(array,total,k,memo):
    key = str(total) +':' +str(k)

    if key in memo:
        return memo[key]
    
    if total == 0:
        return 1
    elif k<0:
        return 0
    elif total <0:
        return 0

    result=pd(array,total-array[k],k-1,memo)

    if array[k] >= total: 
        result += pd(array,total,k-1,memo)

    memo[key] = result
    return result

count([2,4,6,10],8)

