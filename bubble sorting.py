from random import randrange

my_list = []
for i in range(10):
    my_list.append(randrange(100))
print("before sorting: \n",my_list)

#sortowanie
j_count = 1
counter=0
for j in range(0,len(my_list)-j_count):
    for i in range(0,len(my_list)-j_count):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            counter += 1
    #j_count+=1

print("after sorting: \n",my_list,j_count,counter)




