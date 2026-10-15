# Take user input for age, remove extra spaces, and convert it to an integer
a=int(input())

# Check the age category using if-elif-else statements
b="Child"
c="Teenager"
d="Adult"
e="Senior"
# Dont forget to output in uppercase
if a>=0 and a<=12:
    print(b.upper())
elif a>=13 and a<=19:
    print(c.uppper())
elif a>=20 and a<=64:
    print(d.upper())
elif a>=65:
    print(e.upper())
else:
    print("INVALID AGE INPUT")