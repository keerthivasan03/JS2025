
import csv
csv_l="C:\\Users\\keerthivasan.a\\Downloads\\contact_info.csv"
csv_c="C:\\Users\\keerthivasan.a\\OneDrive - Protiviti Member Firm\\Desktop\\Sprint 27\\8743.csv"
fil=open(csv_c)
csv_open=csv.reader(fil)
for row in csv_open:
    name,phone, role,a,d,s,f,g,h,j,k= row
    print("{} is the vaue {} {} {}{}{}{}{}{}{}{}".format(name,phone, role,a,s,d,f,g,h,j,k))

lis= [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
fil_l="C:\\Users\\keerthivasan.a\\Book.csv"
with open(fil_l,"w") as shop:
    writin=csv.writer(shop)
    writin.writerows(lis)
colu="C:\\Users\\keerthivasan.a\\contact_info.csv"
with open(colu) as column:
    rr=csv.DictReader(column)
    for row in rr:
        print("{} is the role {} of the person {} whose phone number is".format(row["role"],row["name"],row["phone"]))

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
fil_1="C:\\Users\\keerthivasan.a\\Book_1.csv"
with open(fil_1,"w") as row_column:
    dic=csv.DictWriter(row_column,fieldnames=keys)
    dic.writeheader()
    dic.writerows(users)
