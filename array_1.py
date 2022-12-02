# ` problem 1. print your first and last name`
print("Hayden Hart")
print("\n")
#`problem 2. In the array.py create an array named
#  'cars' with the following elements in this order  ---- 
# Ford,Chrysler,Dodge,Ram,Jeep,Chevy,GMC` 
print("\n")
cars = ["Ford", "Chrysler", "Dodge", "Ram", "Jeep", "Chevy", "GMC"]

#`problem 3. print the array to the console`
print(cars)
print("\n")

#`problem 4. print the length of the array to the console `
print(len(cars))
print("\n")

#`problem 5. Append Buick to the Array`
cars.append("Buick")

#`problem 6. print the array to the console`
print(cars)
print("\n")

#`problem 7. Print the 4th element in the array (Not index 4, element 4)`
print(cars[3])
print("\n")

#`problem 8. Insert 'Toyota' into element 3 in the array`
cars.insert(2,"Toyota")

#`problem 9. print the array to the console`
print(cars)
print("\n")

#`problem 10. Remove element 5 of the array (hint look at options for pop())
cars.pop(4)

#`problem 11. print the array to the console`
print(cars)

print("\n")
#`problem 12. Sort the array in ascending order`
cars.sort()

#`problem 13. print the array to the console`
print(cars)
print("\n")

#`problem 14. Sort the array in descending order`
cars.sort(reverse=True)

#`problem 15. print the array to the console`
print(cars)
print("\n")
#`problem 16. create a variable called my_array_length with a value of
#the cars array length (spelling, capitilization, and spaces matter)`
my_array_length = len(cars)

#`problem 17. create a variable called array_string with a value of 
# 'The length of my array is ' (spelling, capitilization, and spaces matter)`
array_string = "The length of my array is"

#`problem 18. print array_string concatenated with my_array_length to the console.`
print(array_string, str(my_array_length))

# for each
# cars --> plural --> whole list
# car --> singular -- one element
print("\n")
cars.append("Kia")
element =1
for car in cars:    # len(cars) = 8     # len of list for (i = 0, i<cars.len, i++)
    print(element, car)
    element += 1 