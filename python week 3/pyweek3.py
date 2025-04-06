"""temperature=7

if temperature >=40:
  print("It is a hot day")
elif temperature >20:
   print("It is a warm day")
elif temperature > 10:
   print("It is a code day")
else:print("We are all going to freeze")

#LOOPS
fruits= ["orange","apple","mango"]
         
for fruit in fruits :
 print(fruit)  :      

count=1
while count<=5:
  print(count)
  count +=1"""

def calculate_discount(price,dPercent):
  if  dPercent >= 0.2:
    Newp= price - ( dPercent* price) 
    return print(f"The discounted price is:${Newp:.2f}")
  else:print(f"No discount applied. The price remains: ${price:.2f}")

p= float(input("enter price:"))
dp=float(input("enter discount:"))

calculate_discount(p,dp)