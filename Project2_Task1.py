N=int(input("Enter the Nth term upto which the fibonacci numbers must be generated:"))
print("the fibonacci numbers:\n")
for s in range(0,2):
    print(s,"\n")
a=0;
b=1;
for j in range(0,N-2):
    s=a+b;
    print(s,"\n")
    a=b;
    b=s;
    

