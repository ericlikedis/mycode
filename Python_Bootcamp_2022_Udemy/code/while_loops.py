# Example while loop
x = 50
while x < 5:
    print(f'The current value of x is {x}')
#    x = x + 1
    x += 1

# Break, Continue, Pass
# We can use break, continue, and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:
# break: Breaks out of the current closest enclosing loop.
# continue: Goes to the top of the closest enclosing loop. 
# pass: Does nothing at all.

# Example of pass
x = [1,2,3]
for item in x:
    # comment
    pass
print('end of my script')

# Example of continue 
myString = 'Sammy'
for letter in myString:
    if letter == 'a':
        continue
    print(letter)

# Example of break
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x = x+1

i = 5
while True:
    if i % 0o11 == 0:
        break
    print(i)
    i += 1