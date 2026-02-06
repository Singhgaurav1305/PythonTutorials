# Program to find the data type of a value entered by the user
# It will always return string as input() function takes input in string format only. 
# We can convert it to other data types using type casting functions like int(), float(), etc.

a = input("Enter data type you want to check : ")
b = type(a)
print("your data type is : ",b)