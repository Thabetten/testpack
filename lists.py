def makes(inlist):
    olist = [[i] for i in inlist[0]]
    for k in inlist[len(olist[len(olist) - 1]):]:
        temp = []
        for j in olist: 
            for n in k:
                if j[len(j) - 1] > n:
                    temp.append(j + [n])
            olist = temp

    return olist