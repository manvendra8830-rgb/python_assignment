#  grade of Student

Students = {
    "Rahul" : "B",
    "Sachin": "A",
    "kunal" : "B"
}
# Add New Students

name = input("Enter the name : ")
grade = input("Enter your garde : ")

Students[name] = grade

#upadte new student

name = input("Enter your update students : ")
if name in Students:
    grade =input("Enter upadte grade : ")
    Students[name]=grade
else:
    print("Students not found! ")

print("\nAll student grades ..") 

for name,grade in Students.items():
    print(name, ":",grade)