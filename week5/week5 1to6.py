#ques1
goes = 0
for goes in range(10):
    print(goes)
    
goes = 0
while True:
    print(goes)
    goes += 1
    if goes == 10:
        break
    
#ques2
from sys import argv
print(len(argv)-1)

#ques3
from sys import argv
list = argv[:]
list.sort(key=len)
print(list)
try:
    print(f"The shortest word is: {list[0]}")
except:
    print("word is not passed")
    
#ques4
from sys import argv
from urllib.request import urlopen
from urllib.error import *
try:
    user_link = argv[1]
    link = urlopen(user_link)

except IndexError as i:
    print("No url Provided and", i)
    
except HTTPError as h:
    print("HTTP error", h)

except URLError as u:
    print("Opps ! Page not found!", u)

else:
    print("Yeah ! Page found")

#ques5
from sys import argv
from statistics import mean

try:
    list = argv[1:]
    new_list = [(int(i)) for i in list]

    max_value = max(new_list)
    min_value = min(new_list)
    mean_value = mean(new_list)


except IndexError as i:
    print("No string provided and", i)
   
except ValueError as v:
    print("No Argument Provided", v)

except NameError as n:
    print("No Argument Provided", n)

else:
    print("The max Value is", max_value)
    print("The min Value is", min_value)
    print("The mean Value is", mean_value)
    
#ques6
from shutil import copyfile
from sys import argv
origin_filename=None
try:
    origin_filename = argv[1]
    filename, extension = origin_filename.split('.')

    target_filename = (f"{filename}_backup.{extension}")

    copyfile(origin_filename, target_filename)
except IndexError as i:
    print('file name is not given.', i)
except ValueError as v:
    print("Cannot find file extension.", v)
except FileNotFoundError as f:
    filename=origin_filename
    print(f"Cannot open {filename}.", f)
    