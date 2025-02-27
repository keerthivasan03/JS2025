#multiplication table
def multiplication_table(common):
    for x in range(11):
        final=common * x
        print(common, "X",  x, "= " + str(final))
multiplication_table(5)
#fizzbizz
for x in range(16):
    if (x%3==0) and (x%5==0):
        print(str(x)+ " fizzbizz")
    elif (x%3==0):
        print(str(x)+ " fizz")
    elif (x%5==0):
        print(str(x)+ " bizz")
    else:
        print(str(x)+ " Not divisible by both 3 & 5")
#countdigits
def count_digit(defie):
        digit=0
        if defie==0:
            digit=0
        while defie>0:
            defie=defie//10
            digit+=1
        return digit
print(count_digit(6578784))    
#largest digit
#output=0
def largest_digit(input):
    output=0
    for x in input:
        if int(x)>output:
            output=int(x)
    print(output)
largest_digit("75748549")

for x in range(1,10):
     counting=0
     for y in range(1,x+1):
          if x%y==0 and y!=0:
               counting+=1
     if counting==2:
      print("It is the Prime number: "+ str(x))

def factorial(num):
    incremen=1
    for q in range(1, num+1):        
            incremen*=q
    print(incremen) 
factorial(5)   

def pyramid(n):
     for x in range(1, n+1):
          for y in range(1,x+1):
               print("*", end="")
          print()
pyramid(5)

#def palindrome(s):
palindrome="121"
vari=""
for x in palindrome:
    vari=x+vari
print(vari)
if vari==palindrome:
    print(palindrome+ " It is a palindrome")
else:
    print(palindrome + " Is not a Palindrome number")
#palindrome("121")
#Reveresenumber

number=21
sum=0
for x in range(1, number+1):
     
     if x%2==0:
        sum+=x
        print(str(x) + " Is the even number")

print("Sum of all even numbers between 1 and "+str(number)+ " is: " +str(sum))

def reverse(number):
    store=""
    for x in number:
        store=x+store
    print(store)
reverse("keerthivsan")
