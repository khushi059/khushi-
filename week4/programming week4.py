#ques1
result = lambda x : "True" if x>=0 and x<=100 else "False"
print(result(1))
print(result(101))

#ques2
def count_upper_lower(string):
    lowercase_letter_count = 0
    uppercase_letter_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1

    print(uppercase_letter_count, lowercase_letter_count)
count_upper_lower("Hello")


#ques3  
name=input("Enter your name: ")
if name:
    name=name[0].upper()+name[1:].lower()
    print("Hello %s!"%name)
else:
    print("Hello Stranger!")
    
#ques4   
str=input("Enter a string: ")
# str="Hey how are you\n"
def remove_last(str):
    print(str)
    if len(str)>1:
        str=str.strip()
        str=str[:-1]
    else:
        str=str
    print(str)
    return str
remove_last(str)


#ques5
def c_to_f(temp):
    temp = float(temp)
    f = (temp * 1.8) + 32
    result = (f"{temp}C is equivalent to {f}F")
    return result

def f_to_c(temp):
    temp = float(temp)
    c = (temp - 32) / 1.8
    result = (f"{temp}F is equivalent to {c}C")
    return result

print(c_to_f(30))
print(f_to_c(86))

#ques6
def conversion():
    userinput = str(input("Enter temp: "))
    if "C" in userinput or "c" in userinput:
        list = [userinput]
        seprated_list = [i for i in list[0]]
        seprated_list[-1:] = []
        joined_list = "".join(seprated_list)
        temp = float(joined_list)
        f = (temp * 1.8) + 32
        result = (f"{temp}C is equivalent to {f}F")
        return result
    else:
        result = "Something went wrong !"
        return result
    
print(conversion())

#ques7
from statistics import mean

def maths(a,b,c,d,e,f):
    list = [a,b,c,d,e,f]
    max_value = max(list)
    min_value = min(list)
    mean_value = mean(list)
    print("The max Value is", max_value)
    print("The min Value is", min_value)
    print("The mean Value is", mean_value)
    return None

maths(1,2,3,4,5,6)

#ques8
from statistics import mean

def maths():
    list = []
    while(True):
        user_input = str(input("Enter numbers or press enter to end: "))
        list.append(user_input)
        if user_input == "":
            break
        else:
            continue
    list[-1:] = []
    new_list = [int(i) for i in list]

    max_value = max(new_list)
    min_value = min(new_list)
    mean_value = mean(new_list)
    print("The max Value is", max_value)
    print("The min Value is", min_value)
    print("The mean Value is", mean_value)
    return None

maths()

