'''product=1
for n in range(1,10):
    product=product*n
print(product)

def to_celsius(x):
  return (x-32)*5/9
for x in range(0,100,10):
   print(x, to_celsius(x))

for n in range(1,15,6):
   print(n)

for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

teams={"keerthi","vasan","Anu","Harishwadha"}
for home_teams in teams:
   for away_teams in teams:
      if home_teams!=away_teams:
         print(home_teams, "vs", away_teams)

greetin="hello"
for cha in range(len("greeting")):
   print(cha)

waste= "Keerthivasan"
index=0
while index<len(waste):
   print(waste[index:index+1])
   index+=1

numbers = [1, 2, 3, 4, 5, 8]
squared_numbers = [x ** 2 for x in numbers]
#print(squared_numbers)
for x in numbers:
   sq=[x**2 for x in numbers]
   print(sq)
greetin="hello"
print(greetin[::-3])

def format_phone(phonenum):
    area_code = (" ( " + phonenum[:3] + " )" )
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line
print(format_phone("2025551212")) # Outputs: (202) 555-1212

def friend_list(friends):
    for friend in friends:
        print("hi "+ friend)
friend_list('Bobby')
friend_list(['bobby'])

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y) )
    print("Exit inner loop")

for x in range(7):
    if x % 2 == 0:
        print(x)

# The loop should print 0, 2, 4, 6

# As a list comprehension:
even_numbers = [x for x in range(7) if x % 2 == 0]
print(even_numbers)

sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)

for n in range(10):
  print(n+n)

input = "Four score and seven years ago"
for c in input:
  if c.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(c)
input1="KEerthivasan"
print([c for c in input1 if c in ['a','e','i','o','u']])
print([c for c in input1 if c.lower() in ['a', 'e', 'i', 'o', 'u']])

def factoril(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factoril(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factoril(3)

for x in range(10):
    for y in range(x):
        print(y)
        
for sum in range(5):
    sum = sum+sum
    print(sum)
    
x = 1
sum = 0
#for x in range(10):
while x <= 10:
    sum += x
    x += 1
print(sum)

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(rows): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x+1): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        print()


rows_asterisks(5)
'''
def digits(n):
    count = 0
    if n == 0:
        count += 1  # If n is 0, it has 1 digit.
    while n > 0:  # While n is greater than 0, keep dividing by 10
        n = n // 10  # Perform integer division to remove the last digit
        count += 1  # Increment the count for each digit
    return count

# Test cases
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1