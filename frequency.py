mystr = "tom, dick, harry, three, one, three, tom, harry, jon, one, jon, harry"
mylist = mystr.split()

mylist1 = set(mylist)
mylist2 = list(mylist1)

count  = [0] * len(mylist2)
mydict = dict()
for i in range(len(mylist2)):
    for j in range (len(mylist)):
        if mylist2[i] == mylist[j]:
            count[i] += 1
    mydict[mylist2[i]] = count[i]
print(mydict)