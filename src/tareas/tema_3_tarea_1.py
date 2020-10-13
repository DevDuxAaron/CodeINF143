import datetime

x = datetime.datetime.now()
for i in range(10**5):
	pass
y = datetime.datetime.now()

print(x.strftime("%f"))
print(y.strftime("%f"))
print(int(x.strftime("%f")) -  int(y.strftime("%f")))