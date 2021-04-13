#Positive numbers in a range
n=input("Enter the Numbers:")
l1=list(map(int,n.split()))
print("The positive numbers from ",l1,"are:\t")
s=""
for j in l1:
    if j>0:
        print(j)
        s=s+" "+str(j)
if 0 in l1:
    print("Note:Zero is neither negative nor positive")
l2=list(map(int,s.split()))       
print("The list of positive numbers from ",l1,"is:",l2)
