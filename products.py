products = []
while True :
	name = input('please input products name:')
	if name == 'q':
		break
	price = input('please input products price:')
        products.append([name,price])
print(products)

for p in products:
	print(p[0],'price is',p[1])

import io 
with io.open('products.csv','w', encoding='utf-8') as f:
	f.write('products,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
