# First Python Program when you stated a 
print("Hello Faizan Welcom to the python .I am the Powerhouse of Programming in the world")
# Variable in puthon
# There are three Basic Variable use in python around all  the wordld
# Int => That are use to print integers like  x=20
# Float => That are use to print the decimal number in console and use any function
# string => That are use to print the any  text word pargraph any person name place city country etc in console
# Example of three types
# Int Varriable
x=20
i=2.2
name="Sir Yasir"
print(type(x))   
print(type(i))
print(type(name))

# Python list 
# That is work to stored in one bracket lots of data in python caleed lsit but in javascript 
# called in array python list and  array work it same only name differnce

# See few Examples
fruits=['apple', 'mango','orange']
name=['Yasir','Asad','Adeel Ahmed']
students=['Ali','Faizan','asad']
print(students[2])
print(name[2])
print(fruits[0])

# input statement
name=input("Enter Your name")
print("Hello"+ name + "welcome to the jumanji")

# Arthermatic Operates in python
# equailty =>  "="
# inequality => "!="
# Greater then = ">"
# less then    => "<"
# Green then equal to => ">="

# if statement in python few example with operaters
age=20
if age>=20:
    print("True")
if age==24:
   print("True")
if age<=8:
    print("True")
    # control flow
    # else sataement short from in  elif
# elif allowed to check multiple condition in statement
score=90
if score>=80:
    print("Well")
elif 89 <= score <89 :
    print("Nice")
else:
   print("You can do better ")
#    lops 
# Two types of loops main
# while
# for
# see example
count=0
for counter in range(5 ):
    count+=counter
    print(count)
score = 0        # <-- Initialize 'score' first
scores = 1       # Optional, will be overwritten anyway

while score in range(6):  # Equivalent to: while score < 6
    scores = score + 1
    print(scores)
    score += 1
# loop control statemets
number=['1','2','3']
for num in number:
    if num==3:
        continue
    if num==5:
         break
    print(num)

# half slides
# Python functions

def greet(names):
    print("my name is"+names)


greet("Alice")
# file handling concep in python
# file opening method
# opening a file for read
file=open("example.txt","r")
content=file.read()
print(content)
file.close()
# using python few libraries
# Importing NumPy
import numpy as np
numbers=[2,3,4,5,5,7]
arr=np.array(numbers)
total=np.sum(arr)
avg=np.mean(arr)
maxs=np.max(arr)
print("Array",arr)
print("total",total)
print("average",avg)
print("Greater number",maxs)
# Importing Pandas​

import pandas as pd



# Creating a DataFrame​

data={'Name':['Yasir'],'Age':[23],'Student':['it']}
df=pd.DataFrame(data)
print(df)
# Importing Matplotlib​

import matplotlib.pyplot as plt



# Creating a simple plot​

x = [1, 2, 3, 4, 5]

# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)


# plt.show()

# python api fetch data
import requests
response = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2025-05-04&sortBy=publishedAt&apiKey=099f9b807cd0468a84cbf6844face9a7')

data = response.json()

print(data)
# Importing the Random module​

import random


# Generating a random number between 1 and 10​

random_number = random.randint(1, 10)

print("Random Number:", random_number)