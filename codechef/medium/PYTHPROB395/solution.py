# Step 1: Declare the messy address with leading symbols
messy_address = "####123 Baker Street"

c=messy_address.lstrip('#')
print(c)
print(len(c))