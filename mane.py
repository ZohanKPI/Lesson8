import random
def mane_function(list1):
    for x in list1:
        print(x)


my_list1 = [1,2,3]
my_list2 = []
for i in range (3):
    my_list2.append(random.randint(1,5))
my_list3 = ['Python', 'Java', 'C++']
mane_function(my_list1)
mane_function(my_list2)
mane_function(my_list3)
def test_function(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

int1 = 3
int2 = 4
int3 = 5
test_function(int1, int2, int3)
