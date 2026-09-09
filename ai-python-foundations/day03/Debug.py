Students = ["Ravi", "Anil", "Kiran", "Suresh"]
found=False
for i in range(len(Students)):
    if Students[i]=="Kiran":
        print("student found", Students[i], sep='-->>')
        found=True
        break
if not found:
    print("Student not found")


Students = ["Ravi", "Anil", "Kiran", "Suresh"]
found=False
for student in Students:
    if student == "Kiran":
        print("student found", student, sep='-->>')
        found=True
        break
if not found:
    print("student not found")


Students = ["Ravi", "Anil", "Kiran", "Suresh"]
if "Kiran" in Students:
    print("student found-->>Kiran")
else:
    print("Kiran not found")