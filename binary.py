l,num=[],int(input("enter the num"))
while num>1:
    l.append(num%2)
    num=int(num/2)
    l.append(l)
    print("binary equivelent=",l[::-1])