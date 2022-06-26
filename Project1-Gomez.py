print("This program will tell you if the triangle is an equilateral triganle or not")
number1 = int(input('Enter the length of the first side of the triangle : '))
number2 = int(input('Enter the length of the second side of the triangle : '))
number3 = int(input('Enter the length of the third side of the triangle : '))
if number1 == number2 and number1 == number3 and number2 == number3:
	print("This triangle is an equilateral triangle.")
else:
	print("This is NOT an equilaterial triangle.")
