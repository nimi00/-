import random
k=0

flag="true"
p=['1','2','3','4','5','6','7','8','9']
#Ο 1ος παικτης θα εχει ως συμβολο 'Χ' και ο 2ος ως συμβολο 'Ο'!
z='X' 
#Αρχικοποιηση της τριλιζας οπου το 'r' σημαινει κενο! 
for i in range (0,9):
   p[i]=" "
#Εκτυπωση της τριλιζας για καθοδηγηση των παικτων οσο αφορα τα κελια!
print (' 1 | 2 | 3' )
print ('-----------')
print (' 4 | 5 | 6 ')
print ('-----------')
print (' 7 | 8 | 9 ')
print ("-------------------------------------------")
#Αρχη του παιχνιδιου   
while k<=9 and flag=="true":
   k=k+1
   if z=='X':
       print ('Play the player')
       x=int(input ('Dose keli:' ))
   else:
      print ('Play the computer')
      x= random.randint(1,9)
   
   if (x<1 or x>9):
      while (x<1 or x>9):
         #Ελεγχος για υπαρκτο κελι.Υπενθυμιζεται οτι τα κελια ειναι απο 1 μεχρι 9 και αν δοθει λαθος κελι τοτε ο παικτης πρεπει να ξαναδωσει κελι!
        x= int(input ("Edoses lathos keli. Dose xana!" ))
   while p[x-1]!=' ':
      #Ελεγχος για το αν ο παικτης η ο υπολογιστης εδωσε δεσμευμενο κελι!
      if z=='X':
	 
         x=int(input ('Edoses keli desmeumeno. Dose allo keli'))
      else:
        
        x= random.randint(1,9)
     
   p[x-1]=z
   #Ελεγχος αν υπαρχει νικητης!
   if (k>=5 and((p[0]==z and p[1]==z and p[2]==z)or (p[3]==z and p[4]==z and p[5]==z)or(p[6]==z and p[7]==z and p[8]==z)or(p[0]==z and p[3]==z and p[6]==z)or(p[1]==z and p[4]==z and p[7]==z)or (p[2]==z and p[5]==z and p[8]==z)or(p[0]==z and p[4]==z and p[8]==z) or(p[2]==z and p[4]==z and p[6]==z))):
     if z=='X':
       print ('Winner the first player!!!')
     else:
       print ('Winner the computer player!!!')
     flag="false"
   #Αλλαγη συμβολου για να παιξει ο αλλος παικτης!
   if  z=='X':
     z='O'
   else:
     z='X'
  #Εκτυπωση της τριλιζας για καθε γυρο για να εχουν οι παικτες σε τι κατασταση βρισκονται!
   print (p[0],'|',p[1],'|',p[2])
   print ('-----------')
   print (p[3],'|',p[4],'|',p[5])
   print ('-----------')
   print (p[6],'|',p[7],'|',p[8])
   print ("--------------------------------------")
