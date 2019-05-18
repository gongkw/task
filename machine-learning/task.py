

def task(array,target):
    sorted_array=sorted(array)
    pair_list=dict()
    start_index=0
    end_index=len(sorted_array) -1

    #special case


    while start_index <= end_index:
        pair_sum=sorted_array[start_index] + sorted_array[end_index]
        print pair_sum
        if pair_sum == target:
            pair_list[sorted_array[start_index]] = sorted_array[end_index]
            start_index +=1
            end_index -=1
        elif pair_sum < target:
            start_index +=1
        else:
            end_index -=1


    print pair_list

task([2,8,8,6,10],16)