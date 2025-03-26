
'''#encode ans decode
str='𝕻yꓕhoฅ'
print('string',str)
str1=str.encode()
print("encode:",str1)
str2=str.encode(encoding='UTF-8',errors='ignore')
print('ignore',str2)
str3=str.encode(encoding='ascii',errors='replace')
print('replace',str3)'''

#Q1
n=int(input())
j=str(n)
k=j+j
h=j+j+j
sum=int(k)+int(j)+int(h)
print(sum)

#Q2
import math
def rad(r):
    return math.pi*(r**2)
r=int(input())
print(rad(r))

#Q3
print('''a string in which you "don't have to use
new line
or tab.........is called as
Dash string---------> example''')

#Q4
print('''Twinkle,twinkle,little star,
\t How I wonder what you are?
\t\tUp above the world so high
\t\tLike a diamond in the sky
Twinkle, twinkle, little star
\tHow I wonder what you are?''')

