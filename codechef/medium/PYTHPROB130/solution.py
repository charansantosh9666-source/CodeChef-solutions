activity,place=input().split()

favorite_activity=activity.upper()

favorite_place=place.upper()

num_friends,hours_spent=map(int,input().split())

print(f"You plan to go {favorite_activity} at the {favorite_place}.")
print(f"You will be joined by {num_friends} friends and will spend {hours_spent} hours there.")
