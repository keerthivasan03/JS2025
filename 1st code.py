'''
poda: int="fsdf"
print("abc"+"8.5")
a=12
b=15
c=a/b
print("D is "+ str(c))
a = "10"  # String
b = 5     # Integer
result = int(a) + b  # Explicitly converting `a` to an integer
print(result)   # Output: 15
print(type(result))

import typing
list_of_number: typing.Set[int]={"name", 1,2,4}
print(list_of_number)

def keerthi(vasan, married):
    print("Good bug" + vasan)
    print("Python" + married)
keerthi("poda", "dai")
keerthi("nothing", "much")

name="Keerthi"
print("He is a good but he is so " ,name, "waste fellow not wrth for " ,100)
print(type(name))
sort_number={11,2,3,4,5,5,6,7,8,9.12}
print(sorted(sort_number))
print(min(sort_number))
print(max(sort_number))

def keerthi(vasan, poda):
    return vasan*poda
    nmae=keerthi(10,15)
nnnn=keerthi(11,12)
mmmm=nmae+nnnn
print(mmmm)

def greeting(koe):
    return koe 
    print("Poda day " + koe)
result= greeting("vdad dai")
print(result)


def calculation(name):
    number=len(name)*9
    print("Hello"+ name+ "your lucky number is "+ str(number))
calculation("keerthivasan")
calculation("Harishwadha")

def nne(radious):
    num=radious * 9
    print("nmon of gfihdfd: " + str(num))
    #return nne
nne(10)

def moo(asd):
    k=asd*8
    print("papspas " + str(k))
moo(10)



print("CAT" > "cat")
print(1+8 == 6+3)


def keerthi(goodbuy):
    if len(goodbuy) > 5:
        print("Not good buy")
    else:
        print("good buy")
keerthi("Keerthivasan")
keerthi("asn")
    
def number(integer):
    if(integer%2==0):
        print("Positive")
    else:
        print("no positive")
number(10)
#above code I have give print so value is printed and in below code i have given only return value so we need to value to print

def numm(quu):
    if (quu % 2 == 0):
        return True
    return False
print(numm(10)) # one way
#another way to print
result= numm(10)
print(result)
'''
def rank(numerical):
    if numerical<=5:
        print("Toppers in class")
    elif numerical <10:
        print("medium students")
    else:
        print("need to compete with all students")
rank(3)
rank(5)
rank(7)
rank(10)
rank(25)

def rank(name):
    if name== "keerthi":
        glass = "number 1"
    elif name== "vasan":
        glass ="number5"
    elif name=="anu":
        glass ="Number 2"
    elif name=="hari":
        glass ="number 4"
    else:
        glass="Nmae is not present in the list"
    return glass
results= rank("hari")
print(str(results) +  " is the class topper")

def sprint_28(story_number):
    if story_number==9876:
        assignee="Keerthivasan"
    elif story_number==9999:
        assignee="Rangarajan"
    elif story_number==9786:
        assignee="keerthivasan"
    else:
        assignee="Mentioned story number is not in this Sprint"
    return assignee
assigned_story=sprint_28(9786)
print("Assigned to "+ assigned_story)

