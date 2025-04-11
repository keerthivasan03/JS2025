def liner(list_of_name,key):
    for i,x in enumerate(list_of_name):
        if x==key:
            return i
    return -1
reuult=liner(["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor","Keerthi"],"Keerthi")
print(reuult)
#import this
string_seperation="KeerThi vasan"
update=string_seperation.lower()
string_dic={}
for updates in update:
    if updates!=" ":
        if updates in string_dic:
            string_dic[updates]+=1
        else:
            string_dic[updates]=1
print(string_dic)

count_vowels="Keerthivasan"
vowels='aeiouAEIOU'
sums=0
for charac in count_vowels:
    if charac in vowels:
        sums+=1
print(sums)

count_vowel="Keerthi vasan"
vowel='aeiouAEIOU'
vowels_dic={}
for counting in count_vowel.lower():
    if counting!=" ":
        if counting in vowel:
            if counting in vowels_dic:
                vowels_dic[counting]+=1
            else:
                vowels_dic[counting]=1
for key, value in vowels_dic.items():
    print(key, ":", value)

fp="C:\\Users\\keerthivasan.a\\python programming\\cogni.txt"
with open(fp, "r") as file:
    lines = file.readlines()
    for line in lines:
        num = line.strip()
        print(num[::-1])  # Reverse the string

"""nums = [1]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # ❌ StopIteration


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (make sure chromedriver is in your PATH or specify the path)
driver = webdriver.Chrome()

# Open the webpage containing the table
driver.get("https://www.w3schools.com/html/html_tables.asp")  # Sample table for testing

# Give time to load the page
time.sleep(2)

# Locate all the rows in the table (excluding the header)
rows = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")

# Initialize an empty list to hold all row data
table_data = []

# Loop through each row
for row in rows:
    # Find all the cells (either <td> or <th>) in the current row
    cells = row.find_elements(By.XPATH, "./th | ./td")

    # Extract text from each cell using a for loop
    row_data = []
    for cell in cells:
        row_data.append(cell.text)

    # Add the row data to the table_data list
    table_data.append(row_data)

# Print the table as a 2D array
for row in table_data:
    print(row)

# Close the browser
driver.quit()"""

def linear_search(list,key):
    for i, item in enumerate(list):
        if item==key:
            return item, key, i
    return  -1
result=linear_search(["Keerthi", "Vasan", "Anu", "renuga", "Ashona", "Swathi", "kamesh", "Deekshitha", "Sarvesh" ], "Swathi")        
print(result)
