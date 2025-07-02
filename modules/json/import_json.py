# 2_7_25
import json
name=input("Enter your name:")
age= int(input("Enter your age:"))
data ={
    "name":name,
    "age": age
    }
with open("user.json",'w') as f:
    json.dump(data,f)

with open("user.json",'r') as f:
    loaded = json.load(f)
    print(f'Read the file: {loaded}')