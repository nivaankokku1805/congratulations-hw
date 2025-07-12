name = "Penguin"
age = 15
is_student = True
weight = 38.5



print("Name : ", name)
print("Data type of name is ", type(name))

print("Age : ", age)
print("Data type of age is ", type(is_student)) 

print("is_student :", is_student )
print("Data type of is_student is ", type(is_student))

print("Weight : ", weight)
print("Data type weight is ", type(weight))


print("\n After Type Casting ....")
age = str(age)
print(age)
print("Data Type of age is  " , type(age))

weight = int(weight)
print(weight)
print("Data type of Weight is", type(weight))


text = str(input("Enter a string:"))


revText = text[::-1]
text = revText

print("Reverce of given String is:")
print(text)
