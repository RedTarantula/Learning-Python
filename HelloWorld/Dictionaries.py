import os
os.system('clear')

favorite_animals = {
	"John":"Chicken",
	"Joshua":"Dragon",
	"Prime":"Renamon"
}

print(favorite_animals)
print(favorite_animals["John"])

del favorite_animals["John"]

print(favorite_animals)

favorite_animals.update({"Vyse":"Wolf"})

favorite_animals["Prime"] = "Cat"

print(favorite_animals)

favorite_animals.update({"John":["Chicken","Bat","Tarantula"]})

print(favorite_animals)
print(favorite_animals["John"][1])