# ques1
name=input("Hello, what is your name? Mr.")
print("Hello Mr.%s Good to meet you!"%name)

#ques2
celsius = float(input('Enter temperature in Celsius: '))
fahrenheit = (celsius * 1.8) + 32
print('%0.1fC is equivalent to %0.1fF'%(celsius,fahrenheit))

#ques3
no_of_total_students=int(input("Enter number of students? "))
no_of_stu_per_group=int(input("Required group size? "))
no_of_group=no_of_total_students//no_of_stu_per_group
no_of_left_out=no_of_total_students-(no_of_group*no_of_stu_per_group)
print("No of Groups with %d Students each: %d"%(no_of_stu_per_group, no_of_group))
if (no_of_left_out<=1):
    print("No of Left Out Student: ", no_of_left_out)
else:
    print("No of Left Out Students: ", no_of_left_out)

#ques4
no_of_sweets=float(input("Enter number of sweets: "))
no_of_pupils=float(input("Enter number of pupils attending: "))
no_of_sweet_per_person=no_of_sweets//no_of_pupils
no_of_left_over=no_of_sweets%no_of_pupils
print("Sweet per person to be distributed %d left over sweets %d"%(no_of_sweet_per_person, no_of_left_over))
