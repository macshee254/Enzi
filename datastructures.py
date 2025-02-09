# list datastructure
# list are mutable
# list are ordered
#list are indexed
fruits= ['apple', 'banana', 'mango','orange', 'pineapple', 'pear', 'lemon', 'peaches', 'grapes']
fruits[0]= "watermelon"
numbers= [1,2,3,4,5,6,7,8,9]
number2=[67,5,2,-7,0,13,5,1,23,3,-5,-4]
number2.sort(reverse=True)
print(number2)
print(fruits)
numbers.append(11)
print(numbers)

print(f"I love eating {fruits[2]}")
# tuple datastructures
# tuples are immutable(unchanged)
# tuples are ordered
# tuples are indexed
cars=('audi', 'toyota', 'mercedes', 'honda', 'hyundai', 'subaru')
print(cars)
nambari=(43,5,87,2,1,-1,-99,-100,-2345,9,0)
# nambari.sort(reverse=True)
print(sorted(nambari))
# set datastructure
# set are unordered
# set are not indexed
computers={'hp', 'dell', 'lenovo', 'ibm', 'acer', 'toshiba', 'mac'}
computers.add('google')
computers.remove('ibm')

print(computers)
num1={1,2,3}
num2={4,5,6}
union_set=num1.union(num2)
print(union_set)
# dictionary data structure
student={'Name':'John', 'Age':5, 'Gender':'Male', 'School': "University of Nairobi"}
print(student['Name'])
print(f"Student name: {student['Name']}")
