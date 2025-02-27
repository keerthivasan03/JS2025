import csv
filepath="C:\\Users\\keerthivasan.a\\csv_html.csv"
csv.register_dialect("csv_html",delimiter=",",skipinitialspace=True,strict=True)
with open (filepath,"w",newline="") as csv_html:
    header = ['Full Name', 'Email Address']
    data = [{'Full Name': 'Blossom Gill', 'Email Address': 'blossom@abc.edu'},
{'Full Name': 'Hayes Delgado', 'Email Address': 'nonummy@utnisia.com'},
{'Full Name': 'Petra Jones', 'Email Address': 'ac@abc.edu'},
{'Full Name': 'Oleg Noel', 'Email Address': 'noel@liberomauris.ca'},
{'Full Name': 'Ahmed Miller', 'Email Address': 'ahmed.miller@nequenonquam.co.uk'},
{'Full Name': 'Macaulay Douglas', 'Email Address': 'mdouglas@abc.edu'},
{'Full Name': 'Aurora Grant', 'Email Address': 'enim.non@abc.edu'},
{'Full Name': 'Madison Mcintosh', 'Email Address': 'mcintosh@nisiaenean.net'},
{'Full Name': 'Montana Powell', 'Email Address': 'montanap@semmagna.org'},
{'Full Name': 'Rogan Robinson', 'Email Address': 'rr.robinson@abc.edu'},
{'Full Name': 'Simon Rivera', 'Email Address': 'sri@abc.edu'},
{'Full Name': 'Benedict Pacheco', 'Email Address': 'bpacheco@abc.edu'},
{'Full Name': 'Maisie Hendrix', 'Email Address': 'mai.hendrix@abc.edu'},
{'Full Name': 'Xaviera Gould', 'Email Address': 'xlg@utnisia.net'},
{'Full Name': 'Oren Rollins', 'Email Address': 'oren@semmagna.com'},
{'Full Name': 'Flavia Santiago', 'Email Address': 'flavia@utnisia.net'},
{'Full Name': 'Jackson Owens', 'Email Address': 'jackowens@abc.edu'},
{'Full Name': 'Britanni Humphrey', 'Email Address': 'britanni@ut.net'},
{'Full Name': 'Kirk Nixon', 'Email Address': 'kirknixon@abc.edu'},
{'Full Name': 'Bree Campbell', 'Email Address': 'breee@utnisia.net'}]
    csv_data=csv.DictWriter(csv_html,dialect="csv_html",fieldnames=header)
    csv_data.writeheader()
    csv_data.writerows(data)

log_content = """\
May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (ac)
May 27 11:46:00 ubuntu.local ticky: ERROR: Timeout while retrieving information (ahmed.miller)
May 27 11:46:05 ubuntu.local ticky: INFO: Created ticket [#1235] (ahmed.miller)
May 27 11:46:10 ubuntu.local ticky: ERROR: Connection to DB failed (blossom)
May 27 11:46:15 ubuntu.local ticky: ERROR: Timeout while retrieving information (blossom)
May 27 11:46:20 ubuntu.local ticky: INFO: Created ticket [#1236] (bpacheco)
May 27 11:46:25 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (breee)
May 27 11:46:30 ubuntu.local ticky: INFO: Updated ticket [#1237] (britanni)
May 27 11:46:35 ubuntu.local ticky: ERROR: Permission denied while closing ticket (blossom)
May 27 11:46:40 ubuntu.local ticky: ERROR: The ticket was modified while updating (bpacheco)
May 27 11:46:45 ubuntu.local ticky: INFO: Updated ticket [#1238] (breee)
May 27 11:46:50 ubuntu.local ticky: ERROR: Ticket doesn't exist (flavia)
May 27 11:46:55 ubuntu.local ticky: ERROR: Timeout while retrieving information (ac)
May 27 11:47:00 ubuntu.local ticky: INFO: Created ticket [#1239] (enim.non)
May 27 11:47:05 ubuntu.local ticky: ERROR: Connection to DB failed (ahmed.miller)
May 27 11:47:10 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (ahmed.miller)
May 27 11:47:15 ubuntu.local ticky: ERROR: Permission denied while closing ticket (breee)
May 27 11:47:20 ubuntu.local ticky: ERROR: The ticket was modified while updating (enim.non)
May 27 11:47:25 ubuntu.local ticky: INFO: Updated ticket [#1240] (flavia)
May 27 11:47:30 ubuntu.local ticky: ERROR: Ticket doesn't exist (breee)
May 27 11:47:35 ubuntu.local ticky: INFO: Created ticket [#1241] (ahmed.miller)
May 27 11:47:40 ubuntu.local ticky: ERROR: Timeout while retrieving information (blossom)
May 27 11:47:45 ubuntu.local ticky: ERROR: Connection to DB failed (breee)
May 27 11:47:50 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (flavia)
May 27 11:47:55 ubuntu.local ticky: INFO: Updated ticket [#1242] (ac)
May 27 11:48:00 ubuntu.local ticky: ERROR: Timeout while retrieving information (enim.non)
May 27 11:48:05 ubuntu.local ticky: ERROR: Connection to DB failed (flavia)
May 27 11:48:10 ubuntu.local ticky: INFO: Created ticket [#1243] (enim.non)
May 27 11:48:15 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (blossom)
May 27 11:48:20 ubuntu.local ticky: ERROR: Permission denied while closing ticket (ahmed.miller)
May 27 11:48:25 ubuntu.local ticky: ERROR: The ticket was modified while updating (blossom)
May 27 11:48:30 ubuntu.local ticky: INFO: Created ticket [#1244] (flavia)
"""
filepath1="C:\\Users\\keerthivasan.a\\syslog.log"
with open(filepath1, "w") as file:
    file.write(log_content)

print("syslog.log file has been created successfully.")

import csv
import re
import operator
import os


print(os.path.exists("C:\\Users\\keerthivasan.a\\syslog.log"))
per_user={}
error={}

with open("C:\\Users\\keerthivasan.a\\syslog.log","r",newline="") as extract:
    #read=csv.reader(extract)
    for line in extract:
        searching=r"ticky: (INFO|ERROR): (.+) \(([\w.]+)\)"
        capture=re.search(searching,line)
        print(capture)
        #code, error_message, user=capture[1],capture[2],capture[3]
        code, error_message, user=capture.groups()
        if error_message not in error:
            error[error_message]=1
        else:
            error[error_message]+=1
        #error[error_message] = error.get(error_message, 0) + 1
        if user not in per_user:
            per_user[user]={'INFO':0,'ERROR':0}
        if code=="INFO":
            per_user[user]["INFO"]+=1
        elif code=="ERROR":
            per_user[user]["ERROR"]+=1
    print(error,per_user)
error_list=sorted(error.items(),key=operator.itemgetter(1),reverse=True)
#per_user_list=sorted(per_user.items(),key=operator.itemgetter(1,"ERROR"),reverse=False)
per_user_list=sorted(per_user.items(),key=operator.itemgetter(0))

with open("C:\\Users\\keerthivasan.a\\syslogerror.csv","w",newline="") as error_write:
    error_generate=csv.writer(error_write)
    error_generate.writerow(["Error","Count"])# this value is used to read below
    #error_generate.writerow([key, value] for key,value in error_list)
    for key,value in error_list:
        error_generate.writerow([key, value])
with open("C:\\Users\\keerthivasan.a\\syslogerror.csv", "r") as error_read:
        error_reader=csv.DictReader(error_read)
        for row in error_reader:
            
            print("Error:{}, Count:{} ".format(row["Error"],row["Count"]))
with open("C:\\Users\\keerthivasan.a\\syslogusers.csv","w",newline="") as user_write:
    user_generate=csv.writer(user_write)
    user_generate.writerow(["User","Info","Error"])
    #error_generate.writerow([key, value["INFO"],value["ERROR"]] for key,value in per_user_list)
    for key,value in per_user_list:
        user_generate.writerow([key, value["INFO"],value["ERROR"]])
with open("C:\\Users\\keerthivasan.a\\syslogusers.csv", "r") as user_read:
    user_reader=csv.DictReader(user_read)
    for row in user_reader:
        
        print("User:{}, Info:{}, Error:{} ".format(row["User"],row["Info"],row["Error"]))
        






