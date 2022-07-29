newlist = []
i = 1
while(i<11):
    newlist.append(i)
    i+=1
print(f'Lista nr1: {newlist}')

print(f'Lista nr 2: {[x+1 for x in range(10)]}')
