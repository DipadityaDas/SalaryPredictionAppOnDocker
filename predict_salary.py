from joblib import load

# Loading the Machine Learning Model
model = load("SalaryModel.pkl")

# Infinite Loop for the Prediction prompt
print("************ Salary Prediction App On Docker ************\n")
while True:
	# Taking the User Input
	experience = float(input("Enter your Years of Experience : "))
	result = model.predict([[experience]])

	# Rounding up the result to 2 Decimal Place
	salary = round(*result, 2)

	# print("Estimated Salary of the Employee : {0}{1}\n".format("\u20B9", salary))
	print("Estimated Salary of the Employee : {0}{1}\n".format("$", salary))

	# Taking User Input for further Prediction
	choice = input("Do you want to continue [y/N]: ")
	if (choice == "N" or choice == "n"):
		break
	elif(choice == "Y" or choice == "y"):
		print()
	else:
		break
