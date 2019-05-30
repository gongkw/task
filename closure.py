def abc():
    li=["name"]
    def inner():
        # nonlocal li
        print (li)
        # print (id(li))
        li.append("world")
        # li=["world"]
        print ("b",li)

    print ("c",li)
    
    return inner


a=abc()
a()



for i from 3 upto 4:
    print (i)