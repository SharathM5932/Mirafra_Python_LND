data="stuffed toy teddy, special one, toy teddy, love toy, teddy bear, pink teddy,red teddy, Mr. teddy, my bear, love bear, deer, gift me"
l1=list(filter(lambda x:'teddy' in x , data.split(',')))
print("Dear Surya,")
print(f"Total {len(l1)} teddies are there. And, here they are:")
print(l1)