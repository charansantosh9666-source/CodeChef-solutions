# Take user input for traffic light color and process it
main_light = input( )

# Take user input for blinking light color
blinking_light = input( )

# Check the light color and determine the action using 'or' operator
if main_light == "red" or blinking_light == "flashing red":
    print("Stop")  
elif main_light == "yellow" or blinking_light == "blinking yellow":
    print("Slow Down")  
# Update the code below this line
elif main_light=="green" or blinking_light =="blinking green" :
    print("Go")
else:
    print("Invalid input")