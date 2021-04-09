filename=input("Enter the File name:")
i=filename.index('.')
ext=filename[i+1:]
di={"py":"Python","m":"matlab","doc":"document","jpg":"image","sch":"Pspice schematics","mp4":"video","mp3":"audio"}
for j in di:
    if j==ext:
        print("The extension of the file is:",di[j])
        break
    else:
        continue

if ext not in di:
    print("The file is not valid")
