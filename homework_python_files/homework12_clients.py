with open("../files/clients", "r") as obj:
    ppl_sp_g=[]
    ppl_mails=[]
    countries={"Spain","Germany"}
    for line in obj:
        parts=line.strip().split(";")
        year=int(parts[3].strip().split("/")[2])
        if parts[2]=="Spain" or parts[2]=="Germany":
            ppl_sp_g.append(parts[0])
        if year==2011:
            ppl_mails.append(parts[1])
        countries.add(parts[2])
with open("../files/ppl_in_spain_or_germany", "w") as obj:
    obj.write(";".join(ppl_sp_g))
print(ppl_mails)
print(list(countries))
