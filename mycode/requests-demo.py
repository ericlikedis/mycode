import requests
# Insert web address here:
x = requests.get('')

print(x.headers)
print(x.headers['Server'])
print(x.status_code)

if x.status_code==200:
    print("Success!")
if x.status_code==404:
    print("Not found!")

print(x.elapsed)
print(x.cookies)