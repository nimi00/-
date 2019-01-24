a=int(input("Dose to aristero akro tou diastimatos: " ))
b=int(input("Dose to deksio akro tou diastimatos: " ))
d=int(input("Dose enan akeraio arithmo: "))
t=[]
k=0
#Ευρεση των πρωτων αριθμων μεσα στο διαστημα που δοθηκε
for i in range (a,b+1):
        flag="false"
        j=2
        while j<i and flag=="false":
            if i%j==0:
			#Αν η συνθηκη δεν ισχυσει ποτε τοτε σημαινει οτι ο αριθμος του i ειναι πρωτος αριθμος
                flag="true"
            j=j+1
		#Αποθηκευουμε ολους τους πρωτος αριθμους στον πινακα t
        if flag=="false":
                t.extend([i])
                k=k+1

flag="false"
i=1
#Περνα ολους τους πρωτους αριθμους του διαστηματος μεχρι να βρει το ζευγαρι των πρωτων που θα εχουν διαφορα ιση με d
while i<k and flag=="false":
        j=0
        while j<i and flag=="false":
                if t[i]-t[j]==d:
                        flag="true"
                        print ("To zeugari pou psaxneis einai to [",t[j],",",t[i],"]")
                j=j+1
        i=i+1
#Αν τελικα δεν βρεθηκε καποιο ζευγαρι θα ισχυσει η παρακατω συνθηκη
if flag=="false":
        print ("Den vrethikan se ayto to diasthma protoi arithmoi me diafora ish me",d)
        
