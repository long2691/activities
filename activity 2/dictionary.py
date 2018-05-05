lst = ["a", "b", "c"]

item = {"key": 100}
#dictionary name key
item2 = {"name":"drew"}
print(item["key"])
print(item2["name"])

#dictionary can contain multiple pair of information 
hero = {"name": "iron man", "nationality":"united states", "type": False}
item3 = {"bag" : ["laptop", "usb", "food"], "pocket": [5.00,1.00,'gum'], "reddit": {"key": [1,2,3,4,]}}
print(item3["bag"])
print(item3["pocket"])
print(item3["reddit"]["key"][3])

for keys in item3:
    print (keys)