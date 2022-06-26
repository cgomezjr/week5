print("This program will tell you if the triangle is an right triganle or not"
      "\n\nEnter the lengths smallest to largest")
number1 = int(input("Enter the lengths of all three sides of the triangle: "))
number2 = int(input("Enter the lengths of all three sides of the triangle: "))
number3 = int(input("Enter the lengths of all three sides of the triangle: "))
if number1**2+number2**2==number3**2:
	print("This triangle is an right triangle.")
else:
	print("This is NOT an right triangle.")
