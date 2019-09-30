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
print(products) #print [['Name1', 'Price1'], ['Name2', 'Price2']]

for p in products:
	print(p)    #print['Name1', 'Price1']
				#print['Name2', 'Price2']
	#print(p[0]) #print first of name & product
				#Only print name
	print(p[0], 'price is: ',p[1])