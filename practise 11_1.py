square_numbers=[n*n for n in range(1,11)]
print(square_numbers)
even_numbers=[n for n in range(1,11) if n%2==0]
print(even_numbers)
even_odd_numbers=["even" if n%2==0 else "odd" for n in range(1,11)]
print(even_odd_numbers)
falttened_list=[[1,2],[3,4],[5,6]]
return_list=[final for sublist in falttened_list for final in sublist] 
print(return_list)
"""falttened_list1=[[1,2],[3,4],[5,6]]
save_list=[]
for flat_list in falttened_list1:
    for save_lists in flat_list:
        save_list.append(save_lists)
print(save_list)
"""

list_1=[1,2,4,5,6]
list_2=[1,4,7,8]
common=[lists for lists in list_1 if lists in list_2]
print(common)

list_3=[1,2,4,5,6]
list_4=[1,4,7,8]
common=[]
for lis in list_3:
    if lis in list_4:
        common.append(lis)
print(common)

reverse=["hello", "world", "python"]
return_output=[rev[::-1] for rev in reverse ]
print(return_output)

"""reverse = ["hello", "world", "python"]
for i in range(len(reverse)):
    reverse[i] = reverse[i][::-1]  # Reverse each string in the list
print(reverse)
"""  

divisible=[5, 15, 25, 35, 45, 41]
div_5_10=[divisib+10 for divisib in divisible if (divisib%5==0)]
print(div_5_10)
"""
divisible1=[5, 15, 25, 35, 45, 41]
for d in divisible1:
    if d%5==0:
        res=d+10
        print(res)

"""

