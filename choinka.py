h = 6

if(h%2==0):
    znak = "*"
else:
    znak = "#"

for i in range(h):
    print(" "*(h-(i+1)), znak *(i*2+1))

