import random
temps = []
for i in range(7):
	temps.append(random.randint(26, 40))
print (temps)
DOTW = ['sunday', 'monday', 'tuesday', 'wednsday', 'thursday', 'friday', 'saturday']
print(DOTW)
good_days = 0
for i in range(7):
	if temps[i] % 2 == 0 :
		good_days = good_days + 1
print (good_days)

HT = max(temps)
HTD = 40
LT = min(temps)
LTD = 26
for i in range(7):
	print(DOTW[i], ":", temps[i])
