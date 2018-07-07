principle=float(input('Enter the principle amount:'))
rate=(float(input('Enter the rate (in %):')))/100
time=int(input('Enter the time in years:'))
ntime=int(input('No. of times it\'s compounded per year:'))
interest=principle*((1+rate/ntime)**(ntime*time)) - principle
print('Compound interest (excluding principle amount) is: ₹'+str(interest))