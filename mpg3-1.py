#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

# get input from the user
choice = "y"
while choice.lower() == "y":
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    gallons_cost = float (input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon

        print()
        mpg = round((miles_driven / gallons_used), 2)
        tgc = round((gallons_cost * gallons_used),2)
        cpm = round((gallons_cost / mpg),1)
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ",tgc)
        print ("Cost Per Mile:             ",cpm)
    choice = input("Get entries for another trip? (y/n): ")
    print()

print("Bye")
