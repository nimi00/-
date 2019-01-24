def zero():
	x=0
	return x
	
def one():
	x=1
	return x
	
def two():
	x=2
	return x
	
def three():
	x=3
	return x
	
def four():
	x=4
	return x
	
def five():
	x=5
	return x
	
def six():
	x=6
	return x
	
def seven():
	x=7
	return x
	
def eight():
	x=8
	return x
	
def nine():
	x=9
	return x
	
def plus(x,y):
	#Αθροισμα των αριθμων
	z=x+y
	return z
	
def minus(x,y):
	#Αφαιρεση των αριθμων
	z=x-y
	return z
	
def times(x,y):
	#Πολλαπλασιασμος των αριθμων
	z=x*y
	
	return z
	
a = input("Dose enan arithmo me olografos:	")
b = input("Dose thn praksi me olografos:	")
c = input("Dose enan deutero arithmo olografos:	")
print ("H praksi einai h eksis:(",a,"(",b,"(",c,")))")
s=a
t=[0,0]
for i in range (0,2):
	if s=="zero":
		t[i]= zero()
	elif s=="one":
		t[i]= one()
	elif s=="two":
		t[i]= two()
	elif s=="three":
		t[i]= three()
	elif s=="four":
		t[i]= four()
	elif s=="five":
		t[i]= five()
	elif s=="six":
		t[i]= six()
	elif s=="seven":
		t[i]= seven()
	elif s=="eight":
		t[i]= eight()
	else:
		t[i]= nine()
	s=c
	
x=t[0]

y=t[1]

if b=="plus":
	z= plus(x,y)
elif b=="minus":
	z= minus(x,y)
else:
	z= times(x,y)
print("To apotelesma einai:",z)
		
	
