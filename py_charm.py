def mane_function(x,y,z):
    list1 = [x,y,z]
    print(list1)
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z