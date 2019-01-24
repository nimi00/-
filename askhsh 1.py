def sumIntervals(l):
  #Μετραμε το μηκως του πινακα μεσα στην συναρτηση!
  x=len(l)
  m=[]
  k=0
  #Εντασουμε τα ακρα του καθε συνολου σε εναν αλλον πινακα!
  for i in range(0,x):
     p=l[i]
     m.extend([p[0],p[1]])
  
  z=[]
  #Εντασουμε σε εναν νεο πινακα ολα τα στοιχεια των συνολων!
  for i in range(0,2*x,2):
    for j in range(m[i],m[i+1]):
      z.extend([j])
      k=k+1
  #Ταξινομουμε τον πινακα για την καλυτερη επεξεργασια του!
  z.sort()
  #Μετραμε ποσα ειναι τα διαφορετικα στοιχεια του πινακα οπου αυτο θα ειναι και το αποτελεσμα που θελουμε!
  s=1
  for i in range(1,k):
    if z[i-1]!=z[i]:
      s=s+1
  return s
		
x=int(input("Dose posa diastimata tha doseis: "))
for i in range(0,x):
  #Διαβαζουμε τα ακρα των συνολων!
  a=int(input("Dose to aristero akro tou diastimatos: " ))
  b=int(input("Dose to deksio akro tou diastimatos: " ))
  p=[a,b]
  print ("Ena apo ta diastimata einai to: ",p)
  print(" ")
  if i==0:
    l=[p]
  else:
    l.extend([p])
print("Ta diastimata einai ta eksis: ",l)
print(" ")
#Εκτυπωνουμε το αποτελεσμα!
print("To apotelesma einai: ",sumIntervals(l))
