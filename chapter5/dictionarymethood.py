student={
    "name":"vidya",
    "age":20,
    "course":"cse"
}
print("keys:",student.keys())       #keys: dict_keys(['name', 'age', 'course'])
print("values:",student.values())     #values: dict_values(['vidya', 20, 'cse'])
print("items:",student.items())       #items: dict_items([('name', 'vidya'), ('age', 20), ('course', 'cse')])

print("Name:",student.get("name"))     # Name:vidya
print("Grade:",student.get("grade"))    # Grade: None
student.update({"age":21,"grade":"A"})
print(student)       #{'name': 'vidya', 'age': 21, 'course': 'cse', 'grade': 'A'}
student.pop("grade")
print(student)      # {'name': 'vidya', 'age': 21, 'course': 'cse'}
student.popitem()
print(student)      #{'name': 'vidya', 'age': 21}    removes last insertd item
student.setdefault("gender","Female")
print(student)                        #{'name': 'vidya', 'age': 21, 'gender': 'Female'}


copied_student=student.copy()
print("copied_student",copied_student)     #copied_student {'name': 'vidya', 'age': 21, 'gender': 'Female'}
student.clear()
print(student)    #output:{}