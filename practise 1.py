#Print a Multiplication Table
#Write a program that prints the multiplication table for a given number n. The table should go up to 10.
def input (num):
    # now i am setting the range
    for x in range(11):
        result= num * x
        # it wil calcualte till it reach the range-1
        print(str(x) + "X" + str(num) +"="+ str(result))
input(10)
#Sum of Even Numbers
#Write a program to calculate the sum of all even numbers between 1 and a given number n.
for x in range(1,11):
    #I have set the range fron 1 t 10 and below code will see the number whether it is divisible by 2 and the remainder is 0
    if x%2==0:
        print("Below are the even numbers " + str(x))
        #print (x)
#Reverse a Number
#Write a program to reverse a given number using a loop.
def reverse_digit(number):
    reverse=""
    for x in number:
        reverse=x+reverse
    print(reverse)
reverse_digit("14790")
#another way happen only in python
reverse_digit1="787979794546268"
print(reverse_digit1[::-1])
#Count Digits
#Write a program to count the number of digits in a given number.
def count_digit(digit):
    count=0
    if digit==0:
        count+=1
    while digit>0:
            digit=digit//10
            count+=1
    return(count)
print(count_digit(4324234237))
#Write a program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".
for x in range(101):
    if (x%3==0 and x%5==0):
        print(str(x)+ " FizzBizz")
    elif (x%3==0):
        print(str(x)+ " Fizz")
    elif (x%5==0):
        print(str(x)+ " Bizz")
    else:
    # if (x%3!=0 and x%5!=0):
        print(str(x)+" not divisible by 3 & 5")
#Prime Numbers in a Range
#Write a program to print all prime numbers between 1 and a given number n
def prime_number(num,num1):
    for x in range(num, num1):
        retur= 0
        for y in range(num,num1+1):
            if x%y==0 and y!=0:
                    retur+=1
        if retur==2:
            print(x)
print(prime_number(1, 11))

#Factorial of a Number
#Write a program to calculate the factorial of a given number using a loop.

def numeric(n,m):
    for x in range(n,m):
        final=1
        for y in range(n,m+1):
            final*= y
    print(final)
numeric(1,6)

#Pattern Printing
#Write a program to print the following pattern for a given number n.
def game(numm):
    for x in range(numm):
        for y in range(x+1):
            print("*" , end=" ")
        print()
game(5)

#Palindrome Check
def palidrome(number):
    reverse_check=""
    for x in number:
        reverse_check=x+reverse_check
    if reverse_check==number:
                print("It is palindrome")
    else:
            print("Not a palindrome")
        #return reverse_check
    print(int(reverse_check))
palidrome("1241")

#Find the Largest Digit
def largest(numeric):
    digit=0
    for y in numeric:
        if int(y)>digit:
            digit=int(y)
    return digit 
print(largest("12935"))
                       


    