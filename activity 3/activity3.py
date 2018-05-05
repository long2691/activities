

#dictionary can contain multiple pair of information 
dict1 = {"name" : "long", "age": ['27'], "hobbies": ["games","food","drinking"], "wakeuptimes": {"key": [8.00,6,30,7.00]}}
print(dict1["name"])
print(dict1["hobbies"])
print(dict1["wakeuptimes"]["key"][3])

#drews solution
drew = {
    "name":"drew",
    "age": "85",
    "hobbies": ["coding","reading"],
    "wake_up": {"mon":5, "tues":5, "sat":7}
}
print("hello I am " + drew["name"] + "my age is" + str(drew["age"]))

for hobby in drew["hobbies"]:
    print(hobby)
for time in drew["wake_up"].values():
    #print(time + " " + str(drew["wake_up"][time]))
    print(time)
for k,v in drew["wake_up"].items():
    print(k)
    print(v)