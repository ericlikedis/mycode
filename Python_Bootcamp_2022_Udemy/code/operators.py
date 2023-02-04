# Range function
for num in range(0,11,2):
    print(num)

# Enumerate function:
word = 'abcde'
for letter in enumerate(word):
    print(letter)

# Zip function:
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

# in keyword operator
d = {'mykey':345}
345 in d.values()

# min max 
mylist = [10,30,40,100]
min(mylist)
max(mylist)
print(mylist)

# Shuffling a list
from random import shuffle 
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

random_list = shuffle(mylist)
type(random_list)
print(random_list)

# Grabbing a random integer
from random import randint 
randint(0,100)
mynum=randint(0,100)
print(mynum)

# Accept user input
result = input('What is your name?: ')
print(result)