import json
data = {
    "name": "Rajashekar",
    "age": 24,
    "city": "Hyderabad",
    "skills": ["Python", "Django", "REST API"]
    }

file = open('output.json', 'w')
json.dump(data, file)
file.close()