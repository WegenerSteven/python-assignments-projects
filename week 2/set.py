#creates and empty lis
my_list=[]
print("Empty list", my_list) 
#adds items to the empty list above
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Added list: ", my_list)
        #Insert the value 15 at the second position in the list.
my_list[1] =15

#Extend my_list with another list: [50, 60, 70].
my_list1=[50,60,70]
my_list.extend(my_list1)
print("Extended List: ",my_list)

#Remove the last element from my_list.
del my_list[6]
my_list.sort()  #Sort my_list in ascending order.
print(my_list)
index=my_list.index(30)
print('index of',30,'in my_list is:', index)  #Find and print the index of the value 30 in my_list.