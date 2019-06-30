first_number=input("Please enter the first number: ")
second_number=input("Please enter the second number: ")


if first_number.isdigit() and second_number.isdigit() == True:
	operation=input("You are good to go... Please pick an operation to proceed (*,-,+,/): ")
	if operation=="*":
		print("Your result = %d" % (int(first_number)*int(second_number)))
	elif operation=="-":
		print("Your result = %d" % (int(first_number)- (second_number)))
	elif operation=="+":
		print("Your result = %d" % (int(first_number) + (second_number)))
	elif operation=="/":
		print("Your result = %d" % (int(first_number) / int(second_number)))
	else:
		print("Please enter a valid operation: ")
else:
	print("Please choose valid numbers only... quiting calculator")
