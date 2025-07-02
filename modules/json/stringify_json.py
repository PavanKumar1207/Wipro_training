# 2_7_25
import json 
name=input("Enter your name:")
age= int(input("Enter your age:"))
data ={
    "name":name,
    "age": age
    }
stringify_json = json.dumps(data)
print(f"Seralised data of JSON",type(stringify_json))