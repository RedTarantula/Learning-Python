import os
os.system('clear')

# CONDITIONAL STATEMENTS

num = 5

if(num > 10):
	print("Woah!") # Tabs are important!!!
elif(num == 10):
	print("Not bad, kid")
else:
	print("Pathetic")


if (num > 10) and (num < 100):
	print("How specific")


# LOOPS

counter = 0

while (counter <= 10):
	print(counter)
	counter+=1


names = ["John","Bob","Mary"]

for n in names:
	print(n)

fav_species = {
"John":"Chicken",
"Joshua":"Dragon"
}

for key,value in fav_species.items():
	print(key + " - " + value)