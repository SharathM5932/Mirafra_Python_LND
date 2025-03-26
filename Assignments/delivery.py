data={'Bangalore':'560000','Hyderabad':'500000','Chennai':'600000','mumbai':'400000'}
print('Enter the full address or just city name: ')
address=str(input())
for i in data:
    if i in address:
        print(f'Postal code is:,{data[i]} \n')

        print('We can reach you in time')
        break
    else:
        print('\n')
        print('Sorry! the product cannot be delivered to the address you are entering.')
        break