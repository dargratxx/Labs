#1
int_int = int(input("enter an integer: "))
int_float = float(input("enter a float: "))
int_str = input("enter a string: ")
sum_result = int_int + int_float
print(f"the sum of {int_int} and {int_float} is {sum_result}")
print(f"types: {type(int_int)}, {type(int_float)}, {type(int_str)}")

#2
txt = "456"
numInt = int(txt)
numFloat = float(numInt)
numStr = str(numInt)

print(f"integer: {numInt}, float: {numFloat}, string: {numStr}")
print(f"types: {type(numInt)}, {type(numFloat)}, {type(numStr)}")

#3
person = {
    "name": "John",
    "age": 25,
    "hobbies": ["reading", "basketball", "sleeping"],
}
print(f"name: {person['name']}, age: {person['age']}")
print(f"hobbies: {', '.join(person['hobbies'])}") #объединение элементов

#4
mySet = {1, 2, 3}
mySet.add(4)
mySet.remove(2)

print(f"Updated Set: {mySet}")
print(f"Set contains {len(mySet)} elements.")
