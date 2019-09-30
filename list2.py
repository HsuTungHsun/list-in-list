products = []   #Big list
while True:
	name = input('Enter products name: ')
	if name == 'q':
		break
	price = input('Enter products price: ')
	#p = []  #Creat little list in big list
	#p.append(name)   #Put name string into p list
	#p.append(price)  #Put price string into p list
	#p = [name, price] #Equal to line 7 to 9 
	#products.append(p) #Put little list into big list
	products.append([name, price]) #Equal to line 10 to 11
print(products)
