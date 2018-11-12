num = int(input("Enter an integer to check if it is prime (value must be greater than 1!): "))

for i in range(2, num):
	if(num%i) ==0:
		print("False")
		break
else:
	print("True")