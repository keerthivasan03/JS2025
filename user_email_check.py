import csv
#GIT check
file_name="C:\\Users\\keerthivasan.a\\user_emails.csv"
mail_dic={}
search_name=["Oleg" ,"Noel"]
def search(file_name):
    with open (file_name,"r") as cs:
        reader=csv.reader(cs)
        for row in reader:
            name=row[0].lower()
            mail_dic[name]=row[1]
    return mail_dic
def update(search_name):
    if len(search_name)<2:
        return "Error: No such record found"
    full_name=search_name[0]+" "+search_name[1]
    mail_dic=search(file_name)
    return mail_dic.get(full_name.lower(),"No name present")
def main():
    print(update(search_name))

if __name__=="__main__":
    main()
