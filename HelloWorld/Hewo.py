import os
os.system('clear')

'''
Multi line commenting

DATA TYPES
- Strings
- Numbers
- Lists
- Tuples: static list, it's faster
- Dictionaries
- Booleans


'''

# Single line commenting
print("Hewo World! OWO") 

full_name = "John"
age = 21
animals = ["Tarantula", "Rooster"] # list
pokemon = ("Seviper", "Blaziken") # truple
yoink = False

fav_animal = {
"John":"Rooster",
"Todd":"Tiger",
"Jax":"Frog"
	
}

print(full_name)
print(fav_animal["John"])


s = "Yoinking \"poopy\" haha very fucking \n FUNNY"
print(s);

s = "hello, my name is " + full_name;
print(s);
print(s.upper());
print(s.lower());
print(s.capitalize());
print(s.title());
print(s.swapcase());
print(len(s)); # length of the string
print(s[3])
print(s[0:5]) # doesnt include 5th
print(s.split(" "))
print(s.split(" ")[2])


i = 1
f = 10.10

print(i)
print(float(i))
print(f)
print(int(f))

print(5**5) # Power of
print(9%3.5) # Returns remainder
