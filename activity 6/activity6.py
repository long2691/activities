# generate list of 100 people
my_list = list(range(100))

# let the killing begin
while len(my_list) != 1:
    # remove the even indices by slicing if length of list is even
    if len(my_list) % 2 == 0:
        del my_list[1::2]
    # otherwise remove even indices by slicing AND dropping first value if length of list is odd
    else:
        del my_list[1::2]
        my_list.pop(0)

# return value + 1 to correct value offset
print("The survivor is person: ", my_list[0] + 1) 

# output: 73