def mane_function(x,y,z,k):
    list1 = [x,y,z,k]
    print(list1)
    list2 = [x,y,z,k]
    print(list2)
    if list2 != list1:
        print("Lists are not the same!")
    else:
        print("Lists are the same!")
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x > y and x > z:
            return x
        elif y > x and y > z:
            return y
        else:
            return z
    else:
        return None
a = "Python"
b = "Java"
c = "C++"
d = "JavaScript"
print(mane_function(a,b,c,d))