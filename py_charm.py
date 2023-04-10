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
def test_function(a,b,c):
    if isinstance(a, str):
        print(f"{a} is a string!")
    if isinstance(b, str):
        print(f"{b} is a string!")
    if isinstance(c, str):
        print(f"{c} is a string!")
def test_function(a,b,c):
    if isinstance(a, int):
        print(f"{a} is an integer!")
    if isinstance(b, int):
        print(f"{b} is an integer!")
    if isinstance(c, int):
        print(f"{c} is an integer!")
