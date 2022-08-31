import json
from operator import truediv
import requests

url = "https://raw.githubusercontent.com/Alt-Shivam/Codecs-Registry/main/codec.json"

# Getting Remote Json content and loading it to local variable.
r = requests.get(url)

# Dataset is a dictionary
DataSet=(r.json())

name = input("Enter the codec name you want to search  ")
name2=name.lower()

pointer=False
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
        pointer=True
        break

if pointer==False:
    print("Codec not found in registry.")
    print("You can request to add the same by this link:")
    print("https://alt-shivam.github.io/Codecs-Registry/Others/AddNewCodec.html")


if pointer==True:
    Choice=input("Do you want to learn more about the codec and how to use it? (y/n)")
    url2 = "https://raw.githubusercontent.com/Alt-Shivam/Codecs-Registry/main/Examples.json"
    s = requests.get(url2)
    DataSet2=(s.json())
    if Choice=="y":
        for i in DataSet2:
            temp=i['CodecName']
            temp2=temp.lower()
            if name2==temp2:
                print("CodecID:",i['CodecID'])
                print("How to use this codec:")
                print(i['UseCase'])
    else:
        print("thanks for using this registry.")
