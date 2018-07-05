text =input('Enter a String : ')
reverse =''
for a in range (len(text)-1,-1,-1):
    reverse+=text[a]
    print(reverse)