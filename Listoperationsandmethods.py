years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_years=[]

for year in years:
    if year.endswith("2023"):
        new=year.replace("2023","2024")
        updated_years.append(new)
    else:
        updated_years.append(year)
print(updated_years)

def start_year(start, end):
    return[n*n for n in range(start, end+1)]
print(start_year(2,3))

yeas = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
updated_yeas=[yer.replace("2023","2024") if yer.endswith("2023") else yer for yer in yeas]
print(updated_yeas)

def change_String(new_one):
    sing=""
    updated= new_one.split()
    for element in updated:
        sing+=element[1:]+ "-" + element[0] +" "
    return sing
print(change_String("1one 2two 3three"))

def add_one(number):
    return number+1
numbers = [1, 2, 3, 4, 5]
result = [add_one(number) for number in numbers]
print(result)  # Output: [2, 3, 4, 5, 6]

def add_two(two_number):
    return two_number+2
two_numbers=[1,2,3,4,5,6]
output=map(add_two, two_numbers)
print(list(output))

name=["keerthi","vasan","Harishwadha","Anu"]
age=(27,26,25,24)
finals=zip(name, age)
print(list(finals))