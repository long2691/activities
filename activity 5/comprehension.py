prices = ["24", "13", "16000", "1400"]
price_nums = [int(price) for price in prices]
print(prices)
print(price_nums)

dog = "poodle"
letters = [letter for letter in dog]
print(letters)
print(f"we iterate over a string into al ist : {letters}")

capital_letters = [letter.upper() for letter in letters]
#long version of same thing above
capital_letters = []
for letter in letters:
        capital_letters.append(letter.upper())

no_o = [letter for letter in letters if letter != 'o']
print(no_o)
#same as abvoe but longer - no o's
no_o = []
for letter in letters:
    if letter != 'o':
        no_o.append(letter)

june_temperature = [72,65,59,87]
july_temperature = [87,85,92,79]
august_temperateure = [88,77,66,100]
temperature = [june_temperature, july_temperature, august_temperateure]
lowest_summer_temperature = [min(temps) for temps in temperature]
lowest_summer_temperature = []
print(lowest_summer_temperature)
for temps in temperature:
        lowest_summer_temperature.append(min(temps))

print(sum(lowest_summer_temperature)/len(lowest_summer_temperature))
print(lowest_summer_temperature)
print(lowest_summer_temperature[0])
print(lowest_summer_temperature[1])
print(lowest_summer_temperature[2])
print("=" * 30)
#longhand

def name(parameter):
    return "Hello" + parameter
def average(data1,data2):
    return sum(data)/len(data1) + (sum(data2)/len(data2))
print(name("Loc"))
print(Average([1,2,3,4,5],))

#git status 
#git add .
# git status
# git commit -m "Description comment"
# git push origin master
