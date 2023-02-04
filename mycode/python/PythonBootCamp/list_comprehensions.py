mystring = "hello"
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)

# more efficient way to compute this on a single line
mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

# Perform operations in one line for a list
mylist = [num**2 for num in range(0,11)]
print(mylist)