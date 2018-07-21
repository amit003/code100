n=int(input("enter the no"))
l,flag=[],1
while(n>0):
    l.append(n%8)
    n=int(n/8)
    print(l[::-1])