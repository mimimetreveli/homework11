with open("oscar", "r") as obj:
    oscar={}
    ages={}
    for line in obj:
        parts=line.strip().split(",")
        year=int(parts[0])
        oscar[year]=[parts[3]]
        ages[year]=int(parts[2])
youngest=min(ages.values())
youngest_years=[y for y, a in ages.items() if a==youngest]
for y in youngest_years:
    print(oscar[y], ages[y])
year=int(input("Enter the year: "))
print(oscar[year])
