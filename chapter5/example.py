student={
    "name":"sagar",
    "age":20,
    "course":"computer science",
    "is_enrolled":True,
    0:"sohan"          #string ya integer dono use kar sakte hai keys me
}

print(student["name"])
print(student["age"])


# adding a new keys values pair
student["grade"]="A"
# updating a value
student["age"]=21
# deleting a keys values pair
del student["course"]
# print the updated dictionary
print(student)                     #{'name': 'sagar', 'age': 21, 'is_enrolled': True, 0: 'sohan', 'grade': 'A'}



