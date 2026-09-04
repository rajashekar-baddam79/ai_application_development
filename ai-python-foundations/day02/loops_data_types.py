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