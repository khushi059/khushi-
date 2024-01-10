#ques1
name=input("Enter your name: ")
if name:
    print("Hello %s!"%name)
else:
    print("Hello Stranger!")
    
#ques2
password=input("Enter Password: ")
password_check=input("Confirm Password: ")
if password==password_check:
    print("Password Set!")
else:  
    print("Sorry! Wrong password try again")

#ques3
password=input("Enter Password: ")
if ((len(password)>=8)and(len(password)<=12)):
    password_check=input("Confirm Password: ")
    if password==password_check:
        print("Password Set!")
    else:  
        print("Sorry! Wrong password try again")
else:
    print("Sorry you entered less than 8 characters or more than 12 characters")
    
#ques4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password=input("Enter password: ")
if password in BAD_PASSWORDS:
    print("You cannot have this password!")
else:
    password_check=input("Confirm Password: ")
    if password==password_check:
        print("Password Set!")
    else:  
        print("Sorry! Wrong password try again")

#ques5
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while(True):
    password=input("Enter Password: ")
    if password in BAD_PASSWORDS:
        print("You cannot have this password!")
        continue
    else:
        if ((len(password)>=8)and(len(password)<=12)):
            password_check=input("Confirm Password: ")
            if password==password_check:
                print("Password Set!")
                break
            else:  
                print("Sorry! Wrong password try again")
                continue
        else:
            print("Sorry you entered less than 8 characters or more than 12 characters")
            continue
        
#ques6
for i in range(0,13):
    mul=i*7
    print("%d X 7 = %d" %(i,mul))
    
#ques7
num=int(input("Enter the number for times table: "))
for i in range(0,13):
    mul=i*num
    print("%d X %d = %d" %(i,num,mul))
    
#ques8
num=int(input("Enter the number for times table: "))
if num>0:
    for i in range(0,13):
        mul=i*num
        print("%d X %d = %d" %(i,num,mul))
else:
    for i in range(12,-1,-1):
        mul=i*num
        print("%d X %d = %d" %(i,num,mul))
        
