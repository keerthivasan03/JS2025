
#!/usr/bin/env python3
import sys
import csv
import unittest
#argv = ["Oleg" ,"Noel"]
filename = "C:\\Users\\keerthivasan.a\\user_emails.csv"
def populate_dictionary(filename):
    """Populate a dictionary with name/email pairs for easy lookup."""
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            name = str(row[0]).lower()
            email_dict[name] = row[1].lower()
    return email_dict
"""#1
def find_email(argv):
    if len(argv)<2:
        return "Error: Not enough arguments. Usage: script.py FirstName LastName"
    fullname=argv[0]+" "+argv[1]
    email_dict=populate_dictionary(filename)
    return email_dict.get(fullname.lower(),"No name present")"""
#2
def find_email(argv):
# Return an email address based on the username given
# Create the username based on the command line input.
    try:
        fullname = str(argv[0] + " " + argv[1])
    # Preprocess the data
        email_dict = populate_dictionary(filename)
    # Find and print the email
        return email_dict.get(fullname.lower(),"No email address found")
    except IndexError:
        return "Missing parameters"
"""#3
def find_email(argv):
    # Return an email address based on the username given
   # Create the username based on the command line input.
    try:
        fullname = str(argv[0] + " " + argv[1])
        # Preprocess the data
        email_dict = populate_dictionary(filename)
        # If email exists, print it
        if email_dict.get(fullname.lower()):
          return email_dict.get(fullname.lower())
        else:
          return "No email address found"
    except IndexError:
            return "Missing parameters"
"""
def main():
    print(find_email(["Oleg" ,"Noel"]))

if __name__ == "__main__":
    main()

class Testsearch(unittest.TestCase):
    def test_search(self):
        testcase=["Oleg" ,"Noel"]
        excepted="noel@abc.edu"
        self.assertEqual(find_email(testcase),excepted)
    def test_search1(self):
        testcase1=["Oleg"]
        excepted1="Missing parameters"
        self.assertEqual(find_email(testcase1),excepted1)
    def test_two_name(self):
        testcase = ["Roy","Cooper"]
        expected = "No email address found"
        self.assertEqual(find_email(testcase), expected)
    
if __name__=="__main__":
    unittest.main()


