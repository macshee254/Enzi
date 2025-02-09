# prompt the user for two numbers
from selectors import SelectSelector

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# prompt user to enter operator
operator=input("Enter an operator (+,-,*,/):")
# perform calculation based on operators
if operator =="+":
    result=(num1 + num2)
elif operator == "-":
    result=(num1 - num2)
elif operator == "*":
    result=(num1 * num2)
elif operator == "/":
    if num1%num2==0:
        result=(num1/num2)
    else:
     result=("Error divisible by zero")

else:
    result = "Invalid operator"
print(f"The answer is {result}")
