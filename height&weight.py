weight = int(input("Enter weight"));
height = float(input("Enter height"));
x = weight/float(height*height);
if x < 18.5:
    print("underweight")
if x>=18.5 and x<25:
    print("Normal")
if x >=25 and x < 30:
    print('Overweight')
if x >= 30:
    print('Obesity')