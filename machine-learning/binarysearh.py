

def task(array,target):
    sorted_array=sorted(array)
    pair_list=dict()
    start_index=0
    end_index=length=len(sorted_array)
    
    # mid = (start_index + end_index)/2
    #special case


    for index,num in enumerate(sorted_array):
        start = index
        end = length -1
        complement_num= _binary(sorted_array,target - num,start+1,end)
        



def _binary(array,target,start,end):
    end = len(array) -1
    mid = (end-start)/2
    if mid <0:
        return None
    if array[mid] > target:
        _binary(array,target,start,mid-1)
    else:
        _binary(array,target,mid +1, end)
    
    return 


task([2,2,3,4],4)