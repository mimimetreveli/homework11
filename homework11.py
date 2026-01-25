with open("numbers", "r") as obj:
     squared_nums=[]
     for line in obj:
        squared_nums.append(int(line)**2)
obj2=open('squared_nums','w')
obj2.write(str(squared_nums))
