import random
def mane_function(list1):
    for x in list1:
        print(x)


my_list1 = [1,2,3]
my_list2 = []
for i in range (3):
    my_list2.append(random.randint(1,5))

mane_function(my_list1)
mane_function(my_list2)


