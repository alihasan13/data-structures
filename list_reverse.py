import json
my_list=[]  #delare a empty list
list_length=int(input( "Enter the length of the list: "))   #input arry length
print ("Enter list data: ")
for i in range(list_length):                        #insert data into the list
    value=int(input() )
     
    my_list.append(value)
     
     
add=' '
my_list.reverse()                   #reverse the list
print (add.join(map(str,my_list)))  #print the output excluting the bracket,comma's
print (my_list)                     #print the into list format
