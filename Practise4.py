def reverse_number(reversing_number):
    store=""
    for x in reversing_number:
        store=x+store
    print(store)
reverse_number("1235435")

multiplication=5
for x in range(1,11):
    multi=multiplication*x
    print(x , "* ", multiplication, "= ", multi)

sum=0
for x in range(0,11):
    if x%2==0:
        print(x,  "is the even number")
        sum+=x 
print(sum)

digit=13298743243
largest=0
"""if digit==0:
    largest+=1
"""
while digit>0:
    digit=digit//10
    largest+=1
print(largest)

for x in range(1,16):
    if(x%3==0) and (x%5==0):
        print(x, " FizzBizz")
    elif(x%3==0):
        print(x, " Fizz")
    elif(x%5==0):
        print(x, " Bizz")
    else:
        print(x, " Not divisible by 3 & 5")


for x in range(1,16):
    count=0
    for y in range(1,x+1):
        if y!=0 and x%y==0:
            count+=1
    if count==2:
        print(y)

factorial=3
result=1
for x in range(1, factorial+1):
    result*=x
print(result)

pattern=4
for x in range(1, pattern+1 ):
    for y in range(1,x+1):
        print("*", end="")
    print()

def palindrome(n):
    reverse=""
    for x in n:
        reverse=x+reverse
    print(reverse) 
    if reverse==palindrome:
        print(n, " is a palindrome number")
    else:
        print(n, "Is not a palindrome number")  
palindrome("128") 

def largest_digit(a):
    divi=0
    for q in a:
        if q==0:
            divi=0
        if int(q)>divi:
            divi=int(q)
    print(divi)
largest_digit("14735")

revers="12343243"
print(revers[::-1])

#course
name="Keerthivasan is a good boy"
new_name= name[0:12] + " is not"+ name[15:]
print(new_name)

news="Keerthivasan is a good boy"
print(news.index("n"))
nee= news[0:12]
print(nee)


pets="Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
print(pets.index("s"))
print("Cats" in pets)

keerthivasan="KeerThivasan"
print(keerthivasan.upper())

print(" yes ".strip())
print(" kk Yes ".lstrip())
print(" yes ".rstrip())

print("keerthivasan".count("e"))
print("Forest".endswith("rests"))
print(("This is not fair").split())

name="keerthi"
initial="A"
print("my name is {} . {}".format(name,initial))

name="keerthidsds"
initial="Adsds"
print("my name is {names} . {initials}".format(names=name,initials=initial))