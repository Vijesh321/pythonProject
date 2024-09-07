


values =[3,4,5,8,0,73,2,"vijesh","kumar",8,9,0]
# list data types can accept the different datatypes at the same time in list
print(values)

print (values[7])  # by using index numbers
print (values[8])


print (values[-1])   # -1 means when we have large datatypes in list we have to print

print (values[7:9]) #  to print multiple data types at the same time succeeding index number will consider to -1
print (values[3:6])  #8,0,73
print(values[3:-1]) #[8, 0, 73, 2, 'vijesh', 'kumar', 8, 9]
print(values[-1:3])
print(values[3:6:4])
print(values[1:2:3])
print(values[8:9:7])
print(values[4:3:2])
print(values[8:7:6])


values.insert(7,"konderu")  # inserting data type into list
print(values)

values.insert(10,"python learning")
print(values)

values.insert(11,"list data types")
print(values)


# (insert data tye at end )no matter how many indexes we have in this case we have to add data type into list

values.append("end laziness")
print(values)

values.append(20)
print(values)

# update values

values[7]="KONDERU"
values[3]=6
print(values)
values[8]="VIJESH"
values[9]="K"
print(values)

#delete the data types in list
del values[4]
print(values)
del values[5]
print(values)

values[4]=7
print(values)



