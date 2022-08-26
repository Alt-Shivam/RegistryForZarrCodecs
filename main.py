import json
import requests

url = "https://raw.githubusercontent.com/Alt-Shivam/Codecs-Registry/main/codec.json"

# Getting Remote Json content and loading it to local variable.
r = requests.get(url)

# Dataset is a dictionary
DataSet=(r.json())

name = input("Enter the codec name you want to search  ")
name2=name.lower()

for i in DataSet:
    temp=i['CodecName']
    temp2=temp.lower()
    if name2==temp2:
        print("Codec found in registry...")
        print("Details are as follows for ",name2)
        print("CodecID:",i['CodecID'])
        print("Type:",i['Type'])
        print("Description:",i['Description'])
        print("Last Updated on",i['LastUpdate'])
        print("To know more about the codec, please visit this registry.")
        print("https://alt-shivam.github.io/Codecs-Registry/")
        break