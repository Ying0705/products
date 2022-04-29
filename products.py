products = []
while True :
	name = input('please input products name:')
	if name == 'q':
		break
	price = input('please input products price:')
	p = []
	p.append(name)
	p.append(price)
        products.append(name)
        products.append(p)
print(products)
