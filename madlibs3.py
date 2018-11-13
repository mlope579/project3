choice = input("Do you Want to play a game? (y) or (n)- Enter option between quotation marks:")
while choice == "y":
	while True:
		print("1. Mad Lib 1")
		print("2. Mad Lib 2")
		print("3. Mad Lib 3")
		print("4. Mad Lib 4")
		print("5. Mad Lib 5")
		print("6. Mad Lib 6")
		print("7. Mad Lib 7")
		print("8. Mad Lib 8")
		print("9. Mad Lib 9")
		print("10. Mad Lib 10")
		
		choice2 = int(input("Which template of madlib would you like to play(Enter the number of your choice): "))
		break
		
	if choice2 == 1:
	# Mad Lib 1
	   adjective = raw_input("Enter an adjective, please: ")
	   print("Flip-flops are a staple of any {} summer wardrobe.".format(adjective))

	if choice2 == 2:
	# Mad Lib 2
	   article_of_clothing = raw_input("Enter an article of clothing, please: ")
	   print("My gym locker always stinks because I'm always leaving my dirty {} in there.".format(article_of_clothing))

	if choice2 == 3:
	# Mad Lib 3
	   verb1 = raw_input("Enter a verb, please: ")
	   print("This hot water makes me want to {} on the beach all day long.".format(verb1))

	if choice2 == 4:
	# Mad Lib 4
	   adjective1 = raw_input("Enter an adjective, please: ")
	   print("Life is too {} not to wear a bikini on spring break!.".format(adjective1))

	if choice2 == 5:
	# Mad Lib 5
	   type_of_liquid = raw_input("Enter a type of liquid, please: ")
	   print("Spring break poolparties are just like the ones you used to have when you were a kid... except with way more {}!".format(type_of_liquid))

	if choice2 == 6:
	# Mad Lib 6
	   plural_noun1 = raw_input("Enter a plural noun, please: ")
	   print("Nobody loves spring flowers more than me, except maybe bumble-  {}.".format(plural_noun1))

	if choice2 == 7:
	# Mad Lib 7
	   number1 = raw_input("Enter a number, please: ")
	   print("One margarita, two margarita, {} margaritas, floor!".format(number1))

	if choice2 == 8:
	# Mad Lib 8
	   noun2 = raw_input("Enter a noun, please: ")
	   print("BBQ at my house! Everyone's invated, and it's Bring Your Own {}!".format(noun2))

	if choice2 == 9:
	# Mad Lib 9
	   type_of_food = raw_input("Enter a type of food, please: ")
	   print("My Favorite way to flirt is to ask if I can have a bite of your {}!".format(type_of_food))

	if choice2 == 10:
	# Mad Lib 10
	   plural_noun2 = raw_input("Enter a plural noun, please: ")
	   print("My heart is filled with love and {}".format(plural_noun2))
	   
	else:
		choice = "n"
		print("Goodbye")