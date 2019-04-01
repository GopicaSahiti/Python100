#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gallons_cost = float (input ("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
tgc = gallons_used * gallons_cost
cpm = gallons_used / tgc
mpg = round(mpg, 1)
cpm = round(cpm,1)


            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost :\t\t" + str(tgc))
print("Cost per Mile :\t\t\t" + str (cpm))
print()
print("Bye")


