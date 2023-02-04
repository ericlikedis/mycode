# The term 'iterable' means you can 'iterate' over the object
# For example, you can iterate over eevry character in a string, iterate over every object in a list, iterate over every key in a dictionary.

#  Syntax of a for loop

# my_iterable=[1,2,3]
# for item_name in my_iterable:
#     print(item_name)

mylist = [1,2,3,4,5,6,7,8,9,10]
# for num in mylist:
#     print('hello')
for num in mylist:
    # check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(list_sum)

# for loops with strings
myString = 'Hello world!'
for letter in myString:
    print(letter)

# for loops with strings
for _ in 'Hello world!':
    print(_)

tup = (1,2,3)
for item in tup:
    print(item)

# Tuple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]
len(mylist)
for item in mylist:
    print(item)

# Tuple unpacking example 2:
for (a,b) in mylist:
    print(a)
    print(b)

# unpacking certain items in a list 
mylist = [(1,2,3), (5,6,7),(8,9,10)]
for a,b,c in mylist:
    print(a)

# iterate through a dictionary
d = {'k1':1,'k2':2,'k3':3} # k1, k2, k3 = key # 1, 2, 3 = value
for key, value in d.items():
    print(value)

Num = input("Enter a Number: ") 
print (Num * 3 )
