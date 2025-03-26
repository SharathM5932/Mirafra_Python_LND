loc_add={'hyderabad':[500001,],'bangalore':560002,'collem':403410,'vizag':530001}
print('Enter the full address or just city name: ')
k=input()
found=False
add=k.split(',')
for i in add:
    city=i.strip().lower()
    if city in loc_add:
        print(f"City: {city} \nPostal Code: {loc_add[city]}")
        print("We can reach you in time...")
        found=True
        break
if not found:
    print("Sorry, we do not deliver to your location at the moment.")



