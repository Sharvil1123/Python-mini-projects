import secrets



b = int(input("Enter the amount of digits --> "))
c= secrets.token_hex(b)
print(c)
print(type(c))

