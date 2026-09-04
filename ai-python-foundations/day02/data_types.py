print('==========LIST===========')

list1 = [50, 61.65, 1.0+3.0j, 0b1010, 0o10007, 0xB109F, True, "string", [2, 87.23, False], 
        (4, "slice"), {"name": "Python", "age":36}, {7, 50.72, "set"}, None]
print(list1)
a = list1[6]
print(a)
b = list1[-4]
print(b)
print(type(list1[11]))
print(type(list1))
print(list1[0:9])
print(list1[:6])
print(list1[1:])
print(list1[0:14:2])
print(list1)
list1[0]=25
print(list1[0])
print(list1)


print('===========TUPLE===============')
tuplee = (1, 6.7, "yes", False, ("care", 3, True, None))
print(tuplee)
print(type(tuplee))

a1=tuplee[4]
print(a1)

tup1 = (2, 56, "tuple", "set")

a2 = tuplee + tup1
print(a2)

print('===========Dictionary==========')
dict1 = {'name': 'python', 'age': 36, 'city': "Hyderabad"}
print(dict1)
print(type(dict1))

b1 = dict1['name']
print(b1)

dict1["city"] = 'Delhi'
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

D = dict([("name", "Nani"), ('age', 45), ('DOP', 'Kerock')])
print(D)

D1 = dict(name='Mahesh Babu', age=49)
print(D1)

D2 = {'name': 'Nani', 'age': 45, 'DOP': 'Kerock', 'name': 'Arjun'}
print(D2)


print('===========set========')
Set = {4, 65, 4, "Set", 90, (1, 'AK477',5), 1, 90}
print(Set)
print(type(Set))

##Iterating Strings, list, tuple, dictionary, set

String="Adivi sesh"
new_string = ""
for ch in String:
    new_string = new_string + ch*2
print("new_string", new_string, sep='-->>')


List=[1, 25.45, True, 0b101]
New_List = []
for el in List:
    New_List.append(el*2)
print("New_List", New_List, sep='-->>')


Tuple = (2, 'hi nana', 45.23, False, [8, 98.2, 'Hulek'], 67)
New_list = []
New_tuple = ()
for el in Tuple:
    New_list.append(el*2)
New_tuple=tuple(New_list)
print("New_tuple", New_tuple, sep='-->>')


Set = {5, 25.26, "Set", 76}
New_Set = set()
for num in Set:
    New_Set.add(num*2)
print("New_Set", New_Set, sep='-->>')


Dictionary = {"name": "Koutla", 'pincode': 500110, 'Mdl': 'Sarangapur'}
New_Dict = {}
for key in Dictionary:
    New_Dict[key] = Dictionary[key]
print("New_Dict", New_Dict, sep='-->>')


New_Dict1 = {}
for key,value in Dictionary.items():
    New_Dict1[key] = value
print("New_Dict1", New_Dict1, sep='-->>')


for key, value in Dictionary.items():
    print(f"{key}:{value}")

for k in Dictionary:
    print(k)

for key in Dictionary:
    print(key)

for key in Dictionary.keys():
    print(key)

for value in Dictionary.values():
    print(value)