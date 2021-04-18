def most_frequent(n):
    def count(y):
        c=0
        for z in ll:
            if y==z:
                c+=1
            else:
                continue
        return c
    def getkey(k):
        for key,value in d.items():
            if k==value:
                if key not in li2:
                    return key
    ll=list(n)
    d={}
    for i in ll:
        x=count(i)
        u=ll.index(i)
        d[ll[u]]=x
    li1=list(d.values())
    li1.sort(reverse=True)
    li2=[]
    for j in li1:
        v=getkey(j)
        li2.append(v)
    d1={}
    for l in range(len(li2)):
        d1[li2[l]]=li1[l]
    for key,value in d1.items():
        print(key,":",value)
word=input("Please enter a string ")
most_frequent(word)
