import re

file_name=input("enter file name ").lower()
try:
    with open(file_name,"r") as file:
        data=file.read()
except:
    print(file_name," not found")
    exit()
emails=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",data)

print("Email founds")
for email in emails:
    print(email)