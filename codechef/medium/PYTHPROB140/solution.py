user_input = input() 

city, visits = user_input.split()

city = city.strip()

visits = int(visits.strip())


print(f"Your favorite city is: '{city}', and you want to visit it {visits} times.")