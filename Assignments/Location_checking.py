import re
city_names={'Bangalore':560000,'Hyderabad':500000,'Chennai':600000,'Mumbai':400000}
def loc_check(location):
    for i in city_names:
        if i in location :
           print(city_names[i])
           print("Your delivery package reach in 1 or 2 days.")
           break
    else:
        print("Sorry Can't reach")




while True:
    location = input("Enter Your location:")
    loc_check(location)