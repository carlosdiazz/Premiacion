from datetime import datetime

print('Tuesday, April 19, 2022')
fechaHOY = datetime.today().strftime('%A, %b %d, %Y')
fechaHOY2 = datetime.today().strftime('%A, %B %d, %Y')
fechaHoy3 = datetime.today().strftime('%a %m/%d/%y')

#print(fechaHOY)
print(fechaHOY2)
#print(fechaHoy3)