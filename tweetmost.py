
test_cases = int(input("Enter the number of Test Cases: "))
test_count = 0
while test_count < test_cases:
	tweet_names = []
	dict1={}
	num = int(input("Enter the number of each Test Case:"))

	count = 0
	while count < num:
		name = input("Enter the name followed by the Twitter ID (then press Enter:)")
		tweet_names.append(str(name))
		count += 1
	for names in tweet_names:
		l=names.split(' ')
		singlename = l[0]
		if singlename in dict1:
			dict1[singlename]= dict1[singlename]+ 1
		else:
			dict1[singlename]= 1

	list1= [ ]
	list1.clear()

	val1= 0
	for key,val in sorted(dict1.items()):
		if val1< val:
			val1= val

			list1.clear()
			list1.append(key)

		else:
			if val1== val:
				list1.append(key)
	list1.append(val1)

	print(' '.join(str(x) for x in list1))
	test_count += 1
	tweet_names.clear()
