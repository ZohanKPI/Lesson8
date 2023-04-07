def mane_function(x,y,z):
    list1 = [x,y,z]
    print(list1)
    list2 = [z,y,x]
    print(list2)
    if list2 != list1:
        print("Lists are not the same!")
    else:
        print("Lists are the same!")
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z