while True:
	try:
		price = float(input("Enter product price: "))
	except ValueError:
		print("Enter valid price")
		continue

	try:
		given_cash = float(input("Enter ammount of cash given by client: "))
	except ValueError:
		print("Enter valid ammount")
		continue

	if(given_cash < price):
		print("That's less than the price of the product")
	else:
		possible_changes = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
		number_of_particular_nominal = [0 for x in range(len(possible_changes))]
		change = (given_cash - price)
		while (change > 0):
			for index, x in enumerate(possible_changes):
				if x <= change:
					change = round(change-x,2)
					number_of_particular_nominal[index] += 1
					break

		for index, x in enumerate(number_of_particular_nominal):
			if x > 0:
				print("You need {} {}".format(x, possible_changes[index]))

			
