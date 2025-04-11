input_str = "Ram:89,Lakshman:75,Hanuman:92"

"""result = {v: k for k, v in (item.split(":") for item in input_str.split(","))}

# Split by comma, then split each by colon and reverse key-value

print(result)
"""
results={v:k for k,v in (item.split(":") for item in input_str.split(","))  }
print(results)
new_dict={}
score=0
person=""
for items in input_str.split(","):
        k,v = items.split(":")
        new_dict[v]=k
        if int(v)>score:
            score=int(v)
            person=k
            
print(new_dict)
print(score , ":", person)

nested_list = [1, [2, [3, 4]], 5]
flattened_list = []

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)
        else:
            flattened_list.append(item)

flatten(nested_list)
print(flattened_list)
flist = [[1, 2], [3, 4], [5, 6]] 
nlist=[]
for x in flist:
    for y in x:
        nlist.append(y)
print(nlist)

list1 = [1, 7, 3, 4, 2, 5, 6]
n=len(list1)
for x in range(n):
     for y in range(n-x-1):
          if list1[y]>list1[y+1]:
               list1[y],list1[y+1]=list1[y+1],list1[y]
print(list1)

lst = [11, 1, 2, 3, 15]

# Swap first and last using index
lst[0], lst[-1] = lst[-1], lst[0]

print(lst)  # Output: [15, 1, 2, 3, 11]
